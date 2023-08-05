"""Launch a nextflow workflow."""

import argparse
import logging
import os
import subprocess
import sys
from typing import Union

from epi2melabs.workflows.database import get_session, Instance, Statuses


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Execute a netflow workflow and update the database.",
        usage=(
            "invoke_nextflow -w epi2melabs/wf-alignment -i <instance_id> "
            "-w <workflow_name> -p <params_file> -r <revision> "
            "-wd <work_dir> -l <log_file> -s <stdout_file> -d <database>"
        )
    )

    parser.add_argument(
        '-n',
        '--nextflow',
        required=True,
        default='nextflow',
        help='Path to the nextflow executable.'
    )

    parser.add_argument(
        '-i',
        '--id',
        required=True,
        help='ID of the database instance record to acquire and update.'
    )

    parser.add_argument(
        '-w',
        '--workflow',
        required=True,
        help='Path to or name of the workflow to be run.'
    )

    parser.add_argument(
        '-p',
        '--params',
        required=True,
        help='Path to the workflow params file.'
    )

    parser.add_argument(
        '-r',
        '--revision',
        required=False,
        default=None,
        help='Workflow revision to execute.'
    )

    parser.add_argument(
        '-wd',
        '--work_dir',
        required=True,
        help='Path to what should become the working directory.'
    )

    parser.add_argument(
        '-l',
        '--log_file',
        required=True,
        help='Path to which the logs should be written.'
    )

    parser.add_argument(
        '-s',
        '--std_out',
        required=True,
        help='Path to which the stdout should be written.'
    )

    parser.add_argument(
        '-d',
        '--database',
        required=True,
        help='Path to the SQLITE database to update.'
    )

    parser.add_argument(
        '-wsl',
        action='store_true',
        help='Run command in wsl'
    )

    start = 0
    if 'invoke_nextflow' in sys.argv[0]:
        start = 1

    return parser.parse_args(sys.argv[start:])


def invoke(
    id: str, workflow: str, params: str, work_dir: str,
    log_file: str, std_out: str, database: str, nextflow: str,
    revision: Union[str, None] = None, wsl: bool = False,
) -> None:
    """Run nextflow workflow."""
    logging.basicConfig(
        format='invoke_nextflow <%(asctime)s>: %(message)s',
        level=logging.DEBUG)

    logging.info('Initialising.')
    # This fixes the invocation when it contains spaces
    nextflow = fr"{nextflow}"

    pull_command = None
    if not os.path.isfile(workflow):
        pull_command = [nextflow, 'pull', workflow]

    run_command = [
        nextflow, '-log', log_file, 'run', workflow,
        '-params-file', params, '-w', work_dir,
        '-ansi-log', 'false']

    if wsl:
        logging.info('Setting command to run in WSL.')
        run_command = ['wsl'] + run_command
        if pull_command:
            pull_command = ['wsl'] + pull_command

    if revision:
        logging.info(f'Using revision {revision}.')
        run_command = run_command + ['-r', revision]

    logging.info(f'Command: {" ".join(run_command)}.')

    # Get the invocation instance by id
    db = get_session(database)
    invocation = db.query(Instance).get(id)

    # Update the invocation with the current pid
    pid = os.getpid()
    logging.info(f'The wrapper PID is {pid}.')
    invocation.pid = pid
    db.commit()

    # Set up outputs
    cli_logfile = open(std_out, 'a')
    stdout = cli_logfile
    stderr = cli_logfile
    proc = None

    try:
        # Update the workflow
        if pull_command:
            logging.info('Updating workflow.')
            proc = subprocess.Popen(
                pull_command, stdout=stdout, stderr=stderr)
            if proc.wait():
                logging.info(
                    'Could not update workflow, are you connected '
                    'to the internet?')

        # Invoke the command
        logging.info('Launching workflow.')
        proc = subprocess.Popen(
            run_command, stdout=stdout, stderr=stderr)
        logging.info(f'The workflow PID is {proc.pid}.')

        # Set initial database status
        invocation.status = Statuses.LAUNCHED
        db.commit()

        # Wait for the exit status
        ret = proc.wait()
        sys.exit(ret)

    # If we receive sigint, assume the process was
    # terminated intentionally and exit gracefully
    except KeyboardInterrupt:
        logging.info('Interrupt detected: terminating workflow.')
        if proc:
            proc.kill()
        invocation.status = Statuses.TERMINATED
        db.commit()
        sys.exit(0)

    except SystemExit as e:
        # If we receive system exit of 0, assume the process
        # ended peacefully and exit gracefully.
        if not e.code:
            logging.info('Workflow completed.')
            invocation.status = Statuses.COMPLETED_SUCCESSFULLY
            db.commit()
            sys.exit(0)

        # If we receive a non-zero system exit update the
        # status to reflect an error. Exit with code 1.
        logging.info('Workflow encountered an error.')
        logging.info('See nextflow output for details.')
        invocation.status = Statuses.ENCOUNTERED_ERROR
        db.commit()
        sys.exit(1)

    # This error is thrown if the path to Nextflow
    # is not available, and therefore cannot be launched
    except FileNotFoundError as e:
        logging.info(f"Cant find '{nextflow}' on the path.")
        logging.info(e)
        invocation.status = Statuses.ENCOUNTERED_ERROR
        db.commit()
        sys.exit(1)

    # Handle all other exception classes in the event of
    # unhandled exceptions occurring within the callable.
    # Set the status to error and exit with code 1.
    except Exception as e:
        logging.info('Workflow encountered an error.')
        logging.info(e)
        invocation.status = Statuses.ENCOUNTERED_ERROR
        db.commit()
        sys.exit(1)


def main():
    """Parse arguments and launch a workflow."""
    args = parse_args()
    invoke(
        id=args.id,
        workflow=args.workflow,
        params=args.params,
        revision=args.revision,
        work_dir=args.work_dir,
        log_file=args.log_file,
        std_out=args.std_out,
        database=args.database,
        nextflow=args.nextflow,
        wsl=args.wsl)


if __name__ == '__main__':
    main()

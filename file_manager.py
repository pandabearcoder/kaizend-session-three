import logging
from pathlib import Path


log = logging.getLogger(__name__)


def _get_files_in_dir(path):
    print(path)
    try:
        if path.is_dir():
            for f in path.iterdir():
                print(_get_files_in_dir(f))
    except PermissionError:
        log.warn('Permission Denied')


def list_files(args):
    path = Path(args.path).resolve()

    if not path.exists():
        print('Path does not exist')
    elif path.is_dir():
        _get_files_in_dir(path)
    else:
        print(path)


def list_pattern(args):
    path = Path().glob(args.path)

    for f in path:
        print(f)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    # Add your own script parameters here...
    list_files_parser = subparser.add_parser('ls')
    list_files_parser.set_defaults(func=list_files)
    list_files_parser.add_argument('path', help='Path to list files from')

    list_pattern_parser = subparser.add_parser('ls_pattern')
    list_pattern_parser.set_defaults(func=list_pattern)
    list_pattern_parser.add_argument('path', help='Path to list files from')

    # Default parameters and parameter initialization
    parser.add_argument(
        '-L', '--log-level',
        help='set log level',
        default='INFO',
    )
    parser.add_argument(
        '--log-file',
        help='set log file',
    )
    args = parser.parse_args()

    # Configure logging
    log_params = {
        'filename': args.log_file,
        'level': getattr(logging, args.log_level.upper()),
        'format': (
            '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
        ),
    }
    logging.basicConfig(**log_params)

    # Run
    args.func(args)

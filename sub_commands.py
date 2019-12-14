import logging

log = logging.getLogger(__name__)


def bacon(args):
    with open(args.file) as f:
        print(f.read())


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    # Add your own script parameters here...
    bacon_parser = subparser.add_parser('bacon')
    bacon_parser.set_defaults(func=bacon)
    bacon_parser.add_argument('file')

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

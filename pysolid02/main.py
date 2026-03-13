import argparse
import sys

from util import init_logger


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='[ALURA] py solid 02')
    parser.add_argument('--run', choices=['run'], help='View availiable: [cli | tk]')
    args = parser.parse_args()

    logger = init_logger(log_type='normal')

    if args.run == 'run':
        print('Then run...')
    else:
        print('No run...')
        sys.exit(1)

    sys.exit(0)

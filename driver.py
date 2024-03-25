#! /usr/bin/env python3

import argparse, os, sys

from util import run_stellarium

if __name__ == '__main__':
  parser = argparse.ArgumentParser(add_help=False,
                                formatter_class=argparse.RawTextHelpFormatter,
                                description=sys.argv[0] + ' - Space image CV',
                                argument_default=argparse.SUPPRESS,
                                prog=sys.argv[0])
  parser.add_argument('-h', '--help', action='store_true',
                      help='show this help message.')
  parser.add_argument('-s', '--stellarium', action='store_true',
                      help='Run Stellarium to generate images')
  args = vars(parser.parse_args())
  if 'help' in args:
    parser.print_help()
    sys.exit(0)
  basedir=os.path.sep.join(os.path.realpath(__file__).split(os.path.sep)[:-1])
  if 'stellarium' in args:
    ret = run_stellarium(basedir)
    if ret == 0: print('Stellarium completed successfully')
    else: print('Stellarium exited with code', ret)


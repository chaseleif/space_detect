#! /usr/bin/env python3

import argparse, os, sys

from util import run_stellarium
from starcv import markSatellites, getStats

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
  parser.add_argument('-t', '--test', action='store_true',
                      help='Run under construction test')
  args = vars(parser.parse_args())
  if 'help' in args:
    parser.print_help()
    sys.exit(0)
  basedir=os.path.sep.join(os.path.realpath(__file__).split(os.path.sep)[:-1])
  if 'stellarium' in args:
    ret = run_stellarium(basedir)
    if ret == 0: print('Stellarium completed successfully')
    else: print('Stellarium exited with code', ret)
  if 'test' in args:
    imgpath = os.path.join(basedir, 'data')
    if not os.path.isdir(imgpath):
      print(f'Data directory {imgpath} doesn\'t exist')
      sys.exit(1)
    imgnum = 1
    imgname = os.path.join(imgpath, f'img{imgnum:03d}.png')
    cont = True
    while cont and os.path.isfile(imgname):
      #markSatellites(imgname)
      getStats(imgname)
      imgnum += 1
      imgname = os.path.join(imgpath, f'img{imgnum:03d}.png')
      #cont = input('Continue? [y/N]: ')
      #cont = cont.lower().startswith('y')


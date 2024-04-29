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
  parser.add_argument('-d', '--detect', action='store_true',
                      help='Run satellite detection on input')
  parser.add_argument('--show', action='store_true', default=False,
                      help='Show output images')
  parser.add_argument('--dontsave', action='store_true', default=False,
                      help='Don\'t save output images')
  parser.add_argument('--pause', action='store_true',
                      help='Pause and prompt to continue after each frame')
  parser.add_argument('--split', action='store_true',
                      help='Produce split image output showing image stages')
  parser.add_argument('--truth', action='store_true',
                      help='Produce truth image output and create csv output')
  args = vars(parser.parse_args())
  if 'help' in args:
    parser.print_help()
    sys.exit(0)
  basedir=os.path.sep.join(os.path.realpath(__file__).split(os.path.sep)[:-1])
  if 'stellarium' in args:
    ret = run_stellarium(basedir)
    if ret == 0: print('Stellarium completed successfully')
    else: print('Stellarium exited with code', ret)
  if 'detect' not in args and ('split' in args or 'truth' in args):
    args['detect'] = True
  if 'detect' in args:
    imgpath = os.path.join(basedir, 'data')
    if not os.path.isdir(imgpath):
      print(f'Data directory {imgpath} doesn\'t exist')
      sys.exit(1)
    pause = 'pause' in args
    truth = 'truth' in args
    args = {'splitimg':args['split'] if 'split' in args else False,
            'show':args['show'],
            'save':not args['dontsave']}
    if truth: print('image,num_sats,tp,fp,missed')
    imgnum = 1
    imgname = os.path.join(imgpath, f'img{imgnum:03d}.png')
    processimg = getStats if truth else markSatellites
    while os.path.isfile(imgname):
      processimg(imgname, **args)
      if pause and not input('Continue? ').lower().startswith('y'):
        break
      imgnum += 1
      imgname = os.path.join(imgpath, f'img{imgnum:03d}.png')


#! /usr/bin/env python3

import os
from subprocess import Popen, DEVNULL

# Runs Stellarium given the basic usage described in ../stellarium/README.md
def run_stellarium(basedir):
  os.environ['STELLARIUM_OUTPUTDIR'] = os.path.join(basedir, 'data')
  os.makedirs(os.environ['STELLARIUM_OUTPUTDIR'], exist_ok=True)
  script = os.path.join(basedir, 'stellarium', 'screenshots.ssc')
  cmd = ['stellarium', '--startup-script', script]
  proc = Popen(cmd, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
  proc.communicate()
  return proc.returncode


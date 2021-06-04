#!/usr/bin/env python3
import sys
import subprocess
# accept input file from command line
inputfile = sys.argv[1]
# read each line from file and rename the file name in the line.
# perform actual file renaming to the file system
with open(inputfile, 'r') as  f:
  for line in f:
    mline = line.strip().replace('jane', 'jdoe')
    subprocess.run(['mv', line.strip(), mline])


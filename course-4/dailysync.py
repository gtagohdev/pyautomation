#!/usr/bin/env python3
import subprocess
import os
from multiprocessing import  Pool

# Determine source and target root directory for backup
backupfrom = 'data/prod'
backupto = 'data/prod_backup'

def runsync(targetname):  
  ''' Use rsync command to backup delta at the given directory recursively '''
  fromdir = os.path.join(os.path.expanduser('~'), backupfrom, targetname)
  todir = os.path.join(os.path.expanduser('~'), backupto, targetname)
  print('backup delta (recursively) from: {}'.format(fromdir))
  print('backup delta (recursively) to: {}'.format(todir))
  subprocess.call(['rsync', '-arq', fromdir, todir])
  
def backup_delta():
  ''' Read first level subdirectory names based on the given root directory 
      to backup from and use multiprocessing Pool module functionality to 
      perform the delta copying on each subdirectory parallelly '''
  backuproot = os.path.join(os.path.expanduser('~'), backupfrom)
  #traverse through first level of directory and files start from the given src path
  root, dirs, files = next(os.walk(backuproot, topdown=True))
  print(dirs)
  p = Pool(len(dirs))
  p.map(runsync, dirs)

if __name__ == '__main__':
  # This program only processes backup directories in relative to the default working directory (home)  
  backup_delta()


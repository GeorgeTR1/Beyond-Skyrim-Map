from sys import argv
from glob import glob
import shutil
import os

maxSize = int(1.8e9)
curSize = 0

newdir = argv[1] + '_out'

oldFiles = glob("**", root_dir=argv[1], recursive=True)
newFiles = glob("**", root_dir=newdir, recursive=True)

remainingFiles = sorted(set(oldFiles) - set(newFiles))

if not os.path.exists(newdir):
   os.mkdir(newdir)

for file in remainingFiles:
   oldfile = os.path.join(argv[1], file)
   newfile = os.path.join(newdir, file)
   if os.path.isdir(oldfile):
      os.mkdir(newfile)
   else:
      curSize += os.path.getsize(oldfile)
      if curSize > maxSize:
         break
      shutil.copy(oldfile, newfile)
      print(oldfile)
   
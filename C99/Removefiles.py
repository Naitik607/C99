import os
from os import path
import shutil
import time

# enter your folder or drive or path to remove file
path_file = r"/bin"
#C:\   

now = time.time() - 30 * 86400

# using f instead of path because the  files and subfolders exist in the path can listed 
def main():
  if(path.exists(path_file)) == True:
    for dirpath, subdirs,files in os.walk(path_file):
      for f in os.listdir(path_file):
        if os.stat(f).st_ctime < now:
          if os.path.isfile(f):
            shutil.rmtree(os.path.join(path_file,f))
  else:
    print('file is not found')
  
main()

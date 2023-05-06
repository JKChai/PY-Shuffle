## Jin Kun Chai
## 05/06/2023
import os
import shutil
import random

dirpath = '/mnt/c/Users/chai8/repos/PY-Shuffle/archive/'
destDirectory = '/mnt/c/Users/chai8/repos/PY-Shuffle/brain_data'

print(os.listdir(dirpath + 'Training/'))



# filenames = random.sample(os.listdir(dirpath), 100)

# for fname in filenames:
#     srcpath = os.path.join(dirpath, fname)
#     shutil.copyfile(srcpath, destDirectory)
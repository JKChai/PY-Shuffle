## Jin Kun Chai
## 05/06/2023
import os
import shutil
import random

dirpath = 'C:/Users/chai8/source/repos/PY-Shuffle/archive/'
destDir = 'C:/Users/chai8/source/repos/PY-Shuffle/brain_data'

train_dir = dirpath + 'Training/'
test_dir  = dirpath + 'Testing/'
# ['glioma', 'meningioma', 'notumor', 'pituitary'] ## 530,530,1590,530
# print(len(os.listdir(notumortrainpath))) ## 1595 / 3 = 531

train_counts = []
train_labels = []

for label in os.listdir(train_dir):
    train_labels.append(label)
    train_counts.append(len(os.listdir(train_dir+label)))

print(train_labels)
print(train_counts)


# print(len([name for name in os.listdir(notumortrainpath) if os.path.isfile(name)]))


x_labels = ['glioma', 'meningioma', 'pituitary']

# for x_label in x_labels:
#     filenames = random.sample(os.listdir(train_dir + x_label), 530)

#     for fname in filenames:
#         srcpath = os.path.join(train_dir + x_label, fname)
#         # print(srcpath)
#         shutil.copy(srcpath, destDir + 'train/tumor')

## testing data
for x_label in x_labels:
    filenames = random.sample(os.listdir(test_dir + x_label), 135)

    for fname in filenames:
        srcpath = os.path.join(test_dir + x_label, fname)
        shutil.copy(srcpath, destDir + '/test/tumor')
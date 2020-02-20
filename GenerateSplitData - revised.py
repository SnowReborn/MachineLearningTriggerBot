import numpy as np
import os, shutil
from sklearn.model_selection import train_test_split

"""
Format of
Data
    RawData
​
    ClassifiedData
        hit
        miss
​
    SplitData
        train
            hit
            miss
        test
            hit
            miss
        validation
            hit
            miss
​
Generate SplitData


GenerateSplitData.py:
- creates the folder hierarchy found under SplitData above if the folders do not already exist
- copies over files from ClassifiedData to populate SplitData
- adds the ratio of files to train, test, and validation folders when it copies over the files
"""

train_size = .5
test_size = .25
validation_size = .25
assert train_size + test_size + validation_size == 1

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
split_dir = os.path.join(base_dir, 'SplitData')
class_dir = os.path.join(base_dir, 'ClassifiedData')

folders = ('train', 'test', 'val')
classes = ('hit', 'miss')

def safe_mkdir(path):
	"""More safely runs mkdir only if path doesn't already exist."""
	if os.path.exists(path):
    	#print('Cannot make path' + path + '. Path already exists.')
		pass
	else:
		os.mkdir(path)

safe_mkdir(split_dir)

for folder in folders:
	safe_mkdir(os.path.join(split_dir, folder))
	for c in classes:
		safe_mkdir(os.path.join(split_dir, folder, c))
print("Done making subdirectories.")

split = {}
for c in classes:
	lst_hit = os.listdir(os.path.join(class_dir, c))
	train, test = train_test_split(lst_hit, shuffle = True, train_size = train_size)
	test, val = train_test_split(test, train_size = test_size / (1 - train_size))
	split[c] = {'train': train, 'test': test, 'val':val}
print("Done generating split.")

for folder in folders:
	for c in classes:
		for fname in split[c][folder]:
			source = os.path.join(class_dir, c, fname)
			destination = os.path.join(split_dir, folder, c, fname)
			shutil.copyfile(source, destination)
print("Done populating subdirectories.")

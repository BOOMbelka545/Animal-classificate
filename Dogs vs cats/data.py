import os, shutil


dataset_dir_for_cat = '/home/boombelka/PycharmProjects/Neural_Network/Dogs vs cats/images_cats_dogs/Cat'
dataset_dir_for_dog = '/home/boombelka/PycharmProjects/Neural_Network/Dogs vs cats/images_cats_dogs/Dog'


base_dir = '/home/boombelka/PycharmProjects/Neural_Network/Dogs vs cats/cats_and_dogs_small'
os.mkdir(base_dir)

#Dir for test
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

test_cats_dir = os.path.join(test_dir, 'cats')
os.mkdir(test_cats_dir)

test_dogs_dir = os.path.join(test_dir, 'dogs')
os.mkdir(test_dogs_dir)

# Dir for train
train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)

train_cats_dir = os.path.join(train_dir, 'cats')
os.mkdir(train_cats_dir)

train_dogs_dir = os.path.join(train_dir, 'dogs')
os.mkdir(train_dogs_dir)

#Dir for validation
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)

validation_cats_dir = os.path.join(validation_dir, 'cats')
os.mkdir(validation_cats_dir)

validation_dogs_dir = os.path.join(validation_dir, 'dogs')
os.mkdir(validation_dogs_dir)

#Copy cats photo for train
fnames = ['{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(dataset_dir_for_cat, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)

#Copy cats photo for validation
fnames = ['{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(dataset_dir_for_cat, fname)
    dst = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src, dst)

#Copy cats photo for test
fnames = ['{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(dataset_dir_for_cat, fname)
    dst = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src, dst)

#Copy dogs photo for train
fnames = ['{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(dataset_dir_for_dog, fname)
    dst = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src, dst)

#Copy dogs photo for validation
fnames = ['{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(dataset_dir_for_dog, fname)
    dst = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src, dst)

#Copy dogs photo for test
fnames = ['{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(dataset_dir_for_dog, fname)
    dst = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src, dst)







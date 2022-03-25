import os, shutil

full_CAT_dir = '/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Cat'
full_DOG_dir = '/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Dog'
Base_dir = '/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/Basa_date'

# dir
train = os.path.join(Base_dir, 'train')
os.mkdir(train)

test = os.path.join(Base_dir, 'test')
os.mkdir(test)

validation = os.path.join(Base_dir, 'validation')
os.mkdir(validation)

#train dir

train_cat = os.path.join(train, 'cat')
os.mkdir(train_cat)
train_dog = os.path.join(train, 'dog')
os.mkdir(train_dog
)
# test dir

test_cat = os.path.join(test, 'cat')
os.mkdir(test_cat)
test_dog = os.path.join(test, 'dog')
os.mkdir(test_dog)

# validation dir

validation_cat = os.path.join(validation, 'cat')
os.mkdir(validation_cat)
validation_dog = os.path.join(validation, 'dog')
os.mkdir(validation_dog)

#copy date for train

for i in range(7500):
    shutil.copyfile(f'/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Cat/{i}.jpg', train_cat + '/cat' +f'{i}.jpg')

for i in range(7500):
    shutil.copyfile(f'/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Dog/{i}.jpg', train_dog + '/dog' + f'{i}.jpg')

# copy date for test

for i in range(int(len(os.listdir(full_CAT_dir))*0.6), int(len(os.listdir(full_CAT_dir))*0.8)):
    shutil.copyfile(f'/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Cat/{i}.jpg', test_cat + '/cat' + f'{i}.jpg')

for i in range(int(len(os.listdir(full_CAT_dir))*0.6), int(len(os.listdir(full_CAT_dir))*0.8)):
    shutil.copyfile(f'/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Dog/{i}.jpg', test_dog + '/dog' +  f'{i}.jpg')

# copy date for validation

for i in range(int(len(os.listdir(full_CAT_dir))*0.8), len(os.listdir(full_CAT_dir))-1):
    shutil.copyfile(f'/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Cat/{i}.jpg', validation_cat + '/cat' + f'{i}.jpg')

for i in range(int(len(os.listdir(full_CAT_dir))*0.8), len(os.listdir(full_CAT_dir))-1):
    shutil.copyfile(f'/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/images_cats_dogs/Dog/{i}.jpg', validation_dog + '/dog' + f'{i}.jpg')
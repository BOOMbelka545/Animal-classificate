from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from keras import models
from tensorflow.keras import optimizers 
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras.models import load_model
from matplotlib import pyplot as plt


# Architect model
model = models.Sequential()
model.add(Conv2D(input_shape=(150,150,3),filters=64,kernel_size=(3,3),padding="same", activation="relu"))
model.add(Conv2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Flatten())                                                                                                                                                                            
model.add(Dropout(0.5))
model.add(Dense(1024, activation='relu'))
model.add(Dense(2048, activation='relu'))
model.add(Dense(2, activation='softmax'))                                                                                                                                                                                           

model.compile(optimizer=optimizers.Adam(lr=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy'])

# Preparation of the data

train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'Basa_date/train',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    shuffle=True,
    seed=42 
)
train_generator.save_to_dir

validation_generator = test_datagen.flow_from_directory(
    'Basa_date/validation',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    shuffle=True, 
    seed=42 
) 


print(model.summary())
 
history = model.fit_generator(
    train_generator,
    shuffle=True,
    steps_per_epoch=50,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=32,
    
)

model.save('model.h5')

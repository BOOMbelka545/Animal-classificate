from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import preprocessing
import numpy as np


model = load_model('/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/model1.h5')

test_datagen = ImageDataGenerator(
    rescale=1./255
)

# date_test = test_datagen.flow_from_directory(
#     '/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/Basa_date/test/',
#     target_size=(150, 150),
#     class_mode='categorical')


# results = model.evaluate(date_test, batch_size=64)
# print("test loss, test acc:", results)


#predict

def predict():
    image = preprocessing.image.load_img('/home/boombelka/ПРОГРАММИРОВАНИЕ/animal_recognition/test.jpg')
    image = np.resize(image, (150,150,3))
    input_arr = preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) / 255
    print(input_arr)
    predictions = model.predict(input_arr)
    print(predictions)
    return "Cat" if np.argmax(predictions) == 0 else "Dog"

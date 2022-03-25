import glob
from PIL import Image

imagepath = '/home/boombelka/PycharmProjects/Neural_Network/animal_recognition/Basa_date/validation/cat' 

imgs_names = glob.glob(imagepath+'//*.jpg')

for imgname in imgs_names: 
    img = Image.open(imgname) 
    if img is None:     
        print('dsgdggd')
        print(imgname)
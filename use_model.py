import cv2 as cv 
import numpy as np
import tensorflow as tf

CATEGORY = ["adi" , "Nadi"]
CATEGORY_SHOW = ["this is Aditya" , "this is not Aditya"]

'''
face_cascade = 'haarcascade_frontalface_alt.xml'
face_cascade_name = face_cascade
face_cascade = cv.CascadeClassifier()
face_cascade.load(face_cascade_name)'''
def prepare(filepath):
    IMAGE_SIZE = 100
    image_array = cv.imread(filepath , cv.IMREAD_GRAYSCALE)
    new_array = cv.resize(image_array , (IMAGE_SIZE,IMAGE_SIZE))
    return new_array.reshape(-1 , IMAGE_SIZE , IMAGE_SIZE ,1) 

model = tf.keras.models.load_model('addi.model')

prediction = model.predict([prepare('2.jpg')])
print(CATEGORY_SHOW[int(prediction)])

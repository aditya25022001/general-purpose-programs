import cv2 as cv
'''
import tensorflow as tf
CATEGORIES = ["zero" , "one" ,"two" ,"three" ,"four" ,"five" ,"six" ,"seven" ,"eight" ,"nine"]
def pred(filename):
    image_size = 28
    image_array = cv.imread(filename , cv.IMREAD_GRAYSCALE)
    img = cv.resize(image_array , (image_size,image_size))
    return img.reshape(1,image_size*image_size)

model = tf.keras.models.load_model("digit.model")
prediction = model.predict([pred('test.jpg')])
print(CATEGORIES[int(prediction[0][0])])
'''
image = cv.imread('s3.jpg' , cv.IMREAD_GRAYSCALE)
image2 = cv.resize(image , (50,50))
cv.imwrite('shivajig.png',image2)
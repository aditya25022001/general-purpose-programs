#importing necessary packages
import numpy as np
import cv2 as cv
from keras.datasets import mnist
from keras.utils import np_utils
from keras.layers import Dense , Dropout ,Activation,Flatten
from keras.layers import Conv2D , MaxPool2D
from tensorflow.keras.callbacks import TensorBoard
from keras.models import Sequential

#loading and printing data 
(xtr , ytr) , (xte , yte) = mnist.load_data()
print('Loading data.......')
print('X training : ' , xtr.shape ,  type(xtr))
print('Y training : ' , ytr.shape)
print('X test : ' , xte.shape)
print('y test : ' , yte.shape)


#flattening data i.e converting all 2D matrices of size 28x28
#to 1D vector or matrix as an input layer in form of float32
#basic structure of neural network
#we are creating a neural network not convolutional neural neywork
xtr = xtr.reshape(xtr.shape[0] , xtr.shape[1],xtr.shape[2] , 1)
xte = xte.reshape(xte.shape[0] , xte.shape[1],xte.shape[2] , 1)
xtr = xtr.astype('float32')
xte = xte.astype('float32')

#normalizing the data i.e. converting pixel value of 255 to 1
#basically converting range of 0-->255 to 0-->1
xtr  = xtr/255
xte  = xte/255

#now classifying the data into different classes 
#i.e. 10 digits so classifying the 60000 images into 10 classes
#real machine learning begins
n_classes = 10
print('shape before classification y training : ',ytr.shape)
print('shape before classification y test : ',yte.shape)
Ytr = np_utils.to_categorical(ytr,n_classes)
Yte = np_utils.to_categorical(yte,n_classes)
print('shape after classification y training : ',Ytr.shape)
print('shape after classification y test : ',Yte.shape)

#building nueral network 
model = Sequential()
model.add(Dense(100,input_shape=(784,), activation='relu'))
model.add(Dense(200,input_shape=(784,), activation='relu'))
model.add(Dense(10, activation='softmax'))

#summary of the model
model.summary()

#compiling the model 
model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')

#training the model for 10 epochs
#1 epoch means that all the data goes through the layers once
model.fit(xtr , Ytr , batch_size=128 , epochs=10 , validation_data=(xtr , Ytr))
model.save("digit.model")

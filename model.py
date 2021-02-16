import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D , MaxPooling2D , Dense , Activation , Dropout , Flatten
import pickle

X = pickle.load(open("X.pickle" , "rb"))
y = pickle.load(open("y.pickle" , "rb"))
print(type(X) , type(y))

model = Sequential()
model.add(Conv2D(64 , (3,3) , input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64 , (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model.fit(X , y , batch_size=2,epochs=20,validation_split=0.1)

model.save('addi.model')
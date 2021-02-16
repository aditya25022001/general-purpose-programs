import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random
import pickle

DATADIR = 'trainmod'
CATEGORIES = ["adi" , "Nadi"]
 
for category in CATEGORIES:
    path = os.path.join(DATADIR , category)
    for img in os.listdir(path):
        image_array = cv.imread(os.path.join(path , img) , cv.IMREAD_GRAYSCALE)

training_data = []
def data_load():
    for category in CATEGORIES:
        path = os.path.join(DATADIR , category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            image_array = cv.imread(os.path.join(path , img) , cv.IMREAD_GRAYSCALE)
            training_data.append([image_array , class_num])

data_load()
random.shuffle(training_data)
X = []
y = []
for features , label in training_data:
    X.append(features)
    y.append(label)
random.shuffle(X)
random.shuffle(y)
X = np.array(X).reshape(-1 , 100 , 100 , 1)
y = np.array(y)
X = X/255
print(type(y))
for i in y[:10]:
    print(y[i])


pickle_out = open("X.pickle" , "wb")
pickle.dump(X , pickle_out)
#print(X[0])
pickle_out.close()
pickle_out = open("y.pickle" , "wb")
pickle.dump(y , pickle_out)
pickle_out.close()

import numpy as np
import cv2 as cv
import matplotlib.pyplot as mt
filename = input('enter file name: ')
img1 = cv.imread(filename , 0)
img2 = cv.imread('realOrange.jpg' , 0)
img3 = cv.imread('apple.jpg' , 0)
orb = cv.ORB_create()
kp1 , des1 = orb.detectAndCompute(img1 , None)
kp2 , des2 = orb.detectAndCompute(img2 , None)
kp3 , des3 = orb.detectAndCompute(img3 , None)
bf = cv.BFMatcher()
matches = bf.match(des1 , des2 , None)
matches1 = bf.match(des1 , des3 , None)
matches = sorted(matches , key=lambda x: x.distance)
matches1 = sorted(matches1 , key=lambda x: x.distance)
count = len(matches)  
count1 = len(matches1)
print(count , count1)
img4 = cv.drawMatches(img1 , kp1 , img2 , kp2 , matches[:] , None , flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
img5 = cv.drawMatches(img1 , kp1 , img3 , kp3 , matches[:] , None , flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
if count>count1:
    print('it is an orange')
    
else:
    print('it is an apple')
mt.imshow(img4) , mt.show()
mt.imshow(img5) , mt.show()
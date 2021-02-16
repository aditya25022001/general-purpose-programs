#importing important packages
from __future__ import print_function  
from __future__ import division
import argparse
import imutils 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
#smiling face calculator
def smile_face(frame):
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        frame = cv.rectangle(frame,(x,y),(x+w,y+h),0,2)
        faceROIG = gray[y+h//2:y+h,x:x+w]
        faceROIC = frame[y:y+h,x:x+w]
        smiles = smile_cascade.detectMultiScale(faceROIG)
        for x2,y2,w2,h2 in smiles:
            cv.rectangle(faceROIC,(x2,y2),(x2+w2,y2+h2),0,1)
    cv.imshow('smile',frame)
ap = argparse.ArgumentParser(description='code to parse necessary files')
ap.add_argument('--smile_cascade',help='path to xml file',default='haarcascade_smile.xml')
ap.add_argument('--face_cascade',help='path to xml file',default='haarcascade_frontalface_alt.xml')
ap.add_argument('--camera',help='camera divide number',type=int,default=0)
args = ap.parse_args()
smile_cascade_name = args.smile_cascade
face_cascade_name = args.face_cascade
smile_cascade = cv.CascadeClassifier()
face_cascade = cv.CascadeClassifier()
smile_cascade.load(smile_cascade_name)
face_cascade.load(face_cascade_name)
camera_device = args.camera
cap = cv.VideoCapture(camera_device)
while True:
    ret,frame = cap.read()
    smile_face(frame)
    if cv.waitKey(10) == 27:
        break
'''
'''
inpu = np.arange(1,10).reshape(3,3)
print(inpu)
#print(inpu.shape[:2])
weights = np.random.rand(inpu.shape[1],4)
print(weights)
'''
'''
#template matching
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
face_cascade.load(face_cascade_name)
eyes_cascade.load(eyes_cascade_name)
images = ['i1.jpg','i2.jpg','i3.jpg','i4.jpg','i5.jpg','i6.jpg','i7.jpg'] 
for img in images:
    img2 = cv.imread(img)
    resize = imutils.resize(img2,width=500)
    faces = face_cascade.detectMultiScale(resize)
    for (x,y,w,h) in faces:
        centre = (x+w//2 , y+h//2)
        resize = cv.ellipse(resize,centre,(w//2,h//2),0,0,360,(255,0,255),4)
    cv.imshow('face',resize)
    cv.waitKey(0)
'''
'''
    res = cv.matchTemplate(resize,template,cv.TM_CCOEFF_NORMED)
    minv,maxv,minl,maxl = cv.minMaxLoc(res)
    top_left = maxl
    bottom_right = (top_left[0] + w , top_left[1] + h)
    cv.rectangle(resize,top_left,bottom_right,0,3)
    cv.imshow('template',resize)
    cv.waitKey(0)
'''

#face detection using video capture
def detect_face(frame):
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#    gray = cv.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detect_face(frame)
    cv.waitKey(10)


'''
#background removal....
image = cv.imread('s6.jpeg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey(0)
'''

#rolls = np.random.randint(1,6,10)
#print(rolls)
#print(dir(cv) , sep='/n')

'''
alpha_max = 100
title = 'Linear Blend'
def value(val):
    alpha = val/alpha_max
    beta = (1.0-alpha)
    dst = cv.convertScaleAbs(src1 , alpha=alpha*2 , beta=beta)
    cv.imshow(title,dst)
ap = argparse.ArgumentParser(description='code for adding trackbar to image')
ap.add_argument('--input1',help='path to image1')
args = ap.parse_args()
src1 = cv.imread(cv.samples.findFile(args.input1))
cv.namedWindow(title)
track_bar =  'Brightness'
cv.createTrackbar(track_bar,title,0,alpha_max,value)
value(0)
cv.waitKey(0)
'''
'''
#reading showing image
image1 = cv.imread('s3.jpg')
cv.imshow('Shivaji' , image1)
cv.waitKey(0)

#calculating dimensions of image
(h,w,c) = image1.shape
print("height = {} width = {} channels = {}".format(h,w,c))

#slicing images
roi = image1[:350 , 60:350]
cv.imshow('roi' , roi)
cv.waitKey(0)

#drawing on image
output = image1.copy()
cv.rectangle(output,(60,5),(350,350),(0,0,255),1)
cv.imshow('face',output)
cv.waitKey(0)

#resizing images using aspect ratio
r = 300/w
dim = (300,int(h*r))
image2 = imutils.resize(image1,width=300)
cv.imshow('resized',image2)
cv.waitKey(0)

#rotating the images
#centre = (w//2 , h//2)
#m = cv.getRotationMatrix2D(centre , -45 , 1.0)
#rotate = cv.warpAffine(image2,m,(w,h))
inp = input('user enter the rotation amount : ')
inp2 = input('rotate clockwise: ')
d = ['y','yes','Y','YES']
if inp2 in d:
    rotate = imutils.rotate(image2,-1*int(inp))    
else:
    rotate = imutils.rotate(image2,int(inp))
cv.imshow('rotation',rotate)
cv.waitKey(0)


#blurring
image = cv.imread('s6.jpeg')
blurred = cv.GaussianBlur(image ,(5,5),0)
cv.imshow('blurred',blurred)
cv.waitKey(0)

#learning argparse and edge detection
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True , help="path to image to find edges")
args = vars(ap.parse_args())
image3 = cv.imread(args["image"])
cv.imshow('used argparse',image3)
cv.waitKey(0)
gray = cv.cvtColor(image3,cv.COLOR_BGR2GRAY)
grayed = cv.Canny(gray,30,150)
cv.imshow('grayscale edged',grayed)
cv.waitKey(0)

#thresholding
thresh = cv.threshold(grayed,255,255,cv.THRESH_BINARY_INV)[1]
cv.imshow('thresh',thresh)
cv.waitKey(0)
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image3.copy()
for c in cnts:
    cv.drawContours(output,[c],-1,(240,0,159),3)
    cv.imshow('contours',output)
    cv.waitKey(0)'''


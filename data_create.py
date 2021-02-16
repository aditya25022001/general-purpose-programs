import cv2 as cv
import glob
import argparse
face_cascade = 'haarcascade_frontalface_alt.xml'
face_cascade_name = face_cascade
face_cascade = cv.CascadeClassifier()
face_cascade.load(face_cascade_name)
ap = argparse.ArgumentParser(description='path to data file')
ap.add_argument('--input' , help='file path')
args = ap.parse_args()
destination_file = input('enter destination file/folder path : ')
path = glob.glob('{}\*.jpg'.format(args.input))
i=1
def faceclass(resize):
    faces = face_cascade.detectMultiScale(resize)
    for x,y,w,h in faces:
        global i
        i+=1
        faceROI = resize[y:y+h , x:x+w]
        resized = cv.resize(faceROI , (100,100))
        cv.imwrite('{}{}.jpg'.format(destination_file,i),resized)
for image in path:
    image2 = cv.imread(image , cv.IMREAD_GRAYSCALE)
    resize = cv.resize(image2 , (200,200))
    faceclass(resize)   

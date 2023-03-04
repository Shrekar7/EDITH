import cv2
import numpy as np
from PIL import Image
import os
path = 'C://Users//shrekar reddy//Desktop//edith//samples'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("C:\\Users\\shrekar reddy\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")


def Image_And_Lables(path):

    imagePaths = [os.path.join(path,f)for f in os.listdir(path)]
    faceSamples =[]
    ids = []

    for imagePath in imagePaths:

        gray_img = Image.open(imagePath).convert('L')
        img_arr = m=np.array(gray_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)
        
        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print("Training faces.It will take a few seconds. wait.....")

faces,ids = Image_And_Lables(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

print("model trained, now we can recognize your face.")
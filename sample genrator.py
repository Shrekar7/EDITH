import cv2

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)


detector = cv2.CascadeClassifier('C:\\Users\\shrekar reddy\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

face_id = input("enter the numeric user id here : ")

print("Talking samples, look at the camera............")
count = 0

while True:
    ret, img =cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (500,0,0), 2)
        count += 1


        cv2.imwrite("samples/face." + str(face_id)+ '.'+ str(count)+ ".jpg", converted_image[y:y+h,x:x+w])

        cv2.imshow('image', img)
    
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 10:
        break

print("samples taken now closing the program.....")
cam.release()
cv2.destroyAllWindows























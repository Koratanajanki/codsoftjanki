import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\sukru\Desktop\codsoft\haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\sukru\Desktop\codsoft\codsoftai-1\codsoftjanki-1\WhatsApp Image 2023-09-05 at 19.05.59.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4) 

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.imshow('img',img)
cv2.waitKey()
import cv2
from PIL import Image
clasificador='C:\programming\IA_detecciondecara\haarcascade_frontalface_default.xml'
imagepath='C:\programming\IA_detecciondecara\hq720.jpg'
image=cv2.imread(imagepath)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier(clasificador)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2,minSize=(30,30))
for(x,y,w,h) in faces:
    face=image[y:y+h,x:x+w] 
    blurred_face=cv2.resize(cv2.resize(face,(w//10,h//10)),(w,h))
    image[y:y+h,x:x+w]=blurred_face
#mostrar la imagen de caras detectadas
cv2.imshow('programa para detectar las caras',image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

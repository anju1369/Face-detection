#Face detection
#Haar cascade face detection algorithm
import cv2
alg="haarcascade_frontalface_default.xml"#accessed the modal file
haar_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)#Initializing camera
while True:
    _,img=cam.read()#read the frame from the camera
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#Converting color into gray scale image
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)#get coordinates of face
    for(x,y,w,h) in face:#segregating x,y,w,h.
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()

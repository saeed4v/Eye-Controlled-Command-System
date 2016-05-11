import numpy as np
import cv2
import collections
import time
import picamera
import os




# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
eye0_cascade = cv2.CascadeClassifier('/home/pi/Desktop/pi/Newfolder/haarcascade_eye.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

font=cv2.FONT_HERSHEY_SIMPLEX
cap = picamera.PiCamera()
cap.resolution = (640,480)
cap.framerate = 50

#cap = cv2.VideoCapture(0)
tym=0
ch=0
k=0
d = collections.deque([0,1,2,3,4])

def execute(h,img):
    if h==0:
        cv2.putText(img,'FOOD EXECUTED',(200,200),font,1,(0,255,0),2)
        os.system('mpg321 /home/pi/Desktop/pi/Newfolder/foodmp3.mp3')
        time.sleep(1)

    elif h==1:
            cv2.putText(img,'WATER COMMAND EXECUTED',(200,200),font,1,(0,255,0),2)
            time.sleep(3)
            os.system('mpg321 /home/pi/Desktop/pi/Newfolder/watermp3.mp3')

    elif h==2:
            cv2.putText(img,'TOILET COMMAND EXECUTED',(200,200),font,1,(0,255,0),2)
            time.sleep(1)
            os.system('mpg321 /home/pi/Desktop/pi/Newfolder/toiletmp3.mp3')
            
    elif h==3:
            cv2.putText(img,'DOCTOR COMMAND EXECUTED',(200,200),font,1,(0,255,0),2)
            time.sleep(1)
            os.system('mpg321 /home/pi/Desktop/pi/Newfolder/doctmp3.mp3')

    else:
            cv2.putText(img,'NO SELECTION',(150,200),font,1,(0,255,0),2)
            time.sleep(1)


def display(y,img):
    if y == 0:
        
        
        cv2.putText(img,'FOOD',(10,50),font,1,(255,0,0),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        #cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)

            
    elif y == 1:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,0,0),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        #cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)
        

        

    elif y == 2:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,0,0),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        #cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)


    elif y == 3:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,0,0),2)
        #cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)


    else:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        #cv2.putText(img,'No selection',(100,200),font,1,(255,255,255),1)




while 1:
    
    #ret, img = cap.read()
    cap.capture('image.bmp')
    img = cv2.imread('image.bmp')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye0 = eye0_cascade.detectMultiScale(gray, 1.3, 5)
    z=d[0]
    if ch<5:
        
        display(z,img)
        ch=ch+1
    else:
        d.rotate(1)
        ch=0
    
    
    
    
   
       


    flag=0

    for (x,y,w,h) in eye0:
    
   
        if w>40 and w<70:
            
            flag=1
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        #print roi_color
        
    if flag == 1:
        print 'Eye Open'
        tym=0   
    else:
        print 'Eye Closed'
        tym=tym+1
        

    if tym >2 :
        print 'Next'

        h=d[0]
        d.rotate(1)
        execute(h,img)
        
        tym=0

    cv2.namedWindow('img',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('img',cv2.WND_PROP_FULLSCREEN,cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow('img',img)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2
import collections
import picamera




# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
eye0_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

font=cv2.FONT_HERSHEY_SIMPLEX
cap = picamera.PiCamera()
#cap.start_preview()
cap.resolution = (340,240)
cap.framerate=50



#cap = cv2.VideoCapture(0)
tym=0
d = collections.deque([0,1,2,3,4])

def check():
    cap.capture('image.bmp')
    img=cv2.imread('image.bmp')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye0 = eye0_cascade.detectMultiScale(gray, 1.3, 5)
    
   
       


    flag=0

    for (x,y,w,h) in eye0:
   
        
        flag=1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
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
        
        d.rotate(1)
        tym=0

    
    

def display(y):
    if y == 0:
        
        check=0
        cv2.putText(img,'FOOD',(10,50),font,1,(255,0,0),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)
##        while check<10:
##            check=check+1
##            cap.capture('image.bmp')
##            img=cv2.imread('image.bmp')
##            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##            eye0 = eye0_cascade.detectMultiScale(gray, 1.3, 5)
##            flag=0
##            for (x,y,w,h) in eye0:
##                
##   
##        
##                flag=1
##                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
##                roi_gray = gray[y:y+h, x:x+w]
##                roi_color = img[y:y+h, x:x+w]
##                #print roi_color
##
##            if flag == 1:
##                print 'Eye Open'
##                tym=0   
##            else:
##                print 'Eye Closed'
##                tym=tym+1
##        
##
##            if tym >2 :
##                print 'Next'
##        
##                
##                tym=0
##            
            
            
    elif y == 1:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,0,0),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)
        

        

    elif y == 2:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,0,0),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)


    elif y == 3:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,0,0),2)
        cv2.putText(img,'Close eyes to confirm',(100,200),font,1,(255,255,255),1)


    else:
        cv2.putText(img,'FOOD',(10,50),font,1,(255,255,255),2)
        cv2.putText(img,'WATER',(10,400),font,1,(255,255,255),2)
        cv2.putText(img,'TOILET',(500,40),font,1,(255,255,255),2)
        cv2.putText(img,'DOCTOR',(450,400),font,1,(255,255,255),2)
        cv2.putText(img,'No selection',(100,200),font,1,(255,255,255),1)




while 1:
    
##    cap.capture('image.bmp')
##    img=cv2.imread('image.bmp')
##    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    eye0 = eye0_cascade.detectMultiScale(gray, 1.3, 5)
##    
##   
##       
##
##
##    flag=0
##
##    for (x,y,w,h) in eye0:
##   
##        
##        flag=1
##        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
##        roi_gray = gray[y:y+h, x:x+w]
##        roi_color = img[y:y+h, x:x+w]
##        #print roi_color
##
##    if flag == 1:
##        print 'Eye Open'
##        tym=0   
##    else:
##        print 'Eye Closed'
##        tym=tym+1
##        
##
##    if tym >2 :
##        print 'Next'
##        
##        d.rotate(1)
##        tym=0
##
##    z=d[0]      
##    display(z)
    check()
    cv2.imshow('img',img)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()

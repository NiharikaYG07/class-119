import cv2

vid=cv2.VideoCapture("footvolleyball.mp4")

tracker=cv2.TrackerCSRT_create()
check,img=vid.read()

bbox=cv2.selectROI("ball",img,False)
tracker.init(img,bbox)
print(bbox)

def drawBox(frame,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3,1)
    cv2.putText(frame,"TRACKING",(75,90),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

while True:
    ret,frame=vid.read()

    success,bbox=tracker.update(frame)

    if success:
        drawBox(frame,bbox)
    else:
        cv2.putText(frame,'LOST',(75,90),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    cv2.imshow("video",frame)
    if cv2.waitKey(1)==32:
        break

vid.release()
cv2.destroyAllWindows()

import cv2

vid = cv2.VideoCapture(0)
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
l=4
t=5

while True:
    check,frame = vid.read()

    show = face.detectMultiScale(frame,
    scaleFactor=1.2,
    minNeighbors=5)

    for x,y,w,z in show:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+z),(0,0,255),4)


        cv2.imshow("vids",frame)

        key=cv2.waitKey(100)

        if key == ord('q'):
            l=t
            break
        
        if(l==t):
            vid.release()
            cv2.destroyAllWindows()


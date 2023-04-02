import cv2,time,pandas
from datetime import datetime

frame1 = None
stat_l=[None,None]
time =[]
df=pandas.DataFrame(columns=["Start","End"])

vid = cv2.VideoCapture(0)
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    check,frame = vid.read()
    status = 0

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if frame1 is None:
        frame1 = gray
        continue

    del_frame=cv2.absdiff(frame1,gray)

    thresh = cv2.threshold(del_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh,None, iterations=2)

    (cnts,_) = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 20000:
            continue
        status = 1
        (x,y,w,z)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+z),(0,255,0),3)
    stat_l.append(status)

    stat_l=stat_l[-2:]

    if stat_l[-1]==1 and stat_l[-2]==0:
        time.append(datetime.now())
    if stat_l[-1]==0 and stat_l[-2]==1:
        time.append(datetime.now())

    cv2.imshow("vids",frame)

    show = face.detectMultiScale(frame,
    scaleFactor=1.2,
    minNeighbors=5)

    for x,y,w,z in show:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+z),(0,0,255),4)

        cv2.imshow("vids",frame)

        key=cv2.waitKey(1)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            time.append(datetime.now())
        break

for i in range(0,len(time),2):
    df=df.append({"Start":time[i],"End":time[i+1]},ignore_index=True)

df.to_csv("Time.csv")
df_new = pandas.read_csv('Time.csv')
 
plotx = pandas.ExcelWriter('Plotx.xlsx')
df_new.to_excel(plotx, index=False)
plotx.save()

vid.release()
cv2.destroyAllWindows()

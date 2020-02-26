import cv2 as cv 
import numpy as np 

webcam = cv.VideoCapture('/dev/video0')
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
classificador = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    ret, frame = webcam.read()
    #frame = frame[350:600, 300:680]
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    corpo = classificador.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in corpo:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    cv.imshow('Corpos', frame)

    if cv.waitKey(27) & 0xff == ord('q'):
        break
    


webcam.release()
cv.destroyAllWindows()
import cv2 as cv

web = cv.VideoCapture('/dev/video2')
web.set(cv.CAP_PROP_FRAME_WIDTH, 1476)
web.set(cv.CAP_PROP_FRAME_HEIGHT, 830)

while True: 
    _, frame = web.read()
    frame = frame[374:800, 600:1050]
    cv.imshow('y', frame)

    if cv.waitKey(27) & 0xff == ord('q'):
        break
    
cv.destroyAllWindows()
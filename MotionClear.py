import cv2 as cv
import numpy as np



class Changes():
    def __init__(self, web_number): 
        self.biggest_rect = list()
        self.biggest_area = 0
        self.webcam = cv.VideoCapture(web_number)
        self.webcam.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
        self.webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
        

    def get_changes(self):
        self.biggest_rect = list()
        self.biggest_area = 0
        ret, self.frame1 = self.webcam.read()
        ret, self.frame2 = self.webcam.read()   
        #self.frame1 = self.frame1[350:600, 300:680] 
        #self.frame2 = self.frame2[350:600, 300:680]

        self.difference = cv.absdiff(self.frame1, self.frame2)
        self.blured = cv.GaussianBlur(cv.cvtColor(self.difference,cv.COLOR_BGR2GRAY), (5,5) ,0)
        ret, self.binary = cv.threshold(self.blured, 20, 255, cv.THRESH_BINARY)
        self.dilated = cv.dilate(self.binary, np.ones((7,7)), np.uint8, iterations=7)
        self.contours, self.hierarchy = cv.findContours(self.dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(self.frame1, self.contours, -1, (0,255,0), 3)
       # for contour in self.contours: 
        #    x, y, w, h = cv.boundingRect(contour)
         #   cv.rectangle(self.frame1, (x, x+w), (y, y+h), (255, 0, 0), 4)
        
                

movimento = Changes(web_number =  '/dev/video0')

while True: 

    movimento.get_changes()
    # img = movimento.frame1[int(x_mid-200):int(x_mid+200), int(y_mid-200):int(y_mid+200)]
    cv.imshow('t', movimento.frame1) 
   
    if cv.waitKey(27) & 0xff == ord('q'):
        break
    

cv.destroyAllWindows()
movimento.webcam.release()

    
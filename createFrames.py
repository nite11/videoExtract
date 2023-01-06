# import the necessary packages
import cv2
import math 
import os

count = 0
cap = cv2.VideoCapture("video\Sumida.mp4")   # capturing the video from the given path
frameRate = cap.get(5) # propID 5 : FPS Frame rate.
print(frameRate)
#cap.open()
while(cap.isOpened()):
    frameId = cap.get(1) # propId=1: index of the frame to be captured next
    #print(frameId)
    ret, frame = cap.read() # return True if frame is read correctly
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="frame%d.jpg" %count;count+=1
        cv2.imwrite(os.path.join("frames", filename), frame)
#cap.release()
#print(cap.isOpened())
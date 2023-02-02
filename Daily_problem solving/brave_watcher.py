import cv2
import time
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time
from datetime import datetime
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
start_time = time.time()
counter = 0
clip = []
while True:
    if gw.getWindowsWithTitle('Brave'):
            
            
        clip.append(pyautogui.screenshot())
            
    if time.time() - start_time > 60: # stop recording after 5 minutes
            break

images = start_recording()
for image in images:
    _,im = cap.read()
    
    out.write(im)

# Release the video writer and close the output video file
out.release()

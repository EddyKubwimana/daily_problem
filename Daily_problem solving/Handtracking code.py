
import numpy
import cv2
import mediapipe as mp
import cvzone
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(3,1288)
cap.set(4,786)
detector=HandDetector(detectionCon=0.8, maxHands=2)
while True:
    success,img=cap.read()
    Hands,img=detector.findHands(img)
    if Hands:
        Hand1=Hands[0]
        LmList1=Hand1['lmList']
        bbox1=Hand1['bbox']
        centerpoint1=Hand1['center']
        HandType1=Hand1['type']
       
        
        
        if len(Hands)==2:
            Hand2=Hands[1]
            LmList2=Hand2['lmList']
            bbox2=Hand2['bbox']
            centerpoint2=Hand2['center']
            HandType2=Hand2['type']
            print(HandType1,HandType2)
            fingers1=detector.fingersUp(Hand1)
            fingers2=detector.fingersUp(Hand2)
            print(fingers1)
            print(fingers2)
            lenght,info,img=detector.findDistance(centerpoint1, centerpoint2, img)
    cv2.imshow('image',img)
    cv2.waitKey(1)

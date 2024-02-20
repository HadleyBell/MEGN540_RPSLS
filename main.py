import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)   

detector = HandDetector(maxHands = 1) # o.5 confidence

while True:
    sucess, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    
# img = cv2.imread()
# sucess, img = cap.read()
# cv2.imshow("Image", img)
# cv2.waitKey(1)



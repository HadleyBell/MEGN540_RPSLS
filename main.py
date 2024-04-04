import cv2
import mediapipe as mp
import time
# import cvzone
# from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)   

# detector = HandDetector(maxHands = 1) # o.5 confidence
mpHands = mp.solutions.hands
hands = mpHands.Hands() 
mpDraw = mp.solutions.drawing_utils

# Frame rate
pTime = 0
cTime = 0

while True:
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handsLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handsLms.landmark):
                # print(id, lm)
                h, w, c, = img.shape
                cx, cy = int(lm.x*w), int(lm.y+h)
                print(id, cx, cy)
                
            mpDraw.draw_landmarks(img, handsLms, mpHands.HAND_CONNECTIONS)
            
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime       

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3) #frame rate
    cv2.imshow("Image1", img)
    cv2.waitKey(1)

    # cap.release()
    # cv2.destroyAllWindows()
    # cv2.destroyWindow("Image") 

    
# img = cv2.imread()
# sucess, img = cap.read()
# cv2.imshow("Image", img)
# cv2.waitKey(1)



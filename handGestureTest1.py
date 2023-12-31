import cv2, time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands #used for detecting the hand (it is a class)
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils #for drawing the points on the detected hand
#Calculating frame rate
pTime = 0 
cTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks)

    #handlm: for marking the points on hand
    #mpHands.HAND_CONNECTIONS: to draw the connection btw the detected points
    #h , w, c: height, width, channel.
    if result.multi_hand_landmarks:
        for handLm in result.multi_hand_landmarks:
            for id, lnd in enumerate(handLm):
                h, w, c = img.shape     #get in terms of ratio
                cx, cy = int(lnd.x*w), int(lnd.y*h)
                # print(id, cx, cy)
                #now here using id we can extract and track movements of hand\fingers to performs some task
                #example: tracking the thumb top part (index)
                if id==4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255),  cv2.FILLED )
                
            mpDraw.draw_landmarks(img, handLm, mpHands.HAND_CONNECTIONS) 

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
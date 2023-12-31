import cv2, time
import mediapipe as mp

class HandGesture():
    addDelay = cv2.waitKey(1)
    def __init__(self, mode=False, maxHands=2, detectionConfi=0.5, trackConfi=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfi = detectionConfi
        self.trackConfi = trackConfi
        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils    #for drawing the points on the detected hand
    
    def start(self, webcamAddress=0):
        cap = cv2.VideoCapture(webcamAddress)
        return cap

    def findHands(self, img, draw_Points=True, draw_Connections=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(self.imgRGB)
        if self.result.multi_hand_landmarks:
            for self.handLm in self.result.multi_hand_landmarks:
                if (draw_Points and draw_Connections):
                    self.mpDraw.draw_landmarks(img, self.handLm, self.mpHands.HAND_CONNECTIONS) 
                elif draw_Points:
                    self.mpDraw.draw_landmarks(img, self.handLm)
        return img
    
    def getCooridinates(self, img, handNo=0, traceALl=True, indexTrackNo=None, draw=False):
        coDict = {} 
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[handNo]
            for id, lnd in enumerate(hand.landmark):
                if not traceALl:
                    if indexTrackNo == id:
                        h, w, c = img.shape     #get in terms of ratio
                        cx, cy = int(lnd.x*w), int(lnd.y*h)
                        coDict[id] = [cx, cy]
                        if draw:
                            cv2.circle(img, (cx, cy), 10, (255, 0, 255),  cv2.FILLED)
                    else: continue
                else: 
                    h, w, c = img.shape     #get in terms of ratio
                    cx, cy = int(lnd.x*w), int(lnd.y*h)
                    coDict[id] = [cx, cy]
        return coDict
    
    def display(self, img, windowName):
        cv2.imshow(windowName, img)
    
    def insertFPS(self, img, fps, x, y, RGB):
        cv2.putText(img, str(int(fps)), (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, RGB, 3)
    
    
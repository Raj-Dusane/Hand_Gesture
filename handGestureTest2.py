import time, handGestureModule
def main():
    # Calculating frame rate
    prevTime = 0 
    currentTime = 0
    hand1 = handGestureModule.HandGesture()
    while True:
        start = hand1.start(0)     #IP Address of the webcam can also be given
        success, img = start.read()
        reImg=hand1.findHands(img)
        
        currentTime = time.time()
        fps = 1/(currentTime-prevTime)
        prevTime = currentTime
        
        coordinates = hand1.getCooridinates(reImg, 0, False, 14, True)
        if len(coordinates) != 0:
            for key, values in coordinates.items():
                print(f'{key}', ': ', f'{values}' )
        
        hand1.insertFPS(reImg, fps, 50, 70, (255, 0, 255))
        hand1.display(reImg, "hand1")
        hand1.addDelay

if __name__ == "__main__":
    main()
import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller


cap = cv2.VideoCapture(0)
cap.set(3, 320) 
cap.set(4, 320)  

detector = HandDetector(detectionCon=0.7, maxHands=1)
keyboard = Controller()

while True:
    _, img = cap.read()

    hands, img = detector.findHands(img)

    if hands:
        
        fingers = detector.fingersUp(hands[0])

        if fingers == [0, 0, 0, 0, 0]:  
            keyboard.press(Key.left)
            keyboard.release(Key.right)
        elif fingers == [1, 1, 1, 1, 1]: 
            keyboard.press(Key.right)
            keyboard.release(Key.left)
        else:
            keyboard.release(Key.left)
            keyboard.release(Key.right)
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)

    cv2.imshow("Game Control", img)

    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

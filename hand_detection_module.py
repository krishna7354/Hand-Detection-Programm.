import cv2
import mediapipe as mp
import time

class handDetection():
    def __init__(self, mode=False, maxHands=2, model=1, minDetection=0.5, minTracking=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model = model
        self.minDetection = minDetection
        self.minTracking = minTracking

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode, self.maxHands, self.model, self.minDetection, self.minTracking)
        self.draw = mp.solutions.drawing_utils

    def findHand(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for find in self.result.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(frame, find, self.mphands.HAND_CONNECTIONS)
        return frame

    def findPosition(self, frame, draw=True):
        mylist = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks
            for hand in myhand:
                handNo=[]
                for id, lm in enumerate(hand.landmark):
                    if id==0 or id==4 or id==8 or id==12 or id==16 or id==20:
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        handNo.append([id, cx, cy])
                        if draw:
                            cv2.circle(frame, (cx, cy), 3, (0,255,0), 3, cv2.FILLED)
                mylist.append(handNo)
        return mylist

def main():
    video = cv2.VideoCapture(0)

    cTime = 0
    pTime = 0
    detected = handDetection()
    while True:
        r, frame = video.read()
        frame = cv2.resize(frame, (900,700))
        frame = detected.findHand(frame)
        mylist = detected.findPosition(frame)
        totHand = len(mylist)
        cv2.putText(frame, str(f'Hand: {totHand}'), (5, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2, 3)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime

        cv2.putText(frame, str(f'fps: {int(fps)}'), (5,30), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2, 3)
        cv2.imshow('show', frame)

        if cv2.waitKey(1) & 0xFF == ord('p'):
            break
if __name__ == '__main__':
    main()
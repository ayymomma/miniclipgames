import time

import cv2
import pyautogui
from PyQt5 import QtGui
from PyQt5.QtCore import QObject


class VideoManager:
    runFlag = True

    def __init__(self):
        self.videoStream = None
        self.runFlag = True

    def startStream(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.videoStream = cv2.VideoCapture(0)
        self.videoStream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.videoStream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # last mouse position
        last_x = 0
        last_y = 0
        # move mouse to the center of screen
        pyautogui.moveTo(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)

        while self.runFlag:
            # read frame
            ret, cvImg = self.videoStream.read()
            if ret:
                # mirror image
                cvImg = cv2.flip(cvImg, 1)


                # detect faces
                gray = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
                faceRects = face_cascade.detectMultiScale(gray, 1.3, 5)

                # draw rectangle
                for (x, y, w, h) in faceRects:
                    cv2.rectangle(cvImg, (x + int(w / 2), y + int(h / 2)), (x + int(w / 2), y + int(h / 2)), (0, 255, 0), 3)

                    # get center of face
                    center_x = x + int(w / 2)
                    center_y = y + int(h / 2)

                    # scale the center of face to the center of screen
                    center_x = int(center_x * (pyautogui.size().width / cvImg.shape[1]))
                    center_y = int(center_y * (pyautogui.size().height / cvImg.shape[0]))

                    if abs(center_x - last_x) > 10 or abs(center_y - last_y) > 10:
                        # move mouse to center of face
                        pyautogui.moveTo(center_x, center_y)
                        # save last mouse position
                        last_x = center_x
                        last_y = center_y

                cv2.imshow(" ", cvImg)

            # break on ESC
            if cv2.waitKey(1) == 27:
                break
        self.videoStream.release()
        cv2.destroyAllWindows()


videoManager = VideoManager()
videoManager.startStream()


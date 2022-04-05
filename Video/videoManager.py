import time

import cv2
import pyautogui
from PyQt5 import QtGui
from PyQt5.QtCore import QObject


class VideoManager:
    runFlag = True

    def __init__(self):
        self.runFlag = True

    def startStream(self):
        # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        videoStream = cv2.VideoCapture(0)
        while self.runFlag:
            # preluare imagine
            ret, cvImg = videoStream.read()
            if ret:
                cv2.imshow("", cvImg)
                # cvImg = cv2.flip(cvImg, 1)
                # gray = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
                # eyeRects = eye_cascade.detectMultiScale(gray, 1.3, 5)
                # for (x, y, w, h) in eyeRects:
                #     cv2.rectangle(cvImg, (x + int(w / 2), y + int(h / 2)), (x + int(w / 2), y +
                #                                                             int(h / 2)), (0, 255, 0), 3)
                #
                #     QtGui.QCursor.setPos(x, y)
                #     if True:
                #         pyautogui.leftClick()


videoManager = VideoManager()
videoManager.startStream()
cv2.destroyAllWindows()

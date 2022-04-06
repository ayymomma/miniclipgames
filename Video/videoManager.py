import os
import cv2
import pyautogui
from PyQt5.QtCore import QObject


class VideoManager(QObject):
    runFlag = True

    def __init__(self):
        super().__init__()
        self.videoStream = None
        self.runFlag = True

    def startStream(self):
        face_cascade = cv2.CascadeClassifier(os.getcwd() + "\\resources\\video\\haarcascade_frontalface_default.xml")
        self.videoStream = cv2.VideoCapture(0)
        self.videoStream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.videoStream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # list of last 60 mouse positions
        mouse_positions = []
        # last mouse position
        last_x = 0
        last_y = 0
        # move mouse to the center of screen
        pyautogui.moveTo(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)

        while self.runFlag:
            print("test")
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
                    cv2.rectangle(cvImg, (x + int(w / 2), y + int(h / 2)), (x + int(w / 2), y + int(h / 2)),
                                  (0, 255, 0), 3)

                    # get center of face
                    center_x = x + int(w / 2)
                    center_y = y + int(h / 2)

                    # scale the center of face to the center of screen
                    center_x = int(center_x * (pyautogui.size().width / cvImg.shape[1]))
                    center_y = int(center_y * (pyautogui.size().height / cvImg.shape[0]))

                    if abs(center_x - last_x) > 20 or abs(center_y - last_y) > 20:
                        # move wx mouse to center of face
                        pyautogui.moveTo(pyautogui.size()[0] / 2 + (center_x - pyautogui.size()[0] / 2) * 4,
                                         pyautogui.size()[1] / 2 + (center_y - pyautogui.size()[1] / 2) * 4)
                        # save last mouse position
                        last_x = center_x
                        last_y = center_y
                # add last position to mouse_positions
                if len(mouse_positions) == 60:
                    avgX = 0
                    avgY = 0
                    for x, y in mouse_positions:
                        avgX += x
                        avgY += y
                    avgX /= 60
                    avgY /= 60

                    counter = 0
                    flag = True
                    for x, y in mouse_positions:
                        if abs(avgX - x) > 20 or abs(avgY - y) > 20:
                            counter += 1
                        if counter > 30:
                            flag = False
                            break
                    if flag:
                        # # move mouse on avgX, avgY
                        # pyautogui.moveTo(avgX, avgY)
                        # # click mouse
                        # pyautogui.click()
                        pyautogui.click()
                    mouse_positions = []

                mouse_positions.append((last_x, last_y))

                cv2.imshow(" ", cvImg)

            # break on ESC
            if cv2.waitKey(1) == 27:
                break
        self.videoStream.release()
        cv2.destroyAllWindows()



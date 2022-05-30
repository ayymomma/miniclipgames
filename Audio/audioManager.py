import os

from playsound import playsound
import threading
import multiprocessing


class AudioManager(object):

    def __init__(self):
        self.mouseClickSound = os.getcwd() + "\\resources\\audio\\mouse_click.wav"
        self.ticTacToeSound = os.getcwd() + "\\resources\\audio\\ticTacToeSound.wav"
        self.process = None

    def playSoundButtonClick(self):
        threading.Thread(target=playsound, args=(self.mouseClickSound,), daemon=True).start()

    def ticTacToePlaySound(self):
        # threading.Thread(target=playsound, args=(self.ticTacToeSound,), daemon=True).start()
        self.process = multiprocessing.Process(target=playsound, args=(self.ticTacToeSound,))
        self.process.start()

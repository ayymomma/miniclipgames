import os

from playsound import playsound
import threading


class AudioManager:
    def playSoundButtonClick(self):
        soundName = os.getcwd() + "\\resources\\audio\\mouse_click.wav"
        threading.Thread(target=playsound, args=(soundName,), daemon=True).start()

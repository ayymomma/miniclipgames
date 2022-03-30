import threading

import speech_recognition as sr
import pyttsx3
from PyQt5.QtCore import QObject, pyqtSignal


class VoiceManager(QObject):
    cell_position_signal = pyqtSignal(int)
    reset_signal = pyqtSignal()
    indexList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    quitFlag = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VoiceManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(VoiceManager, self).__init__()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()

    def speechToText(self):
        print("ascult")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.energy_threshold = 1000
            audio = self.recognizer.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            response["transcription"] = self.recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["success"] = False
            response["error"] = "Unable to recognize speech"
        print("am terminat de ascultat")
        return response

    def textToSpeech(self, myText):
        self.engine.say(myText)
        self.engine.runAndWait()

    def start(self):
        action = 'waiting'
        print(action)
        self.quitFlag = True
        while self.quitFlag:
            text = self.speechToText()
            print("----new command----")
            if not text["success"] and text["error"] == "API unavailable":
                print("ERROR: {}\nclose program".format(text["error"]))
                break
            while not text["success"]:
                if not self.quitFlag:
                    return
                print("I didn't catch that. What did you say?\n")
                text = self.speechToText()
            if text["transcription"].lower() == "exit":
                self.quitFlag = False

            print(text["transcription"].lower())

            if action == 'waiting':
                if text["transcription"].lower() == 'start':
                    action = 'start'

            if action == 'start':
                print(action)
                self.textToSpeech(text["transcription"].lower())
                print(text["transcription"].lower())
                if text["transcription"].lower() in self.indexList:
                    self.cell_position_signal.emit(self.indexList.index(text["transcription"].lower()))
                if text["transcription"].lower() == 'reset':
                    self.reset_signal.emit()
                if "stop" in text["transcription"].lower():
                    action = "waiting"

import speech_recognition as sr
from gtts import gTTS

import pathlib
import os

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = os.path.join(pathlib.Path(__file__).parent.resolve(), "audio", "voice.mp3")
    tts.save(filename)
    os.system('start '+filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def get_audio_from_source(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        said = ""

        try:
            said = r.recognize_google(audio_data)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said
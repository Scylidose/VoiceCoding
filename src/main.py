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

    return said

def write_code(text):
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), "code", "code.py")
    f = open(path, "w+")
    f.write(text)
    f.close()

def execute_code():
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), "code", "code.py")
    os.system('python ' + path)

write_code("for i in range(2): print(\"foo\"); print(\"bar\")")
execute_code()
# text = get_audio()

text = "hi"

if "hello" in text:
    speak("Hello world!")

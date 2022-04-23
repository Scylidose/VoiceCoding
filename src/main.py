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

import subprocess 

def execute_code():
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), "code", "code.py")
    os.system('python ' + path)
    output = subprocess.check_output('python ' + path,  shell=True)
    
    return output.decode("utf-8") 

def translate_to_code(audio):
    code_to_write = ""
    statements = audio.split()
    
    for i in range(0, statements):
        if statements[i] == "for":
            code_to_write += "for"

        if statements[i] == "if":
            code_to_write += "if"

    return code_to_write

write_code("for i in range(2): print(\"foo\"); print(\"bar\")")

text = get_audio()

if text == "show result":
    speak(execute_code())
else: 
    translate_to_code(text)

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
    index = 0

    if statements[0] == "add":
        if statements[1] == "function":
            code_to_write += statements[2] + "("
            for param in range(3, len(statements)):
                param_type = "string"
                param_value = ""
                if statements[param] == "type":
                    param_type = statements[param-1]
                if statements[param] == "equal":
                    
                    for value in range(param+1, len(statements)):
                        param_value += statements[value] + " "
                    if param_type == "string":
                        code_to_write += "\""+param_value+"\""
            code_to_write += ")"
    return code_to_write

# write_code("for i in range(2): print(\"foo\"); print(\"bar\")")

# text = get_audio()
text = get_audio_from_source("src/audio/first_use_case.wav")
text = "add function print with parameters string type equal hello world"
print("TRANSLATE TO CODE : " + translate_to_code(text))
write_code(translate_to_code(text))
print("RESULTED CODE : " + execute_code())
# if text == "show result":
#     speak(execute_code())
# else: 
#     print(translate_to_code(text))

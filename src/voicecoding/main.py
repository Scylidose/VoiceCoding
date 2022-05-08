from code_executor import code_executor
from speech_recognizer import speech_recognizer

def main():

    # text = get_audio()
    text = speech_recognizer.get_audio_from_source("src/voicecoding/audio/first_use_case.wav")
    text = "add function print with parameters string type equal hello world"
    print("TRANSLATE TO CODE : " + code_executor.translate_to_code(text))
    code_executor.write_code(code_executor.translate_to_code(text))
    print("RESULTED CODE : " + code_executor.execute_code())
    # if text == "show result":
    #     speak(execute_code())
    # else: 
    #     print(translate_to_code(text))

if __name__ == "__main__":
    main()

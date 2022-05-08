import pathlib
import os

def write_code(text):
    path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "code", "code.py")
    f = open(path, "w+")
    f.write(text)
    f.close()

import subprocess 

def execute_code():
    path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "code", "code.py")
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
                        param_value += statements[value]
                        if value != len(statements)-1:
                            param_value += " "
                    if param_type == "string":
                        code_to_write += "\""+param_value+"\""
            code_to_write += ")"
    return code_to_write

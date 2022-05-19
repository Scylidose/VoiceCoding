import unittest
import pytest

from voicecoding.code_executor import code_executor

class TestCodeExecutor(unittest.TestCase):
    def test_write_code(self):
        text = "add function print with parameters string type equal hello world"

        code_executor.write_code(code_executor.translate_to_code(text))

        result = open("src/voicecoding/code/code.py", "r").readline()
        expected_result = 'print("hello world")'

        assert result == expected_result
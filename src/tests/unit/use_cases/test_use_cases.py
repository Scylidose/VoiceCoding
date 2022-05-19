import unittest
import pytest

from voicecoding.code_executor import code_executor
from voicecoding.speech_recognizer import speech_recognizer

class TestUseCases(unittest.TestCase):
    def test_first_use_case(self):
        # text = speech_recognizer.get_audio_from_source("src/voicecoding/audio/first_use_case.wav")
        text = "add function print with parameters string type equal hello world"

        code_executor.write_code(code_executor.translate_to_code(text))

        result = code_executor.execute_code().strip()
        expected_result = "hello world"

        assert result == expected_result

    def test_second_use_case(self):
        # text = speech_recognizer.get_audio_from_source("src/voicecoding/audio/second_use_case.wav")
        text = "add variable lorem with string type equal hello add variable ispum with float type equal eight point 9"

        code_executor.write_code(code_executor.translate_to_code(text))

        result = code_executor.execute_code().strip()
        expected_result = "lorem = \"hello\"\nipsum = 8.9"

        assert result == expected_result
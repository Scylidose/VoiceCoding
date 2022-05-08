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
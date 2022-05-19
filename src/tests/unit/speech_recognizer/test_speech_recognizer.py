import unittest
import pytest

from voicecoding.speech_recognizer import speech_recognizer

class TestSpeechRecognizer(unittest.TestCase):
    def test_get_audio_from_source(self):
        result = speech_recognizer.get_audio_from_source("src/voicecoding/audio/first_use_case.wav")
        expected_result = "add function print with parameters string type equal hello world"

        assert result == expected_result
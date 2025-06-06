import pytest
from word_utils import word_frequency

def test_basic_sentence():
    text = "Hello world hello"
    result = word_frequency(text)
    assert result == {"hello": 2, "world": 1}

def test_with_punctuation():
    text = "Python, python. PYTHON!"
    result = word_frequency(text)
    assert result == {"python": 3}

def test_empty_string():
    text = ""
    result = word_frequency(text)
    assert result == {}

def test_mixed_characters():
    text = "Test123 test123! 123test"
    result = word_frequency(text)
    assert result == {"test123": 2, "123test": 1}

def test_exception_on_non_string():
    with pytest.raises(TypeError) as exc_info:
        word_frequency(12345)
    assert "Input must be a string" in str(exc_info.value)

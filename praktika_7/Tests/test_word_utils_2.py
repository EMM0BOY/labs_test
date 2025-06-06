import pytest
from word_utils import word_frequency

@pytest.mark.parametrize("text, expected", [
    ("Hello world hello", {"hello": 2, "world": 1}),
    ("Python, python. PYTHON!", {"python": 3}),
    ("", {}),
    ("Test123 test123! 123test", {"test123": 2, "123test": 1}),
])
def test_word_frequency_cases(text, expected):
    assert word_frequency(text) == expected


def test_word_frequency_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        word_frequency(123)
    assert "Input must be a string" in str(exc_info.value)

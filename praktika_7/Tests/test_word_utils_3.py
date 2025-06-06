import pytest
from word_utils_3 import word_frequency

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
    assert "Входные данные должны быть строкой" in str(exc_info.value)

def test_word_frequency_warns_on_large_input():
    long_text = "слово " * 1001
    with pytest.warns(UserWarning, match="Входной текст содержит более 1000 слов"):
        word_frequency(long_text)
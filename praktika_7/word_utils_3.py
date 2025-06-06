import warnings

def word_frequency(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("Входные данные должны быть строкой")

    words = text.lower().split()

    if len(words) > 1000:
        warnings.warn(
            "Входной текст содержит более 1000 слов. Это может повлиять на производительность.",
            UserWarning
        )

    freq = {}
    for word in words:
        word = ''.join(filter(str.isalnum, word))  # Удаляем знаки препинания
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq
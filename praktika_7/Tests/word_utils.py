def word_frequency(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    words = text.lower().split()
    freq = {}
    for word in words:
        word = ''.join(filter(str.isalnum, word))  # Удаление знаков препинания
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq

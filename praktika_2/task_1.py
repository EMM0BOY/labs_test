def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == "".join(reversed(cleaned_text))


user_input = input("Введите строку для проверки на палиндром: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")

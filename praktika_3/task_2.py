import random


def generate_password():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "@#%_^!)(*?"
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    password = "".join(random.choice(all_chars) for _ in range(12))
    return password


password = generate_password()
print("Сгенерированный пароль:", password)

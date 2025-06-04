import re


def calc(expression):
    try:
        # Заменяем проценты на дробные значения
        expression = re.sub(r"(\d+)%", r"(\1/100)", expression)
        # Проверяем выражение на цифры, операторы и скобки
        if not re.match(r"^[\d+\-*/().%^ ]+$", expression):
            raise ValueError("Недопустимые символы в выражении")
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e}"


print(calc("1 + 9"))
print(calc("2 ** 3"))
print(calc("50% * 100"))
print(calc("10 + 20%"))

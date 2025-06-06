import time
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"\n[LOG] Вызов функции {func.__name__}()")
        print(f"[LOG] Время вызова: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[LOG] Аргументы: args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            
            # Логирование успешного выполнения
            exec_time = time.time() - start_time
            print(f"[LOG] Функция выполнена успешно за {exec_time:.4f} сек")
            print(f"[LOG] Результат: {result}")
            
            return result
            
        except Exception as e:
            exec_time = time.time() - start_time
            print(f"[LOG] Ошибка в функции: {type(e).__name__} - {str(e)}")
            print(f"[LOG] Время выполнения до ошибки: {exec_time:.4f} сек")
            print("[LOG] Рекомендация: проверьте входные параметры")
            return None
            
    return wrapper


@logging_decorator
def f1(x):
    """Вычисление сложной дроби"""
    return (x**2 + 3*x + 2) / (x - 5)


print(f1(6))
import unittest

def f4(numbers):
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    
    avg_even = sum(even) / len(even) if even else 0
    avg_odd = sum(odd) / len(odd) if odd else 0
    
    if avg_even > avg_odd:
        return "Среднее четных больше"
    elif avg_odd > avg_even:
        return "Среднее нечетных больше"
    else:
        return "Средние равны"
# Версия с ошибкой
# def f5(n):
#     result = 1
#     for i in range(n):
#         result *= i
#     return result

# без ошибки
def f5(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

class TestFunctions(unittest.TestCase):
    
    # Тесты для f4()
    def test_f4_even_greater(self):
        self.assertEqual(f4([2, 4, 1, 3]), "Среднее четных больше")
    
    def test_f4_odd_greater(self):
        self.assertEqual(f4([1, 3, 2, 4, 5]), "Среднее нечетных больше")
    
    def test_f4_equal(self):
        self.assertEqual(f4([2, 4, 1, 3, 5, 7]), "Средние равны")
    
    def test_f4_empty(self):
        self.assertEqual(f4([]), "Средние равны")
    
    # Тесты для f5() - с обнаружением ошибки
    def test_f5_factorial_of_5(self):
        self.assertEqual(f5(5), 120)  # Этот тест упадет, так как f5(5) вернет 0
    
    def test_f5_factorial_of_1(self):
        self.assertEqual(f5(1), 1)  # Этот тест упадет, так как f5(1) вернет 0
    
    def test_f5_factorial_of_0(self):
        self.assertEqual(f5(0), 1)  # Этот тест упадет, так как f5(0) вернет 1 (из-за range(0))

if __name__ == '__main__':
    unittest.main()
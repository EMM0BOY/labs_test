import pytest
import random

@pytest.fixture
def random_number():
    return random.randint(1, 100)

def test_random_number_in_range(random_number):
    assert 1 <= random_number <= 100, f"Число {random_number} вне диапазона!"

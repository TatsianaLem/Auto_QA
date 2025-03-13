import pytest
from hw1.simple_math import SimpleMath

@pytest.fixture
def simple_math():
    """Создаем экземпляр класса SimpleMath для тестов."""
    return SimpleMath()

def test_square(simple_math):
    """Тестируем метод square."""
    assert simple_math.square(2) == 4      # 2^2 = 4
    assert simple_math.square(-3) == 9     # (-3)^2 = 9
    assert simple_math.square(0) == 0       # 0^2 = 0
    assert simple_math.square(1.5) == 2.25  # 1.5^2 = 2.25

def test_cube(simple_math):
    """Тестируем метод cube."""
    assert simple_math.cube(2) == 8         # 2^3 = 8
    assert simple_math.cube(-3) == -27      # (-3)^3 = -27
    assert simple_math.cube(0) == 0          # 0^3 = 0
    assert simple_math.cube(1.5) == 3.375    # 1.5^3 = 3.375
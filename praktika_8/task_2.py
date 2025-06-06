from hypothesis import given
import hypothesis.strategies as st

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_rounding_difference(x):
    rounded = round(x)
    diff = abs(x - rounded)
    assert diff <= 0.5, f"Разница {diff} больше 0.5 для числа {x}"
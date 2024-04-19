from math import isclose

from hypothesis import given
from hypothesis.strategies import floats, integers

from python_builtins import abs_


@given(integers() | floats(allow_nan=False, allow_infinity=False))
def test_abs(x):
    assert isclose(abs_(x), abs(x))

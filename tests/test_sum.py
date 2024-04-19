from itertools import tee

from hypothesis import given
from hypothesis.strategies import complex_numbers, floats, iterables, integers, text

from python_builtins import sum_


@given(
    iterables(
        integers()
        | floats(allow_nan=False, allow_infinity=False)
        | complex_numbers(allow_nan=False, allow_infinity=False)
    )
)
def test_sum_with_numbers(iterable):
    it1, it2 = tee(iterable)
    assert sum_(it1) == sum(it2)


@given(text())
def test_sum_with_strings(s):
    iterable = iter(s)
    assert sum_(iterable, start="") == s


@given(
    iterables(
        integers()
        | floats(allow_nan=False, allow_infinity=False)
        | complex_numbers(allow_nan=False, allow_infinity=False)
        | text()
    )
)
def test_sum_with_lists(iterable):
    it1, it2 = tee([list(iterable)])
    assert sum_(it1, start=[]) == next(it2)

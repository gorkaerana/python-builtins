from itertools import tee

from python_builtins import sum_


def test_sum_with_integers():
    it1, it2 = tee(range(1, 4))
    assert sum_(it1) == sum(it2)


def test_sum_with_floats():
    it1, it2 = tee(map(float, range(1, 4)))
    assert sum_(it1) == sum(it2)


def test_sum_with_strings():
    s = "hello"
    iterable = iter(s)
    assert sum_(iterable, start="") == s


def test_sum_with_lists():
    it1, it2 = tee([list(range(5))])
    assert sum_(it1, start=[]) == next(it2)

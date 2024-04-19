from itertools import tee

from hypothesis import given
from hypothesis.strategies import (
    iterables,
    binary,
    booleans,
    characters,
    complex_numbers,
    datetimes,
    decimals,
    floats,
    fractions,
    functions,
    integers,
    none,
    text,
    timedeltas,
    times,
    uuids,
)

from python_builtins import map_


def identity(x):
    return x


def make_tuple(x, y):
    return x, y


@given(
    functions(like=identity),
    iterables(
        binary()
        | booleans()
        | characters()
        | complex_numbers()
        | datetimes()
        | decimals()
        | floats()
        | fractions()
        | integers()
        | none()
        | text()
        | timedeltas()
        | times()
        | uuids()
    ),
)
def test_single_iterable(function, iterable):
    it1, it2 = tee(iterable)
    assert list(map_(function, it1)) == list(map(function, it2))


@given(
    functions(like=make_tuple),
    iterables(
        binary()
        | booleans()
        | characters()
        | complex_numbers()
        | datetimes()
        | decimals()
        | floats()
        | fractions()
        | integers()
        | none()
        | text()
        | timedeltas()
        | times()
        | uuids()
    ),
    iterables(
        binary()
        | booleans()
        | characters()
        | complex_numbers()
        | datetimes()
        | decimals()
        | floats()
        | fractions()
        | integers()
        | none()
        | text()
        | timedeltas()
        | times()
        | uuids()
    ),
)
def test_multiple_iterables(function, iterable1, iterable2):
    it1, it2 = tee(iterable1)
    it3, it4 = tee(iterable2)
    assert list(map_(function, it1, it3)) == list(map(function, it2, it4))

from itertools import tee

from hypothesis import given
from hypothesis.strategies import (
    binary,
    booleans,
    characters,
    complex_numbers,
    data,
    datetimes,
    decimals,
    floats,
    fractions,
    integers,
    iterables,
    none,
    text,
    timedeltas,
    times,
    uuids,
)

from python_builtins import zip_


iterable_of_anything = iterables(
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
)


@given(iterable_of_anything, iterable_of_anything)
def test_zip_two_iterables(it1, it2):
    (it11, it12), (it21, it22) = tee(it1), tee(it2)
    assert list(zip_(it11, it21)) == list(zip(it12, it22))


@given(integers(min_value=3, max_value=10), data())
def test_zip_multiple_iterables(n, data):
    iterable_tuples = [tee(data.draw(iterable_of_anything)) for _ in range(n)]
    assert list(zip_(*(it for (it, _) in iterable_tuples))) == list(
        zip(*(it for (_, it) in iterable_tuples))
    )

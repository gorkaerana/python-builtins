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
    integers,
    none,
    text,
    timedeltas,
    times,
    uuids,
)

from python_builtins import all_


@given(
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
    )
)
def test_all(iterable):
    it1, it2 = tee(iterable)
    assert all_(it1) == all(it2)

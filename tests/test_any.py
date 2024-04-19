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

from python_builtins import any_


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
def test_any(iterable):
    it1, it2 = tee(iterable)
    assert any_(it1) == any(it2)

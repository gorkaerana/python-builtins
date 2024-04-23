from itertools import tee

from hypothesis import given
from hypothesis.strategies import (
    binary,
    booleans,
    characters,
    complex_numbers,
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

from python_builtins import enumerate_


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
def test_enumerate(iterable):
    it1, it2 = tee(iterable)
    assert list(enumerate_(it1)) == list(enumerate(it2))

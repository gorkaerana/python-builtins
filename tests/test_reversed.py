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
    lists,
    none,
    text,
    timedeltas,
    times,
    uuids,
)

from python_builtins import reversed_


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
def test_reversed_object_with___reversed__(iterable):
    class Foo:
        def __init__(self, iterable):
            self.iterable = iterable

        def __reversed__(self):
            yield from self.iterable

    it1, it2 = tee(iterable)
    foo = Foo(it1)
    assert list(reversed_(foo)) == list(it2)


@given(
    lists(
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
def test_reversed_object_with___len___and___getitem__(sequence):
    assert list(reversed_(sequence)) == list(reversed(sequence))

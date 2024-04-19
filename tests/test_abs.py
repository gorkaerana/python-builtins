import pytest

from python_builtins import abs_

@pytest.mark.parametrize("x", [1, -1, 1., -1., 1+1j, 1-1j])
def test_abs(x):
    assert abs_(x) == abs(x)

import pytest

from python_builtins import property_


class Foo:
    x = 1

    def xget(self):
        return self.x

    def xset(self, value):
        self.x = value

    def xdel(self):
        del self.x

    bar = property_(xget, xset, xdel)


def test_getter():
    foo = Foo()
    assert foo.bar == 1

def test_setter():
    foo = Foo()
    foo.bar = 2
    assert foo.bar == 2

def test_deleter():
    foo = Foo()

    with pytest.raises(AttributeError) as e_info:
        del foo.bar

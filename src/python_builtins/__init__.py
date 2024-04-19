from typing import Callable, Iterable


def abs_(x: int | float):
    # TODO: support complex numbers
    return x if x >= 0 else -x


def all_(iterable: Iterable) -> bool:
    for i in iterable:
        if not i:
            return False
    return True


def any_(iterable: Iterable) -> bool:
    for i in iterable:
        if i:
            return True
    return False


def sum_(iterable: Iterable, /, start: int = 0):
    s = start
    for i in iterable:
        s += i
    return s


class property_:
    def __init__(
        self,
        fget: Callable | None = None,
        fset: Callable | None = None,
        fdel: Callable | None = None,
        doc=None,
    ):
        self.getter = fget
        self.setter = fset
        self.deleter = fdel
        self.doc = doc

        if self.setter is not None:
            self.__set__ = self.setter

        if self.deleter is not None:
            self.__delete__ = self.deleter

        if (self.__doc__ is None) and (self.getter.__doc__ is not None):
            self.doc = self.getter.__doc__

    def __get__(self, instance, owner):
        return self.getter(instance)

    def __call__(self, *args, **kwargs):
        return self.__init__(*args, **kwargs)

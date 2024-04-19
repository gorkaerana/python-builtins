from typing import Callable


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
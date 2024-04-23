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


def map_(function: Callable, iterable: Iterable, *iterables: Iterable):
    if iterables:
        for i in zip(iterable, *iterables):
            yield function(*i)
    else:
        for i in iterable:
            yield function(i)


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


class range_:
    def __init__(self, start, stop=None, step=None):
        if (stop is None) and (step is None):
            self.start = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.start = start
            self.stop = stop
            self.step = 1
        else:
            self.start, self.stop, self.step = start, stop, step

    def value_at_index(self, i):
        return self.start + self.step * i

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        if (
            ((value := self.value_at_index(index)) < self.stop)
            if (self.step > 0)
            else ((value := self.value_at_index(index)) > self.stop)
        ):
            return value
        raise IndexError

    def __len__(self):
        length = abs(self.start - self.stop) / abs(self.step)
        print(length)
        integer_below = int(length)
        return integer_below + 1 if (length - integer_below) > 0 else integer_below

    def __iter__(self):
        i = 0
        while (
            ((next_ := self.value_at_index(i)) < self.stop)
            if (self.step > 0)
            else ((next_ := self.value_at_index(i)) > self.stop)
        ):
            yield next_
            i += 1


def reversed_(seq: Iterable) -> Iterable:
    if hasattr(seq, "__reversed__"):
        yield from seq.__reversed__()
    elif hasattr(seq, "__len__") and hasattr(seq, "__getitem__"):
        for i in range(len(seq) - 1, -1, -1):
            yield seq[i]
    else:
        raise TypeError(f"'{type(seq)}' is not reversible")


def sum_(iterable: Iterable, /, start: int = 0):
    s = start
    for i in iterable:
        s += i
    return s


def zip_(*iterables):
    iterables = list(map(iter, iterables))
    while True:
        next_ = []
        for iterable in iterables:
            try:
                next_.append(next(iterable))
            except StopIteration:
                return
        yield tuple(next_)

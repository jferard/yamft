#  YAMFT - Yet another more-functools
#
#  Copyright (C) 2019 J. Férard <https://github.com/jferard>
#
#  This file is part of YAMFT.
#
#  YAMFT is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  YAMFT is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# The LIST COMPREHENSION section
from yamft import either, left, maybe


class Box:
    """This is a box where you put a value and can read it

    >>> from yamft.operator import pow1
    >>> b = Box(2)
    >>> list(i for _ in range(5) for i in b.apply(pow1(2)))
    [2, 4, 16, 256, 65536]
    >>> b.get()[0]
    4294967296
    """
    def __init__(self, value=None):
        if value is not None:
            self._value = value

    def set(self, value):
        prev = self._value
        self._value = value
        return prev,

    def get(self):
        return self._value,

    def apply(self, func):
        prev = self._value
        self._value = func(self._value)
        return prev,

class BoxB:
    """
    """
    def __init__(self, value):
        if value is not None:
            self._next = value
            self._buf = [None]
        else:
            self._buf = [None]

    def set(self, value):
        print("set", value, self._buf)
        self._next = value
        self._buf.append(value)
        return True

    def get(self):
        while self._next is not None:
            print("get", self._next, self._buf)
            yield self._next
            # optional set call goes here
            self._next = self._buf.pop()

    def iterate(self, func, test=None):
        while self._next is not None:
            yield self._next
            value = func(self._next)
            self._next = value
            if test is not None and not test(value):
                self._next = None

def try_or(try_func, *args, **kwargs):
    """

    >>> from yamft.operator import eq1
    >>> [try_or(int, c, ValueError, 0) for c in "1a2b3c"]
    [1, 0, 2, 0, 3, 0]

    """
    *args, exc, default = args
    return left(either(try_func, exc)(*args, **kwargs), default)


def not_except(try_func, *args, **kwargs):
    """
    >>> [int(c) for c in "1a2b3c" if not_except(int, c, ValueError)]
    [1, 2, 3]
    >>> [v for c in "1a2b3c" for v in not_except(int, c, ValueError)]
    [1, 2, 3]
    """
    *args, exc = args
    return maybe(either(try_func, exc)(*args, **kwargs))

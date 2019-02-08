# -*- coding: utf-8 -*-
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
import operator
import functools


def yamft_wraps(qualname, doc):
    """A YAMFT version of functools @wraps"""
    def real_wraps(func):
        func.__name__ = qualname
        func.__qualname__ = qualname
        func.__doc__ = doc
        return func
    return real_wraps

# Base bricks:
#
# * star and unstar to unpack/pack the arguments
# * either is a (value, Exception) tuple, where one of the two elements is None
# * maybe is a singleton or an empty tuple


def unstar(func):
    """Packs the positional arguments into sequence/collection

    >>> unstar(sum)(1,2,3)
    6

    """
    return lambda *args: func(args)


def star(func):
    """Unpacks the sequence/collection into positional arguments

    >>> import math
    >>> star(math.pow)([2,8])
    256.0

    """
    return lambda args: func(*args)


def either(func, *excs):
    """

    >>> either(int, ValueError)(1)
    (1, None)
    >>> either(int, ValueError)("a")
    (None, ValueError(...))
    >>> [left(either(int, ValueError)(c), 0) for c in "1a2b3c"]
    [1, 0, 2, 0, 3, 0]

    """
    if excs:
        exc = tuple(excs)
    else:
        exc = Exception

    @yamft_wraps(f"either_{func}", f"""Return ({func}(args), None) if there is 
    no exception, else (None, exception)")""")
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs), None
        except exc as e:
            return None, e
    return wrapped


def left(either_value, default):
    """Return the left value of an either, otherwise default

    >>> left((1, None), 0)
    1
    >>> left((None, Exception()), 0)
    0
    """
    v = either_value[0]
    return default if v is None else v


def maybe(either_value):
    """Return the a singleton containing the left value of an either,
    otherwise an empty tuple

    >>> maybe((1, None))
    (1,)
    >>> maybe((None, Exception()))
    ()
    >>> [v for c in "1a2b3c" for v in maybe(either(int, ValueError)(c))]
    [1, 2, 3]
    """
    v = either_value[0]
    return () if v is None else (v,)


fst = operator.itemgetter(0)
snd = operator.itemgetter(1)
thd = operator.itemgetter(2)
fth = operator.itemgetter(3)


# The MAP section

# The MISC section


def flip(func):
    """Flip the two first arguments of a function

    >>> import operator
    >>> flip(operator.sub)(1,0)
    -1
    >>> import functools
    >>> sub_1 = functools.partial(flip(operator.sub), 1)
    >>> sub_1(10)
    9
    """

    def wrapped(b, a, *args, **kwargs):
        return func(a, b, *args, **kwargs)

    return wrapped


def even(v):
    """

    >>> list(filter(even, range(10)))
    [0, 2, 4, 6, 8]

    """
    return v % 2 == 0


def odd(v):
    """

    >>> list(filter(odd, range(10)))
    [1, 3, 5, 7, 9]

    """
    return v % 2 == 1


def ident(x):
    """

    >>> ident(1)
    1

    """
    return x


def merge(d1, d2):
    """

    """
    return {**d1, **d2}


def swap(a, b):
    return b, a


def coalesce(*values):
    """Return the first True value in values or None

    >>> coalesce() is None
    True
    >>> coalesce("a")
    'a'
    >>> coalesce("", "a")
    'a'
    """
    return next((v for v in values if v), None)


def find_first(func, *values):
    """Return the first value that matches the func in values or None

    >>> find_first(lambda x: False) is None
    True
    >>> find_first(lambda x: False, *range(10)) is None
    True
    >>> find_first(even, *range(10))
    0
    >>> find_first(odd, *range(10))
    1
    """
    return next((v for v in values if func(v)), None)


def coalesce_none(*values):
    """Return the first True value in values or None

    >>> coalesce() is None
    True
    >>> coalesce("a")
    'a'
    >>> coalesce("", "a")
    'a'
    """
    return next((v for v in values if v is not None), None)


def partial_r(func, *p_args, **p_kwargs):
    """Simplified version of fuctools.partial for rightmost arguments

    >>> import operator
    >>> partial_r(operator.sub, 1)(10)
    9
    >>> list(map(partial_r(operator.pow, 2), range(1, 11)))
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """

    def wrapped(*args, **kwargs):
        new_kwargs = {**p_kwargs, **kwargs}
        return func(*args, *p_args, **new_kwargs)

    return wrapped


def dot(*funcs):
    """Function must be starred in order to pass one argument.

    >>> from yamft.operator import add1, pow1
    >>> dot(pow1(2), add1(10))(2)
    144
    >>> dot(add1(10), pow1(2))(2)
    14

    >>> import math
    >>> dot(math.sqrt, math.pow)(2, 8)
    16.0
    >>> from yamft import star
    >>> dot(math.sqrt, star(math.pow), divmod)(23, 3)
    7.0

    >>> dot(float, snd, str.split)('-- 2.5 --')
    2.5

    """
    @yamft_wraps(f"dot_{funcs}", "Same as {}".format(".".join(map(str, funcs))))
    def wrapped(*args, **kwargs):
        it = reversed(funcs)
        try:
            first_func = next(it)
            ret = first_func(*args, **kwargs)
            for func in it:
                ret = func(ret, **kwargs)
        except StopIteration:
            ret = args
        return ret
    return wrapped


from yamft.operator import *
from yamft.comprehension import *
from yamft.incubator import *
from yamft.map_fold import *
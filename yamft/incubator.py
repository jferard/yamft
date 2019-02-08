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
from functools import partial
from yamft import fst, snd, dot


def curry(func):
    """Curry a function

    >>> import operator
    >>> from yamft import flip
    >>> curryfied_sub = curry(flip(operator.sub))
    >>> curryfied_sub(5)(7)
    2

    >>> from yamft import apply_all
    >>> list(map(list, apply_all(map(curry(operator.mul), range(1,4)), range(1,4))))
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """
    def wrapped(a):
        return partial(func, a)

    return wrapped


def unlazy(func):
    """

    >>> unlazy(lambda x, y: x + y())(1, 2)
    3

    """
    def wrapped(*args, **kwargs):
        args = tuple([args[0]] + [lambda: arg for arg in args[1:]])
        return func(*args, **kwargs)

    return wrapped


def once(ret, *_args):
    """
    `v in once(value)` is equivalent to `v = value`.

    >>> {k: v for t in ["a b", "c d"] for k, v in once(t.split())}
    {'a': 'b', 'c': 'd'}

    Optional parameters may be used for side effects, but won't
    affect the result

    >>> {k: v for t in ["a b", "c d"] for k, v in once(t.split(), print("parse '{}'".format(t)))}
    parse 'a b'
    parse 'c d'
    {'a': 'b', 'c': 'd'}
    """
    return ret,


def side(*_args):
    """
    Perform a side effect and return True.

    >>> seen = set()
    >>> [v for v in [1,2,4,2,7,1,7,4,3] if v not in seen and side(seen.add(v))]
    [1, 2, 4, 7, 3]

    :param _args:
    :return:
    """
    return True


filter0 = partial(filter, None)


def map_k(func, iterable):
    """
    Add a key after the value to create a tuple `(v, func(v))`
    for every `v` in `iterable`.

    >>> from yamft import add1
    >>> list(map_k(add1(2), range(5)))
    [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)]
    """

    return map(lambda v: (v, func(v)), iterable)


sorted_k = partial(sorted, key=snd)
collect = partial(map, fst)


def filter_k(func, iterable):
    """
    Input and output: tuples (value, key)

    >>> from yamft import even, add1
    >>> from operator import neg
    >>> list(filter_k(even, (map_k(dot(neg, add1(1)), range(5)))))
    [(1, -2), (3, -4)]
    """
    if func is None:
            func = bool
    return filter(dot(func, snd), iterable)


def filter0_k(iterable):
    """

    >>> from yamft import sub1
    >>> list(filter0_k(map_k(sub1(2), range(5))))
    [(0, -2), (1, -1), (3, 1), (4, 2)]
    """
    return filter(dot(bool, snd), iterable)


def filter_map(func, iterable):
    """

    >>> from yamft import either
    >>> list(filter_map(either(float, ValueError), ["1","a","3","4"]))
    [1.0, 3.0, 4.0]
    """
    return map(fst, filter(lambda e: snd(e) is None, map(func, iterable)))
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

from yamft import star, dot


def map_star(func, *iterables):
    """A version of map that unpacks the zipped tuples into positional arguments

    >>> import math
    >>> list(map_star(math.pow, zip([2,2], [4,8])))
    [16.0, 256.0]
    """
    return map(star(func), *iterables)


def map_dot(*args):
    """A version of map that composes the functions before applying map

    >>> from yamft import snd
    >>> list(map_dot(snd, divmod, [10, 11], [3, 3]))
    [1, 2]
    >>> list(map_dot(snd, divmod))
    Traceback (most recent call last):
    ...
    TypeError: map() must have at least two arguments.
    """
    for i, arg in enumerate(args):
        if "__call__" not in dir(arg):
            return map(dot(*args[:i]), *args[i:])
    return map(dot(*args))


def apply_all(funcs, *iterables):
    """
    >>> list(apply_all([float, str], range(1,10)))
    [(1.0, '1'), (2.0, '2'), (3.0, '3'), (4.0, '4'), (5.0, '5'), (6.0, '6'), (7.0, '7'), (8.0, '8'), (9.0, '9')]
    """
    return zip(*(map(lambda func: map(func, *iterables), funcs)))


# The FOLD section

def reduce_r(function, sequence, lazy_last=None):
    """Equivalent to Haskell's `foldr` function.
    `function` must take a lazy (ie callable) second arg.

    The classical example:

    >>> reduce_r(lambda x, acc: [x] + acc(), range(10), lambda: [])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> reduce_r(lambda x, acc: acc() + [x], range(10), lambda: [])
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    More Haskell style:

    >>> from yamft.operator import lazy_cons
    >>> reduce_r(lazy_cons, [1, 2, 3, 4, 5, 6, 7, 8, 9, []])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    What about infinite sequences?

    >>> import itertools
    >>> reduce_r(lambda x, acc: x and acc(), itertools.repeat(False))
    False

    A more tricky example:

    >>> def f(a, lazy_b):
    ...     return a if a > 5 else a + lazy_b()
    ...
    >>> import itertools
    >>> reduce_r(f, itertools.count())
    21

    Explanation. According to fold right definition, the reurn value is:
    `f(1, lambda: f(2, lambda: f(3, lambda: f(4, lambda: f(5, lambda: f(6, lambda: ...))))))`.
    Since `f(6, _) == 6`, we have `f(1, lambda: f(2, lambda: f(3, lambda: f(4, lambda: f(5, lambda: 6)))))`
    Since `f(5, lambda: 6) == 5 + (lambda: 6)() == 5 + 6 == 11`, we have
    `f(1, lambda: f(2, lambda: f(3, lambda: f(4, lambda: 11))))`. The next steps
    are:

    * `f(1, lambda: f(2, lambda: f(3, lambda: 15)))`
    * `f(1, lambda: f(2, lambda: 18))`
    * `f(1, lambda: 20)`
    * `21`

    Some other cases:

    >>> reduce_r(lazy_cons, [])
    Traceback (most recent call last):
    ...
    StopIteration
    >>> reduce_r(lazy_cons, [[]])
    []
    >>> reduce_r(lazy_cons, [], lambda: [])
    []
    >>> reduce_r(lazy_cons, [1], lambda: [])
    [1]
    >>> reduce_r(lazy_cons, [1, []])
    [1]
    """

    def reduce_r_lazy(first, second, it):
        """Returns a callable"""

        def wrapped():
            try:
                third = next(it)
            except StopIteration:
                if lazy_last is None:
                    return function(first, lambda: second)
                else:
                    return function(first, lambda: function(second, lazy_last))
            else:
                return function(first, reduce_r_lazy(second, third, it))

        return wrapped

    it = iter(sequence)
    try:
        first = next(it)
        try:
            second = next(it)
        except StopIteration:
            if lazy_last is None:
                return first
            else:
                return function(first, lazy_last)
        else:
            return reduce_r_lazy(first, second, it)()
    except StopIteration:
        if lazy_last is None:
            raise
        else:
            return lazy_last()


def map_keys(func, d):
    """

    >>> from yamft import square
    >>> map_keys(square, {1:1, 2:2, 3:3})
    {1: 1, 4: 2, 9: 3}

    """
    return {func(k): v for k, v in d.items()}


def map_values(func, d):
    """

    >>> from yamft import square
    >>> map_values(square, {1:1, 2:2, 3:3})
    {1: 1, 2: 4, 3: 9}

    >>> from functools import partial
    >>> from yamft import split1
    >>> map_values(int, dict(map(split1('='), "A=5,B=7".split(','))))
    {'A': 5, 'B': 7}

    """
    return {k: func(v) for k, v in d.items()}


def map_fst(func, items):
    """
    >>> list(map_fst(ord, [('A',1,1,1), ('B',2,2,2)]))
    [(65, 1, 1, 1), (66, 2, 2, 2)]
    """

    return ((func(one), *other) for one, *other in items)


def map_snd(func, items):
    """
    >>> list(map_snd(ord, [(1,'A',1,1), (2,'B',2,2)]))
    [(1, 65, 1, 1), (2, 66, 2, 2)]
    """
    return ((one, func(two), *other) for one, two, *other in items)


def map_thd(func, items):
    """
    >>> list(map_thd(ord, [(1,1,'A',1), (2,2,'B',2)]))
    [(1, 1, 65, 1), (2, 2, 66, 2)]
    """
    return ((one, two, func(three), *other) for one, two, three, *other in items)


def map_fth(func, items):
    """
    >>> list(map_fth(ord, [(1,1,1,'A'), (2,2,2,'B')]))
    [(1, 1, 1, 65), (2, 2, 2, 66)]
    """
    return ((one, two, three, func(four), *other) for one, two, three, four, *other in items)
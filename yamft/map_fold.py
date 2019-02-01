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
from yamft import star

def map_star(func, *iterables):
    """A version of map that unpacks the zipped tuples into positional arguments

    >>> import math
    >>> list(map_star(math.pow, zip([2,2], [4,8])))
    [16.0, 256.0]
    """
    return map(star(func), *iterables)


def map_compose(funcs, *iterables):
    """A version of map that composes the functions before applying map"""
    return map(compose(*funcs), *iterables)


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


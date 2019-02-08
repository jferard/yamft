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
"""A list of helper + doctests"""

from yamft import *


def yamft_help(func):
    """
    Help on yamft funcs

    >>> yamft_help(list)
    Help on class list in module builtins:
    ...
    <BLANKLINE>

    >>> yamft_help(fst) # doctest:+ELLIPSIS
    Help on fst:
    <BLANKLINE>
            Returns the first element of a sequence
    <BLANKLINE>
        ... fst([2, 3, 4, 5])
        2
        ... fst([])
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
    <BLANKLINE>
    <BLANKLINE>

    """
    global _my_globals
    try:
        name = _my_globals[func]
        help_func = globals().get("_help_"+name)
    except KeyError:
        help(func)
    else:
        print("""Help on {}:

        {}""".format(name, help_func.__doc__))


def _help_fst():
    """Returns the first element of a sequence

    >>> fst([2, 3, 4, 5])
    2
    >>> fst([])
    Traceback (most recent call last):
    ...
    IndexError: list index out of range

    """
    pass


def _help_snd():
    """Returns the second element of a sequence

    >>> snd([2, 3, 4, 5])
    3

    """
    pass


def _help_thd():
    """Returns the third element of a sequence

    >>> thd([2, 3, 4, 5])
    4

    """
    pass


def _help_fth():
    """Returns the fourth element of a sequence

    >>> fth([2, 3, 4, 5])
    5

    """
    pass


def _help_filter0():
    """Shortcut for `filter(None, ...)`

    >>> list(filter0([1,0,2,3,0,4]))
    [1, 2, 3, 4]

    """
    pass


def _help_sorted_k():
    """Sort values by key.
    Input and output: tuples (value, key)

    >>> from operator import neg
    >>> list(sorted_k(map_k(neg, range(5))))
    [(4, -4), (3, -3), (2, -2), (1, -1), (0, 0)]
    """
    pass


def _help_collect():
    """Remove the key

    >>> from operator import neg
    >>> list(collect(sorted_k(map_k(neg, range(5)))))
    [4, 3, 2, 1, 0]

    """
    pass




_my_globals = {v: k for k, v in globals().items() if "__call__" in dir(v)}

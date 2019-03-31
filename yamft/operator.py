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

#  YAMFT - Yet another more-functools
#
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

"""Adaptation of Lib/operator.py to functional style: every binary operator `<bin>(a, b)`
has an equivalent `<bin1>(b)` so that `<bin1>(b)(a) = `<bin>(a, b)`"""

__all__ = ['add1', 'and1', 'bw_and1', 'bw_or1', 'concat1', 'contains1', 'countOf1',
           'delitem1', 'eq1', 'floordiv1', 'ge1', 'getitem1', 'gt1',
           'iconcat1', 'imatmul1', 'indexOf1', 'is1', 'is_not1', 'le1',
           'lt1', 'matmul1', 'mod1', 'mul1', 'ne1', 'or1', 'pow1',
           'rshift1', 'setitem1', 'sub1', 'truediv1', 'xor1',
           'dget', 'square', 'cube', 'split1']


from yamft import yamft_wraps

# Comparison Operations *******************************************************#


def lt1(b):
    """Return a function a -> (a < b)."""
    @yamft_wraps(f"lt_{b}", f"Same as a < {b}.")
    def wrapped(a):
        return a < b
    return wrapped


def le1(b):
    """Return a function a -> (a <= b)."""
    @yamft_wraps(f"le_{b}", f"Same as a <= {b}.")
    def wrapped(a):
        return a <= b
    return wrapped


def eq1(b):
    """Return a function a -> (a == b).

    >>> eq1(10)(5)
    False
    """
    @yamft_wraps(f"eq_{b}", f"Same as a == {b}.")
    def wrapped(a):
        return a == b

    return wrapped


def ne1(b):
    """Return a function a -> (a != b)."""
    @yamft_wraps(f"ne_{b}", f"Same as a != {b}.")
    def wrapped(a):
        return a != b
    return wrapped


def ge1(b):
    """Return a function a -> (a >= b)."""
    @yamft_wraps(f"ge_{b}", f"Same as a >= {b}.")
    def wrapped(a):
        return a >= b
    return wrapped


def gt1(b):
    """Return a function a -> (a > b)."""
    @yamft_wraps(f"gt_{b}", f"Same as a > {b}.")
    def wrapped(a):
        return a > b
    return wrapped


# Logical Operations **********************************************************#


def is1(b):
    """Return a function a -> (a is b)."""
    @yamft_wraps(f"is_{b}", f"Same as a is {b}.")
    def wrapped(a):
        return a is b
    return wrapped


def is_not1(b):
    """Return a function a -> (a is b)."""
    @yamft_wraps(f"is_not_{b}", f"Same as a is not {b}.")
    def wrapped(a):
        return a is not b
    return wrapped


def is_none(a):
    return a is None


def is_not_none(a):
    return a is not None

# Mathematical/Bitwise Operations *********************************************#


def add1(b):
    """Return a function a -> (a + b)."""
    @yamft_wraps(f"add_{b}", f"Same as a + {b}.")
    def wrapped(a):
        return a + b
    return wrapped


def bw_and1(b):
    """Return a function a -> (a & b)."""
    @yamft_wraps(f"bw_and_{b}", f"Same as a & {b}.")
    def wrapped(a):
        return a & b
    return wrapped


def floordiv1(b):
    """Return a function a -> a // b."""
    @yamft_wraps(f"floordiv_{b}", f"Same as a // {b}.")
    def wrapped(a):
        return a // b
    return wrapped


def lshift1(b):
    """Return a function a -> a << b."""
    @yamft_wraps(f"lshift_{b}", f"Same as a << {b}.")
    def wrapped(a):
        return a << b
    return wrapped


def mod1(b):
    """Return a function a -> a % b."""
    @yamft_wraps(f"mod_{b}", f"Same as a % {b}.")
    def wrapped(a):
        return a % b
    return wrapped


def mul1(b):
    """Return a function a -> a * b."""
    @yamft_wraps(f"mul_{b}", f"Same as a * {b}.")
    def wrapped(a):
        return a * b
    return wrapped


def matmul1(b):
    """Return a function a -> a @ b."""
    @yamft_wraps(f"matmul_{b}", f"Same as a @ {b}.")
    def wrapped(a):
        return a @ b
    return wrapped


def bw_or1(b):
    """Return a function a -> a | b."""
    @yamft_wraps(f"bw_or_{b}", f"Same as a | {b}.")
    def wrapped(a):
        return a | b
    return wrapped


def or1(b):
    """Return a function a -> a or b."""
    @yamft_wraps(f"or_{b}", f"Same as a or {b}.")
    def wrapped(a):
        return a or b
    return wrapped


def pow1(b):
    """Return a function a -> a ** b."""
    @yamft_wraps(f"pow_{b}", f"Same as a ** {b}.")
    def wrapped(a):
        return a ** b
    return wrapped


def square(i):
    return i*i


def cube(i):
    return i*i*i


def rshift1(b):
    """Return a function a -> a >> b."""
    @yamft_wraps(f"rshift_{b}", f"Same as a >> {b}.")
    def wrapped(a):
        return a >> b
    return wrapped


def sub1(b):
    """Return a function a -> a * b."""
    @yamft_wraps(f"sub_{b}", f"Same as a - {b}.")
    def wrapped(a):
        return a - b
    return wrapped


def truediv1(b):
    """Return a function a -> a / b."""
    @yamft_wraps(f"truediv_{b}", f"Same as a / {b}.")
    def wrapped(a):
        return a / b
    return wrapped


def xor1(b):
    """Return a function a -> a ^ b."""
    @yamft_wraps(f"xor_{b}", f"Same as a ^ {b}.")
    def wrapped(a):
        return a ^ b
    return wrapped


# Sequence Operations *********************************************************#


def concat1(b):
    """Return a function a -> (a + b) for sequences."""
    if not hasattr(b, '__getitem__'):
        msg = "'{}' object can't be concatenated".format(type(b).__name__)
        raise TypeError(msg)

    @yamft_wraps(f"concat_{b}", f"Same as a + {b} for sequences.")
    def wrapped(a):
        return a + b

    return wrapped


def contains1(b):
    """Return a function a -> b in a."""
    @yamft_wraps(f"contains_{b}", f"Same as {b} in a.")
    def wrapped(a):
        return b in a

    return wrapped


def countOf1(b):
    """Return a function a -> the number of times b occurs in a."""
    @yamft_wraps(f"countOf_{b}", f"Same as count of {b} in a.")
    def wrapped(a):
        count = 0
        for i in a:
            if i == b:
                count += 1
        return count

    return wrapped


def delitem1(b):
    """Return a function a -> del a[b]."""
    @yamft_wraps(f"delitem_{b}", f"Same as del a[{b}].")
    def wrapped(a):
        del a[b]

    return wrapped


def getitem1(b):
    """Return a function a -> a[b]."""
    @yamft_wraps(f"getitem_{b}", f"Same as count of a[{b}].")
    def wrapped(a):
        return a[b]

    return wrapped


def indexOf1(b):
    """Return a function a -> b.index(1)."""
    @yamft_wraps(f"indexof_{b}", f"Return the first index of b in a.")
    def wrapped(a):
        for i, j in enumerate(a):
            if j == b:
                return i
        else:
            raise ValueError('sequence.index(x): x not in sequence')
    return wrapped


def setitem1(b, c):
    """Return a function a -> a[b] = c."""
    @yamft_wraps(f"setitem_{b}_{c}", f"Same as a[{b}] = {c}.")
    def wrapped(a):
        a[b] = c
    return wrapped


# In-place Operations *********************************************************#


def iconcat1(b):
    """Return a function a -> (a += b), for a and b sequences."""
    if not hasattr(b, '__getitem__'):
        msg = "'{}' object can't be concatenated".format(type(b.__name__))
        raise TypeError(msg)

    @yamft_wraps(f"iconcat_{b}", f"Same as a += {b} for sequences.")
    def wrapped(a):
        a += b
        return a

    return wrapped


def imatmul1(b):
    """Return a function a -> (a @= b), for a and b sequences."""
    if not hasattr(b, '__getitem__'):
        msg = "'{}' object can't be concatenated".format(type(b.__name__))
        raise TypeError(msg)

    @yamft_wraps(f"imatmul_{b}", f"Same as a @= {b} for sequences.")
    def wrapped(a):
        a @= b
        return a


def and1(b):
    """Return a function a -> (a and b)."""
    @yamft_wraps(f"and_{b}", f"Same as a and {b}.")
    def wrapped(a):
        return a and b
    return wrapped

## lazy operators


def lazy_and(a, b):
    return a and b()


def lazy_or(a, b):
    return a or b()


def cons(a, b):
    return [a] + b


def lazy_cons(a, b):
    return [a] + b()


def dget(k, d=None):
    return lambda D: D.get(k, d)


def split1(sep=None, maxsplits=-1):
    return lambda s: s.split(sep, maxsplits)


def destr(sequence):
    """

    >>> destr([1,2,3])
    (1, [2, 3])
    >>> dict(map(destr, [[1,2,3], [4,5,6]]))
    {1: [2, 3], 4: [5, 6]}
    """
    return sequence[0], sequence[1:]
|Build Status| |Code Coverage|

YAMFT (Yet another `more-functools`)
====================================

Copyright (C) J. Férard 2019

YAMFT is another functional library for Python.

Goals
-----
YAMFT doesn't try to mimic Haskell, but rather tries to improve Python functional skills. It targets two main domains:

* `list` and `dict` comprehensions: YAMFT aims to provide functions that will help write more powerful list and dict comprehensions.
* `map`: YAMFT aims to provide helpers to write maps.

But the main goal of YAMFT is... fun. Python is not a functional language, but it's sometimes amusing to use functional idioms to express some lists.


Tricky list comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~
List comprehension are very powerful, and sometimes we want them to be even more powerful. This
leads to some weird constructions. YAMFT aims to provide helpers for writing those list comprehensions.

Functional paradigm in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It should be obvious for everyone that Python is not a pure functional language
like Haskell, and that the Python code is often more readable and efficient
when we **do not** use the functional paradigm. Tough, I find that functional
programming is sometimes beautiful.


Method
------
Functional style in Python is often cumbersome:

    >>> map(lambda x:x*x*x, range(5))
    [0, 1, 8, 27, 64]

is worse than:

    >>> [x*x*x for x in range(5)]
    [0, 1, 8, 27, 64]


But this is more disputable when you compare:

    >>> [str(x) for x in range(5)]
    ['0', '1', '2', '3', '4']

with:

    >>> list(map(str, range(5)))
    ['0', '1', '2', '3', '4']

I prefer the latter. The main issue is the lambda syntax. Hence, YAMFT aims to provide plug and play curryfied functions to avoid lambdas.


Installation
------------

Needs Python 3.7

Just ``git clone`` the repo:

.. code-block:: bash

    > git clone https://github.com/jferard/yamft.git

Test
----

.. code-block:: bash

    > pytest --doctest-modules

Help
----
Functions are not first class citizens in Python. You can't give them a docstring when they are defined by an assignment (e.g. `fst = operator.itemgetter(0)`). YAMFT has a special `yamft_help` function to handle this case:

    >>> yamft_help(fst) # doctest:+ELLIPSIS
    Help on fst:
    ...

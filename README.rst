|Build Status| |Code Coverage|

YAMFT (Yet another `more-functools`)
====================================

Copyright (C) J. Férard 2019

YAMFT is another functional library for Python.

Goals
-----
YAMFT doesn't try to mimic Haskell, but rather tries to improve Python functional skills. It targets two main domains:

* `list` and `dict` comprehensions: YAMFT aims to provide functions that will help write more powerful list and dict comprehension.
* `map`: YAMFT aims to provide helpers to write maps.


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


Installation
------------

Needs Python 3.7

Just ``git clone`` the repo:

.. code-block:: bash

    > git clone https://github.com/jferard/yamft.git
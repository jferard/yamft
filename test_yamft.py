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

from yamft import *
from yamft.operator import *
import itertools

import unittest


class TestYAMFT(unittest.TestCase):
    def test1(self):
        haystack = "absddrgvrezfdfgvreegfdvsdfezgvfdfbdfhtgsdvve"
        needle = "df"
        box = Box(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], list(itertools.takewhile(ge1(0), (i for _ in itertools.count() for i in box.get() if box.set(haystack.find(needle, i+1))))))
        self.assertEqual([12, 24, 31, 34], list(itertools.takewhile(ge1(0), (i for _ in itertools.count() for i in box.apply(lambda j: haystack.find(needle, j+1))))))


if __name__ == '__main__':
    unittest.main()

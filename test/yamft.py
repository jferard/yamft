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
import itertools

import unittest

frvr = itertools.count


class TestBox(unittest.TestCase):
    def test1(self):
        haystack = "absddrgvrezfdfgvreegfdvsdfezgvfdfbdfhtgsdvve"
        needle = "df"

        all_ge_0 = dot(list, partial(itertools.takewhile, ge1(0)))

        box = Box(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], all_ge_0(i for _ in frvr() for i in box.get() if
                                                    box.set(haystack.find(needle, i + 1))))
        box = Box(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], all_ge_0(i for _ in frvr() for i in
                                                    box.apply(lambda j: haystack.find(needle, j + 1))))

        box = Box(haystack.find(needle))
        next_index = dot(partial(haystack.find, needle), add1(1))
        self.assertEqual([12, 24, 31, 34], all_ge_0(i for _ in frvr() for i in box.apply(next_index)))


class TestBoxB(unittest.TestCase):
    def test2(self):
        haystack = "absddrgvrezfdfgvreegfdvsdfezgvfdfbdfhtgsdvve"
        needle = "df"

        all_ge_0 = dot(list, partial(itertools.takewhile, ge1(0)))
        box = BoxB(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], all_ge_0(i for i in box.get() if box.set(haystack.find(needle, i + 1))))
        box = BoxB(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], list(
            i for i in box.get() if coalesce_none(i, -1) >= 0 and box.set(haystack.find(needle, i + 1))))

    def test3(self):
        haystack = "absddrgvrezfdfgvreegfdvsdfezgvfdfbdfhtgsdvve"
        needle = "df"
        next_index = dot(partial(haystack.find, needle), add1(1))

        all_ge_0 = dot(list, partial(itertools.takewhile, ge1(0)))

        box = BoxB(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], all_ge_0(box.iterate(next_index)))
        box = BoxB(haystack.find(needle))
        self.assertEqual([12, 24, 31, 34], list(box.iterate(next_index, ge1(0))))


class TestSortedK(unittest.TestCase):
    def test1(self):
        rows = ['1.4 2.5 5.6', '2.4 7.5 9.8', '4.8 9.7 2.5', '4.5 6.5 7.9', '1.3 3.4 12.6']
        float_key = dot(float, thd, str.split)
        get_sorted_le8 = dot(sorted_k, partial(filter_k, le1(8)))
        self.assertEqual(['4.8 9.7 2.5', '1.4 2.5 5.6', '4.5 6.5 7.9'],
                         list(collect(get_sorted_le8(map_k(float_key, rows)))))



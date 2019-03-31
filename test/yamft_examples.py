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
from yamft import *
import itertools

import unittest

class Examples(unittest.TestCase):
    def test1(self):
        L = [
            {'id': 1, 'date': '2019-02-28', 'val': 10.5},
            {'id': 2, 'date': '2019-02-28', 'val': 12.7},
            {'id': 1, 'date': '2019-03-01', 'val': 10.9},
            {'id': 2, 'date': '2019-03-01', 'val': 12.1},
            {'id': 2, 'date': '2019-03-02', 'val': 12.9},
        ]
        self.assertEqual({1: [{'date': '2019-02-28', 'id': 1, 'val': 10.5},
                              {'date': '2019-03-01', 'id': 1, 'val': 10.9}],
                          2: [{'date': '2019-02-28', 'id': 2, 'val': 12.7},
                              {'date': '2019-03-01', 'id': 2, 'val': 12.1},
                              {'date': '2019-03-02', 'id': 2, 'val': 12.9}]}, group_by(dget('id'), L))
        self.assertEqual([[{'date': '2019-02-28', 'id': 1, 'val': 10.5},
                           {'date': '2019-03-01', 'id': 1, 'val': 10.9}],
                          [{'date': '2019-02-28', 'id': 2, 'val': 12.7},
                           {'date': '2019-03-01', 'id': 2, 'val': 12.1},
                           {'date': '2019-03-02', 'id': 2, 'val': 12.9}]], list(group_by(dget('id'), L).values()))
        self.assertEqual({'date': '2019-03-01', 'id': 1, 'val': 10.9},
                         merge({'date': '2019-02-28', 'id': 1, 'val': 10.5},
                               {'date': '2019-03-01', 'id': 1, 'val': 10.9}))
        self.assertEqual({'date': '2019-03-02', 'id': 2, 'val': 12.9},
                         merge({'date': '2019-02-28', 'id': 2, 'val': 12.7},
                               {'date': '2019-03-01', 'id': 2, 'val': 12.1},
                               {'date': '2019-03-02', 'id': 2, 'val': 12.9}))
        self.assertEqual([{'date': '2019-03-01', 'id': 1, 'val': 10.9},
                          {'date': '2019-03-02', 'id': 2, 'val': 12.9}],
                         list(map_star(merge, group_by(dget('id'), L).values())))


if __name__ == '__main__':
    unittest.main()

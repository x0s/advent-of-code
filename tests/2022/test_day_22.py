import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_22 import (part_1)


@contextmanager
def mocked_get_input(year, day):
    yield """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().patchGetInput(2022, 22, 1, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 6032)


if __name__ == "__main__":
    unittest.main()
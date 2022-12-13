import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_13 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 13, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 13)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 140)

if __name__ == "__main__":
    unittest.main()
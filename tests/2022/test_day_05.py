import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_05 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n\n"
  

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 5, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 'CMZ')

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 'MCD')

if __name__ == "__main__":
    unittest.main()
import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_20 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield """1\n2\n-3\n3\n-2\n0\n4\n"""

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 20, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 3)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 1623178306)

if __name__ == "__main__":
    unittest.main()
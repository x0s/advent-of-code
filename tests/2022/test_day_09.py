import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_09 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input_part_1(year, day):
    yield "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n"

@contextmanager
def mocked_get_input_part_2(year, day):
    yield "R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20\n"


class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().patchGetInput(2022, 9, 1, mocked_get_input_part_1)
        super().patchGetInput(2022, 9, 2, mocked_get_input_part_2)
        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 13)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 36)

if __name__ == "__main__":
    unittest.main()
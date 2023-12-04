import unittest

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch

from advent_of_code.year_2023.day_01 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input_1(year, day):
    yield "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"

@contextmanager
def mocked_get_input_2(year, day):
    yield "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixt"

class TestExamples(TestCase):

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('advent_of_code.year_2023.day_01.part_1.get_input', side_effect=mocked_get_input_1))
        cls.enterClassContext(
            patch('advent_of_code.year_2023.day_01.part_2.get_input', side_effect=mocked_get_input_2))

        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        calories = part_1.main()
        self.assertEqual(calories, 142)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        calories = part_2.main()
        self.assertEqual(calories, 281)

if __name__ == "__main__":
    unittest.main()
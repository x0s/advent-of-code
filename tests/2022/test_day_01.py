import unittest

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch

from advent_of_code.year_2022.day_01 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n"

class TestExamples(TestCase):

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('advent_of_code.year_2022.day_01.part_1.get_input', side_effect=mocked_get_input))
        cls.enterClassContext(
            patch('advent_of_code.year_2022.day_01.part_2.get_input', side_effect=mocked_get_input))

        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        calories = part_1.main()
        self.assertEqual(calories, 24_000)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        calories = part_2.main()
        self.assertEqual(calories, 45_000)

if __name__ == "__main__":
    unittest.main()
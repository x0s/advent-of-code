import unittest

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch

from advent_of_code.year_2021.day01 import (part_1,
                                            part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "199\n200\n208\n210\n200\n207\n240\n269\n260\n263"

class TestExamples(TestCase):

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('advent_of_code.year_2021.day01.part_1.get_input', side_effect=mocked_get_input))
        cls.enterClassContext(
            patch('advent_of_code.year_2021.day01.part_2.get_input', side_effect=mocked_get_input))

        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        count = part_1.main()
        self.assertEqual(count, 7)

    def test_part2(self):
        """Test if example from part 1 problem statement works"""
        count = part_2.main()
        self.assertEqual(count, 5)

if __name__ == "__main__":
    unittest.main()
import unittest

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch

from advent_of_code.year_2021.day02 import (part_1,
                                            part_2)


@contextmanager
def mocked_get_input(year, day):
    yield """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

class TestExamples(TestCase):

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('advent_of_code.year_2021.day02.part_1.get_input', side_effect=mocked_get_input))
        cls.enterClassContext(
            patch('advent_of_code.year_2021.day02.part_2.get_input', side_effect=mocked_get_input))

        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        position, depth, product = part_1.main()
        self.assertEqual(position, 15)
        self.assertEqual(depth, 10)
        self.assertEqual(product, 150)

    def test_part2(self):
        """Test if example from part 1 problem statement works"""
        position, depth, product = part_2.main()
        self.assertEqual(position, 15)
        self.assertEqual(depth, 60)
        self.assertEqual(product, 900)

if __name__ == "__main__":
    unittest.main()
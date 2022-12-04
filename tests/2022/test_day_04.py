import unittest

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch

from advent_of_code.year_2022.day_04 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n"

class TestExamples(TestCase):

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('advent_of_code.year_2022.day_04.part_1.get_input', side_effect=mocked_get_input))
        cls.enterClassContext(
            patch('advent_of_code.year_2022.day_04.part_2.get_input', side_effect=mocked_get_input))

        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        n_overlapping = part_1.main()
        self.assertEqual(n_overlapping, 2)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        n_overlapping = part_2.main()
        self.assertEqual(n_overlapping, 4)

if __name__ == "__main__":
    unittest.main()
import unittest

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch

from advent_of_code.year_2023.day_02 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n"

class TestExamples(TestCase):

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('advent_of_code.year_2023.day_02.part_1.get_input', side_effect=mocked_get_input))
        cls.enterClassContext(
            patch('advent_of_code.year_2023.day_02.part_2.get_input', side_effect=mocked_get_input))

        super().setUpClass()

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        calories = part_1.main()
        self.assertEqual(calories, 8)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        calories = part_2.main()
        self.assertEqual(calories, 2286)

if __name__ == "__main__":
    unittest.main()
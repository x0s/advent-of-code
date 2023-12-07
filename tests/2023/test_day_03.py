import unittest

from contextlib import contextmanager
from tests.utils import TestExamplesMain

from advent_of_code.year_2023.day_03 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..\n"

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2023, 3, mocked_get_input)
        #super().patchGetInput(2023, 3, 1, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 4361)

    def test_drop_line(self):
        Coord, Item = part_1.Coord, part_1.Item
        heap_fixture = {
            Coord(0, 1, 4): Item("555"),
            Coord(1, 7, 8): Item("#"),
            Coord(1, 9, 10): Item("*"),
            Coord(8, 2, 7): Item("12345")}
        
        self.assertEqual(part_1.
            drop_line(heap_fixture, 8), {Coord(8, 2, 7): Item("12345")})



    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 467835)

if __name__ == "__main__":
    unittest.main()
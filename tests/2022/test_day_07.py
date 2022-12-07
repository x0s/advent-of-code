import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_07 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k\n"

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 7, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 95437)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 24933642)
    
    def test_max_capped_sum(self):
        sizes = [94_853, 584, 10_000]
        self.assertEqual(part_1.SolutionOne.max_capped_sum(sizes, ceiling=100_000), 95437)

if __name__ == "__main__":
    unittest.main()
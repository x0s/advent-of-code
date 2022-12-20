import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_18 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield '1,1,1\n2,1,1\n3,1,1\n4,1,1\n5,1,1\n6,1,1\n1,2,1\n2,2,1\n4,2,1\n5,2,1\n6,2,1\n1,3,1\n2,3,1\n3,3,1\n4,3,1\n5,3,1\n6,3,1\n1,4,1\n2,4,1\n3,4,1\n4,4,1\n5,4,1\n6,4,1\n1,1,2\n2,1,2\n3,1,2\n4,1,2\n5,1,2\n6,1,2\n1,2,2\n6,2,2\n1,3,2\n6,3,2\n1,4,2\n2,4,2\n3,4,2\n4,4,2\n5,4,2\n6,4,2\n1,1,3\n2,1,3\n3,1,3\n4,1,3\n5,1,3\n6,1,3\n1,2,3\n2,2,3\n3,2,3\n4,2,3\n5,2,3\n6,2,3\n1,3,3\n2,3,3\n3,3,3\n4,3,3\n5,3,3\n6,3,3\n1,4,3\n2,4,3\n3,4,3\n4,4,3\n5,4,3\n6,4,3\n1,1,4\n2,1,4\n3,1,4\n4,1,4\n5,1,4\n6,1,4\n1,2,4\n6,2,4\n1,3,4\n6,3,4\n1,4,4\n2,4,4\n3,4,4\n4,4,4\n5,4,4\n6,4,4\n1,1,5\n2,1,5\n3,1,5\n4,1,5\n5,1,5\n6,1,5\n1,2,5\n2,2,5\n3,2,5\n4,2,5\n5,2,5\n6,2,5\n1,3,5\n2,3,5\n3,3,5\n4,3,5\n5,3,5\n6,3,5\n1,4,5\n2,4,5\n3,4,5\n4,4,5\n5,4,5\n6,4,5'

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 18, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 206)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 178)

if __name__ == "__main__":
    unittest.main()
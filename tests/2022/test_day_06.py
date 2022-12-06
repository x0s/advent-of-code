import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_06 import (part_1,
                                             part_2)

BUFFERS = [ ("mjqjpqmgbljsphdztnvjfqwrcgsmlb",     7, 19) ,
            ("bvwbjplbgvbhsrlpgdmjqwftvncz",       5, 23),
            ("nppdvjthqldpwncqszvftbrmjlhg",       6, 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",  11, 26)]


@contextmanager
def mocked_get_input(year, day):
    yield BUFFERS[0][0]

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 6, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), BUFFERS[0][1])

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), BUFFERS[0][2])

    def test_get_marker_index(self):
        for buffer, idx_packet, idx_msg in BUFFERS:
            self.assertEqual(part_1.SolutionOne.get_marker_index(buffer, 4), idx_packet)
            self.assertEqual(part_1.SolutionOne.get_marker_index(buffer, 14), idx_msg)

if __name__ == "__main__":
    unittest.main()
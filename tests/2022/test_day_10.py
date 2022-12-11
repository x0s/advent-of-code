import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.helpers import logging_level
from advent_of_code.logging import log
from advent_of_code.year_2022.day_10 import (part_1,
                                             part_2)


@contextmanager
def mocked_get_input(year, day):
    yield "addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop"

OUTPUT = """████....████....████....████....████....████....████....████....████....████....
██████......██████......██████......██████......██████......██████......██████..
████████........████████........████████........████████........████████........
██████████..........██████████..........██████████..........██████████..........
████████████............████████████............████████████............████████
██████████████..............██████████████..............██████████████.........."""


class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 10, mocked_get_input)
        cls.maxDiff = None

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 13140)

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        #logging.disable(logging.DEBUG)
        with logging_level('debug'):
            with self.assertLogs('app') as cm:
                part_2.main()
            self.assertEqual(cm.output, [f'INFO:app:{out}' for out in OUTPUT.split('\n')])

if __name__ == "__main__":
    unittest.main()
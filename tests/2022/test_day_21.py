import operator
import unittest
from contextlib import contextmanager

from tests.utils import TestExamplesMain
from advent_of_code.year_2022.day_21 import (part_1,
                                             part_2,)


@contextmanager
def mocked_get_input(year, day):
    yield """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

class TestExamples(TestExamplesMain):

    @classmethod
    def setUpClass(cls):
        super().setUpClassAndPatch(2022, 21, mocked_get_input)

    def test_part1(self):
        """Test if example from part 1 problem statement works"""
        self.assertEqual(part_1.main(), 152)

    def test_read_operation(self):
        self.assertEqual(part_1.SolutionOne.
            read_operation("drzm * dbpl"), (operator.mul, ("drzm", "dbpl")))

        self.assertEqual(part_1.SolutionOne.
            read_operation("doug + dagg"), (operator.add, ("doug", "dagg")))

        self.assertEqual(part_1.SolutionOne.
            read_operation("bull - dogg"), (operator.sub, ("bull", "dogg")))

        self.assertEqual(part_1.SolutionOne.
            read_operation("glue / niak"), (operator.truediv, ("glue", "niak")))

        self.assertRaises(part_1.OperationNotFound,
            part_1.SolutionOne.read_operation, "monk ** kkey")

    def test_part2(self):
        """Test if example from part 2 problem statement works"""
        self.assertEqual(part_2.main(), 301)

    def test_inverse_operation(self):
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "X + beta",  from_the_right=False),
                             ("X"    , "gamma - beta"))
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "alpha + X", from_the_right=True),
                             ("X"    , "gamma - alpha"))
        
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "X - beta",  from_the_right=False),
                             ("X"    , "beta + gamma"))
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "alpha - X", from_the_right=True),
                             ("X"    , "alpha - gamma"))

        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "X / beta",  from_the_right=False),
                             ("X"    , "beta * gamma"))
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "alpha / X",  from_the_right=True),
                             ("X"    , "alpha / gamma"))
        
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "X * beta",  from_the_right=False),
                             ("X"    , "gamma / beta"))
        self.assertEqual(part_2.SolutionTwo.
            inverse_operation("gamma", "alpha * X", from_the_right=True),
                             ("X"    , "gamma / alpha"))

        self.assertRaises(part_1.OperationNotFound,
            part_2.SolutionTwo.inverse_operation, "gamma", "alpha ** X", from_the_right=True)

if __name__ == "__main__":
    unittest.main()
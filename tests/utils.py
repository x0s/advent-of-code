from unittest import TestCase
from unittest.mock import patch

class TestExamplesMain(TestCase):
    
    @classmethod
    def setUpClassAndPatch(cls, year, day, mocked_get_input):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch(f'advent_of_code.year_{year}.day_{day:02}.part_1.get_input', side_effect=mocked_get_input))
        cls.enterClassContext(
            patch(f'advent_of_code.year_{year}.day_{day:02}.part_2.get_input', side_effect=mocked_get_input))

        super().setUpClass()
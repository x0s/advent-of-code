from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import patch, mock_open

from advent_of_code.config import (get_token,
                                   get_input)


# inspired from https://stackoverflow.com/a/28507806/3581903
@contextmanager
def mocked_requests_get(url, *args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    if url == 'https://adventofcode.com/2021/day/13/input':
        raw_text_fixture = "forward 5\ndown 5\nforward 8\nup 3"
        yield MockResponse(raw_text_fixture, 200)


class TestExamples(TestCase):

    config_token_fixture = "ru=2315512c2123c3312q351c56q2; session=5654512c785c21b"
    config_toml_fixture = f"""token = \"{config_token_fixture}\"""".encode('utf-8') # should be binary

    @classmethod
    def setUpClass(cls):
        
        # We set up the same fixture input for all test case(part 1 and 2), py>=3.11
        cls.enterClassContext(
            patch('builtins.open', mock_open(read_data=cls.config_toml_fixture)))
        cls.enterClassContext(
            patch('advent_of_code.config.requests.get', side_effect=mocked_requests_get))

        super().setUpClass()

    def test_get_token(self):
        """Test if token is correctly retrieved from TOML config file"""
        self.assertEqual(get_token(), self.config_token_fixture)
    
    def test_get_input(self):
        """Test if token is correctly retrieved from TOML config file"""

        with get_input(year=2021, day=13) as raw_text:
            self.assertEqual(raw_text, "forward 5\ndown 5\nforward 8\nup 3")
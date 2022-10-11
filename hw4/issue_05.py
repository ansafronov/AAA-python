from unittest.mock import patch
import pytest
from what_is_year_now import what_is_year_now

response_1 = '{"$id":"1","currentDateTime":"2010-10-11T16:12Z","utcOffset":"00:00:00","isDayLightSavingsTime":false,"dayOfTheWeek":"Tuesday","timeZoneName":"UTC","currentFileTime":133099783601886629,"ordinalDate":"2010-284","serviceResponse":null} '
response_2 = '{"currentDateTime":"01.03.2010"}'
response_3 = '{"currentDateTime":"2010 10 11T16:12Z"}'


def test_get_year_dashs():
    with patch('what_is_year_now.urllib.request.urlopen') as mocked_get_cases:
        with open('mock_files/file_mock_1.txt', 'w') as f:
            f.write(response_1)
        with open('mock_files/file_mock_1.txt', 'r') as f:
            mocked_get_cases.return_value.__enter__ = lambda _: f
            assert what_is_year_now() == 2010
            mocked_get_cases.assert_called_once()


def test_get_year_dots():
    with patch('what_is_year_now.urllib.request.urlopen') as mocked_get_cases:
        with open('mock_files/file_mock_2.txt', 'w') as f:
            f.write(response_2)
        with open('mock_files/file_mock_2.txt', 'r') as f:
            mocked_get_cases.return_value.__enter__ = lambda _: f
            assert what_is_year_now() == 2010
            mocked_get_cases.assert_called_once()


def test_get_year_space():
    with patch('what_is_year_now.urllib.request.urlopen') as mocked_get_cases:
        with open('mock_files/file_mock_3.txt', 'w') as f:
            f.write(response_3)
        with open('mock_files/file_mock_3.txt', 'r') as f:
            mocked_get_cases.return_value.__enter__ = lambda _: f
            with pytest.raises(ValueError) as e:
                what_is_year_now()
            mocked_get_cases.assert_called_once()

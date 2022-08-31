import pytest
from mock import patch, mock_open

from src.core.util import *
from tests.dataprovider.data import FILE_DATA


class TestGetLimitedGeneratorCopies(object):
    @patch("builtins.open", new_callable=mock_open, read_data=FILE_DATA)
    def test_get_limited_generator_and_copies_ok(mocker, mock_open):
        result1, result2, result3 = get_limited_generator(
            path="/file_path.txt", limit=5, copies=3
        )
        assert result1 is not None and result2 is not None and result3 is not None
        assert len(list(result1)) == 5

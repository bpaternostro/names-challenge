import pytest
import types
from mock import mock_open, patch
from src.core.util import *
from src.exceptions.util_ex import *

file_path = "data/any.txt"  # filename to be processed


class TestGetNameGenerator(object):
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_get_names_generator_ok(mocker, mock_file):
        assert isinstance(get_names_generator(path=file_path), types.GeneratorType)

    def test_get_names_generator_not_ok(mocker):
        with pytest.raises(Exception):
            assert isinstance(
                get_names_generator(path="wrong_file.png"), InvalidExtensionFile
            )

    def test_get_names_generator_file_is_open_not_ok(mocker):
        with pytest.raises(Exception):
            file_to_process = open(file_path, "r")
            assert isinstance(get_names_generator(path=file_path), FileIsOpen)
            file_to_process.close()

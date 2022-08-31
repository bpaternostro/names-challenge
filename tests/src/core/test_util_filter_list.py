import pytest
import types
from mock import MagicMock

from src.core.util import *
from tests.dataprovider.data import FILE_DATA,LIST_DICT_DATA,ITEMS_EX

class TestFilterList(object):
    def test_filter_list_ok(mocker):
        mock_foo = MagicMock()
        mock_foo.iter.return_value.__iter__.return_value = iter(LIST_DICT_DATA)
        assert isinstance(filter_list(list(mock_foo.iter())), list)

    def test_filter_list_not_ok_ex(mocker):
        mock_foo = MagicMock()
        mock_foo.iter.return_value.__iter__.return_value = iter(ITEMS_EX)
        with pytest.raises(Exception):
            assert isinstance(filter_list(mock_foo.iter()), FilterListException)

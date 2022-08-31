import pytest
import types
from mock import MagicMock

from src.core.util import *

items = [
    {"last_name": "Unit", "name": "Test", "full_name": "Unit, Test"},
    {"last_name": "Jones", "name": "Indiana", "full_name": "Jones, Indiana"},
]
items_ex = [
    {"other": "Unit", "name": "Test", "full_name": "Unit, Test"},
    {"last_name": "Jones", "name": "Indiana", "full_name": "Jones, Indiana"},
]


class TestMixPersonsName(object):
    def test_mix_person_names_ok(mocker):
        mock_foo = MagicMock()
        mock_foo.iter.return_value.__iter__.return_value = iter(items)
        *_, last = mock_foo.iter()
        assert isinstance(
            mix_person_names(person_list=mock_foo.iter(), last_name=last["name"]),
            types.GeneratorType,
        )

    def test_mix_person_names_not_ok_ex(mocker):
        mock_foo = MagicMock()
        mock_foo.iter.return_value.__iter__.return_value = iter(items_ex)
        with pytest.raises(Exception):
            assert isinstance(filter_list(mock_foo.iter()), SwapingDictonaryArray)

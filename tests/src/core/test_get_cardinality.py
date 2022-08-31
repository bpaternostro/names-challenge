import pytest
from mock import patch, mock_open

from src.core.util import *
from tests.dataprovider.data import FILE_DATA,LIST_DICT_DATA,ITEMS_EX,LIST_DICT_DATA_IRREGULAR

class TestGetCardinality(object):
    def test_get_cardinality_counters_happy_path_ok(mocker):
        result = get_cardinality(
            persons=LIST_DICT_DATA
        )
        assert len(result["full_names"]) == 25
        assert len(result["last_names"]) == 24
        assert len(result["names"]) == 25
        assert result["distincts"][0][1] == 25
        assert result["distincts"][1][1] == 24
        assert result["distincts"][2][1] == 25
    
    def test_get_cardinality_types_ok(mocker):
        result = get_cardinality(
            persons=LIST_DICT_DATA
        )
        assert isinstance(result,dict)
        assert isinstance(result["distincts"],list)
        assert isinstance(result["distincts"][0],tuple)
        assert isinstance(result["distincts"][1],tuple)
        assert isinstance(result["distincts"][2],tuple)
        assert isinstance(result["full_names"],list)
        assert isinstance(result["last_names"],list)
        assert isinstance(result["names"],list)

    def test_get_cardinality_counters_irregular_path_ok(mocker):
        result = get_cardinality(
            persons=LIST_DICT_DATA_IRREGULAR
        )
        assert len(result["full_names"]) == 2
        assert len(result["last_names"]) == 2
        assert len(result["names"]) == 2
        assert result["distincts"][0][1] == 2
        assert result["distincts"][1][1] == 2
        assert result["distincts"][2][1] == 2

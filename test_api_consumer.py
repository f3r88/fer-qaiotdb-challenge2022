import pytest
import responses
from task1_api_consumer_function import character_info_extractor


def test_valid_character():
    result = character_info_extractor("Pickle Rick")
    assert "Character info" in result
    assert "species" in result["Character info"]
    assert "type" in result["Character info"]
    assert "Location info" in result
    assert "name" in result["Location info"]
    assert "type" in result["Location info"]
    assert "dimension" in result["Location info"]
    assert "residents" in result["Location info"]
    assert "Episode info" in result
    for episode in result["Episode info"]:
        assert "episode_name" in episode
        assert "episode_id" in episode
        assert "characters_count" in episode


def test_character_not_found():
    result = character_info_extractor("Goku")
    assert result is None


def test_character_with_blank_spaces():
    result = character_info_extractor("Jerry    Smith")
    assert result is None


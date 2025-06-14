from utils import clean_text
import pytest

def test_clean_text_basic():
    assert clean_text("  Hello ") == "hello"

def test_clean_text_invalid():
    with pytest.raises(ValueError):
        clean_text(123)

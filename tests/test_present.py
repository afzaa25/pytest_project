import pytest
from lib.present import *

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap() # <-- New code
    message = str(e.value)
    assert message == "No contents have been wrapped."

def test_wrapping_when_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."
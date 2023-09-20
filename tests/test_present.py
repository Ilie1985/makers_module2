import pytest
from lib.present import *


def test_wrap_and_unwrap():
    present=Present()
    present.wrap(22)
    assert present.unwrap()==22

def test_if_present_unwrap_without_wrapping():
    present=Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message =str(e.value)
    assert message =="No contents have been wrapped."

def test_if_present_already_wrapped():
    present=Present()
    present.wrap(33)
    with pytest.raises(Exception) as e:
        present.wrap(44)
    message=str(e.value)
    assert message == "A contents has already been wrapped."
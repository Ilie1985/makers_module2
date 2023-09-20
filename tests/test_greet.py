from lib.greet import *

def test_greet_returns_greet_with_name():
    result= greet("Marian")
    assert result== "Hello, Marian!"
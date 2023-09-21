from lib.challenge_four_ex_one import *

def test_return_greeting_plus_name():
    result=say_hello("kay")
    assert result== "hello kay"
from lib.check_codeword import *

def test_if_codeword_is_horse():
    result =check_codeword("horse")
    assert result =="Correct! Come in."


def test_if_codeword_is_wrong():
    result =check_codeword("some_word")
    assert result == "WRONG!"

def test_if_first_letter_h_last_letter_e():
    result= check_codeword("hope")
    assert result == "Close, but nope."
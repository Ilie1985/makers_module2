from lib.count_words import count_words
from lib.count_words import return_str




# given a string return string
def test_count_words_returns_string_if_string():
    result= return_str("hello")
    assert result == "hello"

# returns the number of words within the string
def test_count_words_returns_number_of_words_in_string():
    result=count_words("one two three four five")
    assert result==5

from lib.text_tracker import *


# 3. Create Examples as Tests
# Make a list of examples of what the function will take and return.

# return a string if specials string exists
def test_if_special_string_in_text():
    result=find_special_string_in_text("text with special string"," special string")
    assert result== True


# return a text without special special string
def test_text_without_special_string():
    result= find_special_string_in_text("text without special string", "not a special string")
    assert result == False

# return false if empty string
def test_text_with_empty_string():
    result=find_special_string_in_text("","text with empty string")
    assert result== False

# return true if text without special string and text
def test_text_without_special_string_and_text():
    result = find_special_string_in_text(" "," ")
    assert result == True

from lib.string_builder import *

def test_concatenate_strings():
    string_builder=StringBuilder()
    string_builder.add("string")
    assert string_builder.output()=="string"
from lib.challenge_five import *




def test_check_method_with_valid_text():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("This is a valid sentence.") == True

def test_check_method_with_invalid_text():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Invalid text") == False

def test_percentage_good_method_with_no_checks():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good() == 0

def test_percentage_good_method_with_checks():
    grammar_stats = GrammarStats()
    grammar_stats.check("This is a valid sentence.")
    grammar_stats.check("Invalid text")
    assert grammar_stats.percentage_good() == 50.0  # 1 out of 2 checks passed



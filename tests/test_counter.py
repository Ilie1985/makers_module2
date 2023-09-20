from lib.counter import *


def test_count_to_a_certain_number():
    counter= Counter()
    counter.add(1)
    
    assert counter.report() == "Counted to 1 so far."
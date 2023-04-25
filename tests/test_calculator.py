from lib.calculator import *

def tests_adds_two_numbers_returns_seven():
    result = add_up(2,5)
    assert result == 7

def tests_adds_two_numbers_returns_five():
    result = add_up(2,3)
    assert result == 5
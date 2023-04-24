from lib.greet import *
def test_greeting():
    result = greet("Afzaa")
    assert result == "Hello Afzaa!"
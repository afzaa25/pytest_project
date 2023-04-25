import pytest
from lib.password_checker import *

def test_check_if_password_is_valid():
    password_checker = PasswordChecker()
    password_checker.check("afzaaaaa")
    with pytest.raises(Exception) as e:
        password_checker.check("afzaa")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."
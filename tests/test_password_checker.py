import pytest
from lib.password_checker import *

# check the length of the password and return True
def test_password_length():
    password_checker=PasswordChecker()
    assert password_checker.check("qwertyoup") is True

# if password is to short return invlid
def test_passsword_too_short():
    password_checker=PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("qwerty")
    message =str(e.value)
    assert message == "Invalid password, must be 8+ characters."
        
# if password input is empty return invalid
def test_password_input_empty():
    password_checker=PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("")
    assert str(e.value) == "Invalid password, must be 8+ characters."


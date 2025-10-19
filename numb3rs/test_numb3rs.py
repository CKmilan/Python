# This is an automated test using pytest test_numb3rs.py


from numb3rs import validate
import pytest

def main():
    test_validator_nums()
    test_validator_any()
    test_validator_length()

def test_validator_nums():
    assert validate("1.132.44.228") == True
    assert validate("22.12.46.274") == False
    assert validate("275.3.6.28") == False

def test_validator_any():
    assert validate("asd.123.%=,.edx") == False
    assert validate("qwe.xyz.asd.fgb") == False

def test_validator_length():
    assert validate("1234.244.12.20") == False
    assert validate("123.244.12.20") == True

if __name__ == "__main__":
    main()

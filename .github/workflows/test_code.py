import pytest

def test_positive_number():
    num = 10
    if num > 0:
        assert True
    else:
        assert False

def test_prime_check():
    num = 10
    is_prime = True
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    assert not is_prime  # 10 is not a prime number

def test_string_length():
    name = "Hrithik"
    assert len(name) == 7

def test_greeting():
    name = "Hrithik"
    greeting = "hello" + name
    assert greeting == "helloHrithik"

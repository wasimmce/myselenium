import pytest

@pytest.mark.random
def test_demo():
    print("Demostrating test cases")

@pytest.mark.alphabets
def test_a():
    print("a")

@pytest.mark.alphabets
def test_b():
    print("b")

@pytest.mark.alphabets
def test_c():
    print("c")

@pytest.mark.alphabets
def test_d():
    print("d")
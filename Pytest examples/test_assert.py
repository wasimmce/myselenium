#assert = actual result != expected result false + asseration error
import pytest


def add(a, b):
    return a+b

@pytest.mark.parametrize("a,b,output", [(5,6,11),(96,11,107),(9,2,10)])
def test_calculate(a, b, output):
    result = add(a, b)
    print(result)
    assert output == result

# def test_add():
#     #a = 10, b=35
#     result = add(10,50)
#     print(result)
#     assert 60==result
#
#     result = add(20, 50)
#     print(result)
#     assert 60 == result
#
#     result = add(15, 50)
#     print(result)
#     assert 60 == result

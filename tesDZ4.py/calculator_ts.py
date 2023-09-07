import pytest
from calculator import Calculator

calculator = Calculator()
#@pytest.mark.xfail
#@pytest.mark.skip()

@pytest.mark.parametrize('a, b, result', [ (4,5,9), (-2,-4, -6), (-6, 6, 0), (3.51, 3.49, 7)])

def test_sum_positive(a, b, result):
    calculator = Calculator()
    res = calculator.sum(a, b)
    assert res == result

def test_sub_positive():
    calculator = Calculator()
    res = calculator.sub(10, 4)
    assert res == 6

def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

def test_mul_positive():
    calculator = Calculator()
    res = calculator.mul(2, 3)
    assert res == 6
    
@pytest.mark.parametrize('nums, result', [([], 0), ([1,2,3,4,5,6,7,8,9,5], 5)])
def test_avg_enply(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result


#print("start")
#res = calculator.sum(4, 5)
#assert res == 9

#res = calculator.sum(-6, -10)
#assert res ==-16

#res = calculator.sum(-6, 6)
#assert res == 0

#res = calculator.sum(5.6, 4.3)
#res = round(res, 1)
#assert res == 9.9

#res = calculator.sum(10, 0)
#assert res == 10

res = calculator.div(10, 2)
assert res == 5

numbers = []
res = calculator.avg(numbers)
assert res == 0

#mumbers = [1,2,3,4,5,6,7,8,9,5]
#res = calculator.div(10, 0)
#assert res == None

print("finish")
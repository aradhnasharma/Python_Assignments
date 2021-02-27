from exponent import exponent
import pytest

@pytest.mark.parametrize(
    "element1,element2,expected",
    [
        (2,5,32),
        (5,5 ,3125),
		(2,0,1),
    ]
)
def test_exponent_elements(element1, element2, expected):
    assert exponent(element1, element2) == expected

def test_negative_assert():
    assert exponent(2,3) != 10
	
	
@pytest.mark.skip(reason="We don't want to test this")
def test_zero_exp():
    with pytest.raises(ValueError):
        0**2
		

@pytest.mark.skipif(True, reason = "Skipping in Condition")
def test_exp_fail():
    assert exponent(0,0) ==2

@pytest.mark.xfail
def test_failing_condition():
    assert exponent(-2,-5) == -10
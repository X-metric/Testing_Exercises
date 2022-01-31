import pytest
from Exercise2_Purchase_Discount import calculate_discount
from pytest import approx

def test_expected_nonmember1():
    assert calculate_discount(1,False) == 0
    assert calculate_discount(2,False) == 0
def test_expected_nonmember2():
    assert calculate_discount(3,False) == 1/4
def test_expected_nonmember3():
    assert calculate_discount(4,False) == approx(1/3)
    assert calculate_discount(5,False) == approx(1/3)
def test_expected_nonmember4():
    assert calculate_discount(6,False) == 1/2
    assert calculate_discount(7,False) == 1/2
    assert calculate_discount(8,False) == 1/2
    assert calculate_discount(9,False) == 1/2
    assert calculate_discount(10,False) == 1/2
def test_expected_nonmember5():
    with pytest.raises(ValueError) as error_message:
        calculate_discount(-1,False)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(0,False)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(11,False)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(10**10,False)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount("a",False)
    assert str(error_message.value) == "amount must be an int"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(1/2,False)
    assert str(error_message.value) == "amount must be an int"
    assert error_message.type == ValueError
# -------------------------------------------------------------

def test_expected_member1():
    assert calculate_discount(1,True) == approx(1/5)
    assert calculate_discount(2,True) == approx(0.2)
def test_expected_member2():
    assert calculate_discount(3,True) == approx(1/4 + 1/5 - (1/4 * 1/5))
def test_expected_member3():
    assert calculate_discount(4,True) == approx(1/3 + 1/5 - (1/3 * 1/5),rel=1e-2)
    assert calculate_discount(5,True) == approx(0.33 + 0.2 - (0.33 * 0.2),rel=1e-2)
def test_expected_member4():
    assert calculate_discount(6,True) == approx(1/2 + 1/5 - (1/2 * 1/5))
    assert calculate_discount(7,True) == approx(0.5 + 0.2 - (0.5 * 0.2))
    assert calculate_discount(8,True) == approx(0.5 + 0.2 - (0.5 * 0.2))
    assert calculate_discount(9,True) == approx(0.5 + 0.2 - (0.5 * 0.2))
    assert calculate_discount(10,True) == approx(0.5 + 0.2 - (0.5 * 0.2))
def test_expected_member5():
    with pytest.raises(ValueError) as error_message:
        calculate_discount(-1,True)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(0,True)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(11,True)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(10**10,True)
    assert str(error_message.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount("a",True)
    assert str(error_message.value) == "amount must be an int"
    assert error_message.type == ValueError
    with pytest.raises(ValueError) as error_message:
        calculate_discount(1/2,True)
    assert str(error_message.value) == "amount must be an int"
    assert error_message.type == ValueError

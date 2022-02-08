from chocolate_implementation import calculate_price, _truncate
from decimal import Decimal
from datetime import date
import pytest

def test_valid1():
# Arrange
# Act
    value = Decimal(0.00*0.95)
# Assert
    assert calculate_price(Decimal(0.00), date(2022,4,9)) == _truncate(value)

def test_valid2():
# Arrange
# Act
    value = Decimal(50.00*0.95)
# Assert
    assert calculate_price(Decimal(50.00), date(2022,4,18)) == _truncate(value)

def test_valid3():
# Arrange
# Act
    value = Decimal(50.01*0.90)
# Assert
    assert calculate_price(Decimal(50.01), date(2022,4,10)) == _truncate(value)

def test_valid4():
# Arrange
# Act
    value = Decimal(100.00*0.90)
# Assert
    assert calculate_price(Decimal(100.00), date(2022,4,17)) == _truncate(value)

def test_valid5():
# Arrange
# Act
    value = Decimal(85.01)
# Assert
    assert calculate_price(Decimal(100.01), date(2022,4,18)) == _truncate(value)

def test_valid6():
# Arrange
# Act
    value = Decimal(100.02*0.85)
# Assert
    assert calculate_price(Decimal(100.02), date(2022,4,10)) == _truncate(value)

def test_valid7():
# Arrange
# Act
    value = Decimal(200.00*1.00)
# Assert
    assert calculate_price(Decimal(200.00), date(2022,4,8)) == _truncate(value)

def test_valid8():
# Arrange
# Act
    value = Decimal(49.99*1.00)
# Assert
    assert calculate_price(Decimal(49.99), date(2022,4,19)) == _truncate(value)

def test_valid9():
# Arrange
# Act
    value = Decimal(850.00*0.85)
# Assert
    assert calculate_price(Decimal(850.00), date(2022,4,17)) == _truncate(value)

def test_valid10():
# Arrange
# Act
    value = Decimal(1000.00*0.85)
# Assert
    assert calculate_price(Decimal(1000.00), date(2022,4,16)) == _truncate(value)
# -------------------------------------------------------------------------------

def test_invalid11():
# Arrange
# Act
    with pytest.raises(ValueError) as error_message:
        calculate_price(Decimal(-0.01), date(2022, 4, 9))
# Assert
    assert error_message.type == ValueError

def test_invalid12():
# Arrange
# Act
    with pytest.raises(ValueError) as error_message:
        calculate_price(Decimal(0.00), "a")
# Assert
    assert error_message.type == ValueError

def test_invalid13():
# Arrange
# Act
    with pytest.raises(ValueError) as error_message:
        calculate_price("a", date(2022,4,9))
# Assert
    assert error_message.type == ValueError

def test_invalid14():
# Arrange
# Act
    with pytest.raises(TypeError) as error_message:
        calculate_price(Decimal(0.00), date(True))
# Assert
    assert error_message.type == TypeError

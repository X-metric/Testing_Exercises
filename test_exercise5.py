from exercise5_dummy import dummy_implementation
from decimal import Decimal
from datetime import date
import pytest

def test_expected1():
# Arrange
# Act
# Assert
    assert dummy_implementation(Decimal(0.00), date(2022,4,9)) == 0.05

def test_expected2():
# Arrange
# Act
# Assert
    assert dummy_implementation(Decimal(50.00), date(2022,4,18)) == 0.05

def test_expected3():
# Arrange
# Act
# Assert
    assert dummy_implementation(Decimal(50.01), date(2022,4,10)) == 0.10

def test_expected4():
# Arrange
# Act
# Assert
    assert dummy_implementation(Decimal(100.00), date(2022,4,17)) == 0.10

def test_expected5():
# Arrange
# Act
# Assert
    assert dummy_implementation(Decimal(100.01), date(2022,4,18)) == 0.15

def test_error1():
# Arrange
# Act
    with pytest.raises(ValueError) as error_message:
        dummy_implementation(Decimal(-0.01), date(2022, 4, 9))
# Assert
    assert error_message.type == ValueError

def test_error2():
# Arrange
# Act
    with pytest.raises(ValueError) as error_message:
        dummy_implementation(Decimal(0.00), date("a"))
# Assert
    assert error_message.type == ValueError

def test_error3():
# Arrange
# Act
    with pytest.raises(ValueError) as error_message:
        dummy_implementation(Decimal(50.01), date(2022, 4, 0))
# Assert
    assert error_message.type == ValueError

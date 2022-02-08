from exercise9_10 import bubble_sort
import pytest

_test_data_for_valid_lists = [
    pytest.param( [ 8 ], [ 8 ], id="1 - Liste mit nur einem Wert "),
    pytest.param( [ 1, 0 ], [ 0, 1 ], id="2 - einfache Liste mit zwei 'integer' Werten" ),
    pytest.param( [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ], [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], id="3 - einfache Liste mit mehreren 'integer' Werten"),
    pytest.param( [ "z" ], [ "z" ], id="4 - einfache Liste mit einem 'string' Wert "),
    pytest.param( [ "b", "a" ], [ "a", "b" ], id="4 - einfache Liste mit 'string' Werten"),
    pytest.param( [ "f", "e", "d", "c", "b", "a" ], [ "a", "b", "c", "d", "e", "f" ], id="5 - einfache Liste mit mehreren 'string' Werten" ),
    pytest.param( [ 14.01218, 0.01, 18.7, 178,666, 3], [ 0.01, 3, 14.01218, 18.7, 178,666], id="6 - einfache Liste mit Decimal, Float und Integer Werten" ),
    pytest.param( [ -5, -38, 189 ], [ -38, -5, 189 ], id="7 - einfache Liste mit negativen Zahlen" ),
    pytest.param( [ 1, 2, 3 ], [ 1, 2, 3 ], id="8 - einfache Liste die bereits geordnet ist" ),
    pytest.param( [], [], id="9 - einfache Listen - sind aber leer!" ),
]

_test_data_for_invalid_lists = [
    pytest.param( [ 3, 2, 1, "c", "b", "a" ], id="10 - Liste mit integer und strings" ),
    pytest.param( [ True, False ], id="11 - Liste mit Booleans!" ),
    pytest.param( ( 3, 2, 1 ), id="12 - tuples!"),
    pytest.param( {3,2,1}, id="13 - Set")
]

@pytest.mark.parametrize("testinglist, orderedlist", _test_data_for_valid_lists)
def test_valid_lists( testinglist, orderedlist ):
    # Arrange
    # Act
    value = bubble_sort(testinglist)
    # Assert
    assert value == orderedlist

@pytest.mark.parametrize("testinglist", _test_data_for_invalid_lists)
def test_invalid_lists( testinglist ):
    # Arrange
    # Act
    # Assert
    with pytest.raises(ValueError):
        bubble_sort(testinglist)
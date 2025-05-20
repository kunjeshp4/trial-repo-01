import pytest

from add import add as simple_add
from subtract import subtract as simple_subtract
from naked_math import add as naked_add, subtract as naked_subtract, multiply, div, exponential


def test_simple_add():
    assert simple_add(2, 3) == 5
    assert simple_add(-1, 1) == 0


def test_simple_subtract():
    assert simple_subtract(5, 3) == 2
    assert simple_subtract(0, -1) == 1


def test_naked_add():
    assert naked_add(1, 2, 3) == 6
    assert naked_add(5) == 5


def test_naked_subtract():
    assert naked_subtract(10, 5, 2) == 3
    assert naked_subtract(5) == 5


def test_multiply():
    assert multiply(2, 3, 4) == 24
    assert multiply(5) == 5


def test_div():
    assert div(100, 2, 5) == 10
    assert div(10) == 10
    with pytest.raises(ValueError):
        div()


def test_exponential():
    assert exponential(2, 3) == 8
    assert exponential(2, 3, 2) == 64
    with pytest.raises(ValueError):
        exponential()

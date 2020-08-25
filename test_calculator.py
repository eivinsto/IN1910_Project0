"""
Testing functions from calculator.py
"""

import calculator
from math import factorial,sin,cos
import pytest

eps = 1e-14     #Error limit to account for machine precision

"Testing add function"
def test_add():
    assert calculator.add(1,2)==3

"Testing add function with floats"
def test_add_floats():
    assert abs(calculator.add(0.1,0.2)-0.3)<eps

"Testing add function with strings"
def test_add_strings():
    assert calculator.add("Hello ","World")=="Hello World"

"Testing factorial function from calculator.py"
def test_factorial():
    assert abs(calculator.factorial(6)-factorial(6))<eps

"Testing sin function"
def test_sin():
    assert abs(calculator.sin(2,1000)-sin(2))<eps

"Testing divide function"
def test_divide():
    assert abs(calculator.divide(6,2)-3)<eps

"Testing cos function"
def test_cos():
    assert abs(calculator.cos(2,1000)-cos(2))<eps

"Testing power function"
def test_power():
    assert abs(calculator.power(3,5)-3**5)<eps

"""
Testing whether add raises TypeError exception if two
incompatible types are given as arguments
"""
def test_add_incompatible_types():
    with pytest.raises(TypeError):
        calculator.add("Hello ",2)

"""
Testing whether divide function returns ZeroDivisionError when we give zero as
second argument.
"""
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(2,0)

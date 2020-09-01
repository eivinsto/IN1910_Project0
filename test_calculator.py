"""
Testing functions from calculator.py
"""

import calculator
from math import factorial,sin,cos
import pytest

eps = 1e-14     #Error limit to account for machine precision

"Testing add function"
@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]]
)
def test_add_exercise_1(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output

"Testing add function with floats"
@pytest.mark.parametrize(
    "arg, expected_output", [[(-0.1, -0.1), -0.2], [(0.1, 0.1), 0.2], [(0.1, 0), 0.1]]
)
def test_add_floats_exercise_2(arg,expected_output):
    assert abs(calculator.add(arg[0],arg[1])-expected_output)<eps

"Testing add function with strings"
@pytest.mark.parametrize(
    "arg, expected_output", [[("Hello ","World"), "Hello World"], \
    [("Test ", "Output"), "Test Output"], \
    [("Text and", " more text"), "Text and more text"]]
)
def test_add_strings_exercise_3(arg,expected_output):
    assert calculator.add(arg[0],arg[1])==expected_output

"Testing factorial function from calculator.py"
@pytest.mark.parametrize(
    "arg, expected_output", [[6, factorial(6)], \
    [2, factorial(2)], [5, factorial(5)]]
)
def test_factorial_exercise_4(arg,expected_output):
    assert abs(calculator.factorial(arg)-expected_output)<eps

"Testing sin function"
@pytest.mark.parametrize(
    "arg, expected_output", [[(2,1000), sin(2)], [(3,1000), sin(3)], \
    [(5,1000), sin(5)]]
)
def test_sin_exercise_4(arg,expected_output):
    assert abs(calculator.sin(arg[0],arg[1])-expected_output)<eps

"Testing divide function"
@pytest.mark.parametrize(
    "arg, expected_output", [[(6,2), 3], [(8, 4), 2], [(5,5), 1]]
)
def test_divide_exercise_4(arg,expected_output):
    assert abs(calculator.divide(arg[0],arg[1])-expected_output)<eps

"Testing cos function"
@pytest.mark.parametrize(
    "arg, expected_output", [[(2,1000), cos(2)], [(3, 1000), cos(3)],\
    [(5, 1000), cos(5)]]
)
def test_cos_exercise_4(arg,expected_output):
    assert abs(calculator.cos(2,1000)-cos(2))<eps

"Testing power function"
@pytest.mark.parametrize(
    "arg, expected_output", [[(3,5), 243], [(2, 3), 8], [(0.5,4), 1/16]]
)
def test_power_exercise_4(arg,expected_output):
    assert abs(calculator.power(arg[0],arg[1])-expected_output)<eps

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

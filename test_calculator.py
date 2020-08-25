import calculator

"Testing add function from calculator.py"
def test_add():
    assert calculator.add(1,2)==3

"Testing add function from calculator.py with floats"
def test_add_floats():
    eps = 1e-14     #Error limit to account for machine precision
    assert calculator.add(0.1,0.2)-0.3<eps

"Testing add function from calculator.py with strings"
def test_add_strings():
    assert calculator.add("Hello ","World")=="Hello World"

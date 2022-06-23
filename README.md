# Fractional Math Calculator ![test coverage badge](https://img.shields.io/badge/test%20coverage-96%25-brightgreen) ![tests badge](https://img.shields.io/badge/tests-143%20passed%2C%200%20failed-brightgreen)
A command line program that takes a string of whole and mixed numbers and returns the mathematical result.


# Requirements
Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.

* Legal operators are be *, /, +, - (multiply, divide, add, subtract)

* Operands and operators shall be separated by one or more spaces

* Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"

* Improper fractions and whole numbers are also allowed as operands

Example run:

? 1/2 * 3_3/4

= 1_7/8

? 2_3/8 + 9/8

= 3_1/2

# Setup
* Clone repo
* Run setup.py from Python 3+
```python
python3 setup.py
```
* Install package via symlink for dev code
```
pip install -e .
```

# Run 
```python
python3 main.py
```

# Run Tests 
Tests can be performed two ways.
One:
```
python3 tests/frac_tests.py
```
Two:
* 
Run the script
```
python3 main.py
```
and in the prompt, enter ***tests***
```
# Command Prompt
Enter a command: tests
```

# Future Work 
* Make compatible with parenthesis
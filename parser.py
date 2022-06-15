from operand import Operand
from expression import Expression
from number import Number

class Parser(object):

    def __init__(self, _expression):
        self.expression = _expression
        self.Numbers = []
        self.parse()

    def parse(self):
        for char in self.expression.get_expression_string():
            if char.isnumeric():
                self.Numbers.append(Number(char))

    def get_number_count(self):
        return len(self.Numbers)

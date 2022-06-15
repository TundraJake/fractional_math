from operand import Operand
from expression import Expression
from number import Number

class Parser(object):

    def __init__(self, _expression):
        self.expression = _expression
        self.Numbers = []
        self.parse()

    def parse(self):
        total_exp_len = self.expression.get_length()
        exp_string = self.expression.get_expression()
        number = ''
        for position in range(total_exp_len):
            if exp_string[position].isnumeric():
                number += exp_string[position]
                if len(number) >= 1 and position+1 == total_exp_len:
                    self.Numbers.append(Number(number))
                    number = ''
            position += 1

    def get_number_count(self):
        return len(self.Numbers)

import random
from operators import Operations, Operator
from expression import Expression
from number import Number

class Parser(object):

    def __init__(self, _expression):
        self.expression = _expression
        self.Numbers = []
        self.Operators = []
        self.parse()

    def print_operators(self):
        str = 'Operators: '
        for op in self.Operators:
            str += op.get_operator() + ','
        return str

    def print_numbers(self):
        str = 'Numbers: '
        for num in self.Numbers:
            str += num.get_number() + ','
        return str

    def parse(self):
        total_exp_len = self.expression.get_length()
        exp_string = self.expression.get_expression()
        number_so_far = ''
        position = 0
        is_fraction = False
        div_count = 0 

        while position < total_exp_len:
            # print('this is the char: ', exp_string[position])
            if self.__is_operator(exp_string[position]):
                if exp_string[position] == Operations.SUB and exp_string[position+1] == Operations.SUB and position != 0:
                    self.Operators.append(Operator(Operations.ADD))
                    position += 1
                    number_so_far += exp_string[position]

                elif exp_string[position] == Operations.SUB and exp_string[position+1].isnumeric() and position == 0:
                    number_so_far += exp_string[position]

                elif exp_string[position] == Operations.SUB and exp_string[position+1].isnumeric() and position >= 0:
                    self.Operators.append(Operator(Operations.ADD))
                    number_so_far += exp_string[position]
                    
                else:
                    self.Operators.append(Operator(exp_string[position]))
                position += 1

            if exp_string[position].isnumeric():
                while position < total_exp_len and (exp_string[position].isnumeric() or exp_string[position] == Operations.UNDERSCORE or exp_string[position] == Operations.DIV):
                    if exp_string[position] == Operations.UNDERSCORE:
                        is_fraction = not is_fraction
                    elif exp_string[position] == Operations.DIV:
                        div_count += 1
                    if div_count == 2:
                        div_count = 0
                        break
                    number_so_far += exp_string[position]
                    position += 1


                if div_count > 0:
                    div_count = 0
                self.Numbers.append(Number(number_so_far))
                number_so_far = ''




    def __is_operator(self, char):
        return char in Operations.operators

    def get_number_count(self):
        return len(self.Numbers)

    def get_operator_count(self):
        return len(self.Operators)
    
    def get_number(self, position):
        try:
            return self.Numbers[position].get_number()
        except:
            raise Exception('Array position out of bounds!')
    
    def get_operator(self, position):
        try:
            return self.Operators[position].get_operator()
        except:
            raise Exception('Array position out of bounds!')
    
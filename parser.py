import random
from operators import Operations, Operator
from expression import Expression
from number import Number

class Parser(object):

    def __init__(self, _expression):
        self._expression = _expression
        self._Numbers = []
        self._Operators = []
        self._Elements = []
        self.parse()

    def print_operators(self):
        str = 'Operators: '
        for op in self._Operators:
            str += op.get_operator() + ','
        return str

    def print_numbers(self):
        str = 'Numbers: '
        for num in self._Numbers:
            str += num.get_number() + ','
        return str

    def parse(self):
        total_exp_len = self._expression.get_length()
        exp_string = self._expression.get_expression()
        number_so_far = ''
        position = 0
        is_fraction = False
        div_count = 0 

        while position < total_exp_len:
            if self.__is_operator(exp_string[position]):
                if exp_string[position] == Operations.SUB and exp_string[position+1] == Operations.SUB and position == 0: 
                    position += 1
                    
                elif exp_string[position - 1].isnumeric() and exp_string[position] == Operations.SUB and exp_string[position+1] == Operations.SUB and position != 0:
                    self._Operators.append(Operator(Operations.ADD))
                    self._Elements.append(Operator(Operations.ADD))
                    position += 1

                elif exp_string[position - 1] in Operations.operators and exp_string[position] == Operations.SUB and exp_string[position+1] == Operations.SUB and position != 0:
                    position += 1


                elif exp_string[position] == Operations.SUB and exp_string[position-1] in Operations.operators and position >= 0:
                    number_so_far += exp_string[position]

                elif exp_string[position] == Operations.SUB and exp_string[position+1].isnumeric() and position == 0:
                    number_so_far += exp_string[position]

                elif exp_string[position] == Operations.SUB and exp_string[position+1].isnumeric() and position >= 0:
                    self._Operators.append(Operator(Operations.ADD))
                    self._Elements.append(Operator(Operations.ADD))
                    number_so_far += exp_string[position]
                    
                else:
                    self._Operators.append(Operator(exp_string[position]))
                    self._Elements.append(Operator(exp_string[position]))
                position += 1

            if exp_string[position].isnumeric():
                while position < total_exp_len and (exp_string[position].isnumeric() or exp_string[position] == Operations.UNDERSCORE):
                    if exp_string[position] == Operations.UNDERSCORE:
                        number_so_far += exp_string[position]
                        position += 1
                        is_fraction = not is_fraction
                        while is_fraction and position < total_exp_len:

                            if div_count == 1 and exp_string[position] in Operations.operators:
                                is_fraction = not is_fraction
                                div_count = 0
                                break
                            elif exp_string[position] == Operations.DIV:
                                number_so_far += exp_string[position]
                                position += 1
                                div_count += 1
                            elif exp_string[position].isnumeric():
                                number_so_far += exp_string[position]
                                position += 1
                    else:
                        number_so_far += exp_string[position]
                        position += 1

                self._Numbers.append(Number(number_so_far))
                self._Elements.append(Number(number_so_far))
                number_so_far = ''



    def __is_operator(self, char):
        return char in Operations.operators

    def get_number_count(self):
        return len(self._Numbers)

    def get_operator_count(self):
        return len(self._Operators)
    
    def get_numbers(self):
        return self._Numbers

    def get_element_count(self):
        return len(self.get_elements())

    def get_elements(self):
        return self._Elements

    def get_operators(self):
        return self._Operators

    def get_number(self, position):
        try:
            return self._Numbers[position].get_number()
        except:
            raise Exception('Array position out of bounds!')
    
    def get_operator(self, position):
        try:
            return self._Operators[position].get_operator()
        except:
            raise Exception('Array position out of bounds!')
    
from parser import Parser
from operators import Operations

class ReversePolishNotation(object):

    def __init__(self, parser):
        self._Elements = parser.get_elements()
        self._calculation = 0
        self._stack = []
        self.__calculate()

    def num_length(self):
        return len(self._Numbers)

    def op_length(self):
        return len(self._Operators)

    def get_element_length(self):
        return len(self._Elements)

    def get_stack_values(self):
        str = ''
        for item in self._stack:
            str += item + ', '
        return str

    def get_stack_value(self, position):
        try:
            return self._stack[position].get_value()
        except:
            raise Exception('Out of bounds')

    def __calculate(self):
        for operator in Operations.operators:
            for iter in range(len(self._Elements)):
                if operator == self._Elements[iter].get_value():
                    if  self.get_element_length() != 0:
                        self._stack.append(self._Elements[iter - 1])
                        self._stack.append(self._Elements[iter + 1])
                        self._stack.append(self._Elements[iter])
                        del self._Elements[iter-1:iter+2]
                    elif self.get_element_length() == 2:
                        self._stack.append(self._Elements[0])
                        self._stack.append(self._Elements[1])
                        del self._Elements
                        break
                    if self.get_element_length() == 0:
                        break

        self._calculation = 1
        
    def get_calculation(self):
        return self._calculation
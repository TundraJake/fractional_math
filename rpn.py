from parser import Parser
from tempfile import tempdir
from operators import Operations
import copy

class ReversePolishNotation(object):

    def __init__(self, parser):
        self._Elements = parser.get_elements()
        self._calculation = 0
        self._stack = []
        self.__build_rvp_stack()

    def num_length(self):
        return len(self._Numbers)

    def op_length(self):
        return len(self._Operators)

    def get_element_length(self):
        return len(self._Elements)

    def get_stack_values(self):
        return self._stack

    def get_stack_value(self, position):
        try:
            return self._stack[position].get_value()
        except:
            raise Exception(f'Out of bounds, size of stack {len(self._stack)} and given position {position}')

    def __build_rvp_stack(self):
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

        print('the stack:', self._stack)

    def calculate(self):
        tmp_stack = copy.deepcopy(self._stack)
        while len(tmp_stack) > 1:
            num1 = tmp_stack.pop(0)
            num2 = tmp_stack.pop(0)
            op = tmp_stack.pop(0).get_value()
            if op == Operations.ADD:
                tmp_stack.append(num1 + num2)

        print(f'size of tmp {len(tmp_stack)}')
        print(tmp_stack[0])

        self._calculation = tmp_stack[0]

        
    def get_calculation(self):
        return self._calculation
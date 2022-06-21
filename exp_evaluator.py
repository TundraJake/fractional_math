from parser import Parser
from tempfile import tempdir
from operators import Operations
import copy

class ExpEvaluator(object):

    def __init__(self, parser):
        self._Elements = copy.deepcopy(parser.get_elements())
        self._calculation = 0

    def num_length(self):
        return len(self._Numbers)

    def op_length(self):
        return len(self._Operators)

    def get_element_length(self):
        return len(self._Elements)

    def calculate(self):
        iter = 0
        op_type = 0
        total_elements = len(self._Elements)
        while len(self._Elements) != 1 and op_type != 5:
            op = Operations.operators[op_type]

            # print(f'size {len(self._Elements)} and iter {iter}')
            element = self._Elements[iter].get_value()
            # print(element, op)
            # print([x.get_value() for x in self._Elements], f'op is {op}')
            if element == Operations.ADD and element == op:
                # print(f'adding {self._Elements[iter-1].get_value()} and {self._Elements[iter+1].get_value()}')
                number = self._Elements[iter-1] + self._Elements[iter+1]
                # print(f'new number {number.get_value()}')
                self._Elements[iter] = number
                del self._Elements[iter+1]
                del self._Elements[iter-1]
                iter = 0

            elif element == Operations.MUL and element == op:
                number = self._Elements[iter-1] * self._Elements[iter+1]
                self._Elements[iter] = number
                del self._Elements[iter+1]
                del self._Elements[iter-1]
                iter = 0
                
            elif element == Operations.DIV and element == op:
                number = self._Elements[iter-1] / self._Elements[iter+1]
                self._Elements[iter] = number
                del self._Elements[iter+1]
                del self._Elements[iter-1]
                iter = 0

            else:
                iter += 1

            if iter == len(self._Elements) and op_type != 5:
                iter = 0
                op_type += 1
                # print('starting over')

        self._calculation = self._Elements[0].get_value()

        
    def get_calculation(self):
        return self._calculation
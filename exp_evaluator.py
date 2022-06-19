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
        total_elements = len(self._Elements)
        # print(f'starting elements', self._Elements)
        while len(self._Elements) != 1 and iter < total_elements:
            # print(f'len of items {len(self._Elements)} and iter is {iter}')
            element = self._Elements[iter].get_value()
            if element == Operations.ADD:
                number = self._Elements[iter-1] + self._Elements[iter+1]
                self._Elements[iter] = number
                del self._Elements[iter+1]
                del self._Elements[iter-1]
                iter = 0

            if element == Operations.MUL:
                number = self._Elements[iter-1] * self._Elements[iter+1]
                self._Elements[iter] = number
                del self._Elements[iter+1]
                del self._Elements[iter-1]
                iter = 0
                
            if element == Operations.DIV:
                number = self._Elements[iter-1] * self._Elements[iter+1]
                self._Elements[iter] = number
                del self._Elements[iter+1]
                del self._Elements[iter-1]
                iter = 0

            iter += 1

        self._calculation = self._Elements[0].get_value()

        
    def get_calculation(self):
        return self._calculation
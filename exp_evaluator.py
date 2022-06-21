from parser import Parser
from tempfile import tempdir
from operators import Operations, Operator
import copy

class ExpEvaluator(object):

    def __init__(self, parser):
        self._Elements = copy.deepcopy(parser.get_elements())
        self._calculation = 0
        self._ops_to_perform = [x.get_value() for x in self._Elements if type(x) == Operator]
        print('the ops', self._ops_to_perform)
        self._highest_precedence = ['*', '/']
        self._lowest_precedence = ['+', '-']

    def num_length(self):
        return len(self._Numbers)

    def op_length(self):
        return len(self._Operators)

    def get_element_length(self):
        return len(self._Elements)

    def calculate(self):
        iter = 0
        while len(self._Elements) != 1:
            if self._highest_precedence[0] in self._ops_to_perform or self._highest_precedence[1] in self._ops_to_perform:
                while True:
                    
                    element = self._Elements[iter].get_value()
                    if element in ['/', '*']:

                        if element == Operations.MUL:
                            number = self._Elements[iter-1] * self._Elements[iter+1]
                            self._Elements[iter] = number
                            del self._Elements[iter+1]
                            del self._Elements[iter-1]
                            self._ops_to_perform = [x.get_value() for x in self._Elements if type(x) == Operator]
                            iter = 0
                            
                        if element == Operations.DIV:
                            number = self._Elements[iter-1] / self._Elements[iter+1]
                            self._Elements[iter] = number
                            del self._Elements[iter+1]
                            del self._Elements[iter-1]
                            self._ops_to_perform = [x.get_value() for x in self._Elements if type(x) == Operator]
                            iter = 0

                    if not self._highest_precedence[0] in self._ops_to_perform and not self._highest_precedence[1] in self._ops_to_perform:
                        break
                    iter += 1
                            
            if self._lowest_precedence[0] in self._ops_to_perform or self._lowest_precedence[1] in self._ops_to_perform:

                while True:
                    element = self._Elements[iter].get_value()
                    if element in ['+']:

                        if element == Operations.ADD:
                            number = self._Elements[iter-1] + self._Elements[iter+1]
                            self._Elements[iter] = number
                            del self._Elements[iter+1]
                            del self._Elements[iter-1]
                            self._ops_to_perform = [x.get_value() for x in self._Elements if type(x) == Operator]
                            iter = 0
                            
                    if not self._lowest_precedence[0] in self._ops_to_perform:
                        break
                    iter += 1

            if iter == len(self._Elements):
                iter = 0
                
        self._calculation = self._Elements[0].get_value()

        
    def get_calculation(self):
        return self._calculation
class Operations(object):
    ADD = '+'
    SUB = '-'
    DIV = '/'
    MUL = '*'
    UNDERSCORE = '_'
    
    operators = [ADD, SUB, MUL]

class Operator(object):

    def __init__(self, operator):
        self._operator = operator

    def get_operator(self):
        return self._operator
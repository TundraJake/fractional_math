class Operations(object):
    ADD = '+'
    SUB = '-'
    DIV = '/'
    MUL = '*'
    
    operators = [ADD, SUB, DIV, MUL]

class Operator(object):

    def __init__(self, operator):
        self._operator = operator
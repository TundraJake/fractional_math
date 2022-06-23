from .entity import Entity

class Operations(object):
    ADD = '+'
    SUB = '-'
    DIV = '/'
    MUL = '*'
    UNDERSCORE = '_'
    
    illegal_chars = '[]\{\}!@#$%^&()?=,:;`~<>\'\"'
    operators = [MUL, DIV, ADD, SUB]

class Operator(Entity):

    def __init__(self, operator):
        self._operator = operator

    def get_operator(self):
        return self._operator

    def get_value(self):
        return self.get_operator()
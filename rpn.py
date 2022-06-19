from parser import Parser

class ReversePolishNotation(object):

    def __init__(self, parser):
        self._Number = parser.get_numbers()
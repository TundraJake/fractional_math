
class Expression(object):

    def __init__(self, expression):
        if len(expression) == 0:
            raise('Expression is empty')
        self._expression = expression

    def get_expression_string(self):
        return self._expression
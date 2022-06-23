class Expression(object):

    def __init__(self, expression):
        expression = expression.replace(' ', '')
        if len(expression) == 0:
            raise Exception('Expression is empty')
        self._expression = expression

    def get_length(self):
        return len(self._expression)

    def get_expression(self):
        return self._expression
class Number(object):

    def __init__(self, number):
        if not number.isnumeric():
            raise Exception(f'Number is either empty or incorrectly formatted. Given: {number}')
        self._number = number
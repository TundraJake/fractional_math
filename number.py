from operators import Operations


class Number(object):

    def __init__(self, number):
        if not Operations.UNDERSCORE in number and not Operations.DIV in number:
            self._whole = number
        elif Operations.DIV in number:
            self._num = number.split('/')[0]
            self._den = number.split('/')[1]
        else:
            self._whole = number.split('_')
            self._num = number[1].split('_')[0]
            self._den = number[1].split('_')[1]
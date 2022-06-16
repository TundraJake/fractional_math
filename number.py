from operators import Operations


class Number(object):

    _whole = 0
    _num = 0
    _den = 0

    def __init__(self, number):
        if not Operations.UNDERSCORE in number and not Operations.DIV in number:
            self._whole = int(number)
        elif Operations.DIV in number:
            self._num = int(number.split('/')[0])
            self._den = int(number.split('/')[1])
        else:
            self._whole = int(number.split('_'))
            self._num = int(number[1].split('_')[0])
            self._den = int(number[1].split('_')[1])

    def get_number(self):
        if self._den > 0:
            return f'{self._whole}_{self._num}/{self._den}'
        else:
            return f'{self._whole}'
from operators import Operations


class Number(object):

    _whole = 0
    _num = 0
    _den = 0

    def __init__(self, number):
        # print('input number: ', number)
        if not Operations.UNDERSCORE in number and not Operations.DIV in number:
            self._whole = int(number)
        else:
            temp = None
            if Operations.UNDERSCORE in number:
                temp = number.split('_')
                self._whole = int(temp[0])
                self._num = int(temp[1].split('/')[0])
                self._den = int(temp[1].split('/')[1])
            else:
                self._num = int(number.split('/')[0])
                self._den = int(number.split('/')[1])

    def get_number(self):
        if self._den > 0 and abs(self._whole) > 0:
            return f'{self._whole}_{self._num}/{self._den}'
        elif self._den > 0:
            return f'{self._num}/{self._den}'
        else:
            return f'{self._whole}'

    def get_whole_number(self):
        if self._whole:
            return self._whole
from operators import Operations
from math import gcd, floor

class Number(object):

    _whole = 0
    _num = 0
    _den = 0
    _gcd = 0

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
                if self._den == 0:
                    raise Exception(f'Denominator cannot be zero! Numerator given \'{self._num}\', Denominator \'{self._den}\'')
            else:
                self._num = int(number.split('/')[0])
                self._den = int(number.split('/')[1])

            if abs(self._num) > abs(self._den):
                fl = int(floor(abs(self._num)  / abs(self._den)))
                if self._num < 0:
                    fl *= -1
                self._whole += fl
                remainder = self._num % self._den
                self._num = remainder

            self._gcd = gcd(self._num, self._den)

            if self._gcd > 1:
                self._num = int(self._num / self._gcd)
                self._den = int(self._den / self._gcd)

            if self._num == self._den:
                self._whole += 1
                self._den = 0
                self._num = 0
            
            if self._den == 1:
                self._whole += self._num
                self._den = 0
                self._num = 0



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

    def get_value(self):
        return self.get_number()

    def __add__(self, rhs):
        string = '' 
        string = str(self._whole + rhs._whole)
        return Number(string)

    def __mul__(self, rhs):
        string = '' 
        string = str(self._whole * rhs._whole)
        return Number(string)

    def __truediv__(self, rhs):
        string = '' 

        if (self._den > 0) or (rhs._den > 0):
            string = ''
        else:
            string = f'{self._whole}/{rhs._whole}'

        return Number(string)

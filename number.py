from operators import Operations
from math import gcd, floor

class Number(object):

    _num = 0
    _den = 0
    _negative = False
    _gcd = 0

    def __init__(self, number):

        if not Operations.UNDERSCORE in number and not Operations.DIV in number:
            self._num = int(number)
            self._den = 1
        else:
            temp = None
            if Operations.UNDERSCORE in number:
                temp = number.split('_')
                whole = int(temp[0])
                if whole < 0:
                    self._negative = True

                self._den = int(temp[1].split('/')[1])
                if self._den == 0:
                    raise Exception(f'Denominator cannot be zero! Numerator given \'{self._num}\', Denominator \'{self._den}\'')
 
                self._num = int(temp[1].split('/')[0]) + abs(whole) * self.get_denominator()

            else:
                self._num = int(number.split('/')[0])
                self._den = int(number.split('/')[1])

                if self._num < 0 and self._den < 0:
                    self._negative = False
                elif self._num < 0 or self._den < 0:
                    self._negative = True

                self._num = abs(self._num)
                self._den = abs(self._den)

            self._gcd = gcd(self._num, self._den)

            if self._gcd > 1:
                self._num = int(self._num / self._gcd)
                self._den = int(self._den / self._gcd)

            print('end result:' , self._num, self._den, self._negative)

    def get_number(self):
        if self.get_denominator() == 1:
            num = self.get_numerator()
            if self.is_negative():
                num *= -1
            return f'{num}'
        elif self.get_denominator() > 1:
            if abs(self.get_numerator()) > abs(self.get_denominator()):
                whole = 0
                num = 0
                
                whole = int(floor(self.get_numerator() / self.get_denominator()))
                num = self.get_numerator() % self.get_denominator()

                if self.is_negative():
                    whole *= -1
                return f'{whole}_{num}/{self.get_denominator()}'
            else:
                num = self.get_numerator()
                if self.is_negative():
                    num *= -1
                return f'{num}/{self.get_denominator()}'

    def is_negative(self):
        return self._negative

    def get_whole_number(self):
        return self._whole

    def get_denominator(self):
        return self._den

    def get_numerator(self):
        return self._num

    def set_denominator(self, val):
        self._den = val

    def set_numerator(self, val):
        self._num = val

    def set_whole_number(self, val):
        self._whole = val

    def get_value(self):
        return self.get_number()

    def __add__(self, rhs):
        string = '' 
        if self.get_denominator() == 1 and rhs.get_denominator() == 1:
            string = str(self.get_numerator() + rhs.get_numerator())
        return Number(string)

    def __mul__(self, rhs):
        string = ''
        if self.get_denominator() == 1 and rhs.get_denominator() == 1: 
            string = str(self.get_numerator() * rhs.get_numerator())
        return Number(string)

    def __truediv__(self, rhs):
        string = '' 
        if (self.get_denominator() > 0) and (rhs.get_denominator() > 0):

            new_num = self.get_numerator() * rhs.get_denominator()
            new_den = self.get_denominator() * rhs.get_numerator()

            string = f'{new_num}/{new_den}'

        elif self.get_denominator() == 0 and rhs.get_denominator() == 0:
            string = f'{self._whole}/{rhs._whole}'


        return Number(string)

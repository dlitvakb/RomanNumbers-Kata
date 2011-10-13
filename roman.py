
class Roman(object):
    def __init__(self, symbol, value, previous):
        self.symbol = symbol
        self.value = value
        self.previous = previous

    def _can_parse(self, a_number):
        return a_number - self.value >= 0

    def parse(self, result, a_number):
        result += self.symbol
        a_number -= self.value
        return result, a_number

    def _child_parse(self, result, a_number):
        if self.previous._can_parse(a_number):
            return self.previous.parse(result, a_number)

        return result, a_number

class ChildRoman(Roman):
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def _child_parse(self, result, a_number):
        return result, a_number


MIL = Roman("M", 1000, ChildRoman("CM", 900))
QUINIENTOS = Roman("L", 500, ChildRoman("CL", 400))
CIEN = Roman("C", 100, ChildRoman("XC", 90))
CINCUENTA = Roman("D", 50, ChildRoman("XD", 40))
DIEZ = Roman("X",10, ChildRoman("IX", 9))
CINCO = Roman("V", 5, ChildRoman("IV", 4))
UNO = ChildRoman("I",1)

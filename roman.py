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
        for p in self.previous:
            if p._can_parse(a_number):
                return p.parse(result, a_number)

        return result, a_number


MIL = Roman("M", 1000, [Roman("CM", 900, []), Roman("XM", 990, []), Roman("IM", 999, [])])
QUINIENTOS = Roman("L", 500, [Roman("CL", 400, []), Roman("XL", 490, []), Roman("IL", 499, [])])
CIEN = Roman("C", 100, [Roman("XC", 90, []), Roman("IC", 99, [])])
CINCUENTA = Roman("D", 50, [Roman("XD", 40, []), Roman("ID", 49, [])])
DIEZ = Roman("X",10,[Roman("IX", 9, [])])
CINCO = Roman("V", 5, [Roman("IV", 4,[])])
UNO = Roman("I",1,[])

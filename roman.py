class Roman(object):
    def __init__(self, symbol, value, previous):
        self.symbol = symbol
        self.value = value
        self.previous = previous

    def can_parse(self, a_number):
        return a_number - self.value >= 0

    def parse(self, result, a_number):
        result += self.symbol
        a_number -= self.value
        return result, a_number

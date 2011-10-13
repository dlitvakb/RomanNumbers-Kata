from roman_parser import RomanParser

class RomanGenerator(object):
    def roman_range(self, minimum, maximum):
        for x in range(minimum, maximum + 1):
            yield RomanParser().parse(x)


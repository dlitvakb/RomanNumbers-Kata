from roman_parser import RomanParser

class RomanGenerator(object):
    def roman_range(self, minimum, maximum):
        result = []
        for x in range(minimum, maximum + 1):
            result.append(RomanParser().parse(x))

        return result

from roman import Roman

class RomanParser(object):
    def __init__(self):
        self.romans = [ Roman("M", 1000, [Roman("CM", 900, []), Roman("XM", 990, []), Roman("IM", 999, [])]),
                        Roman("L", 500, [Roman("CL", 400, []), Roman("XL", 490, []), Roman("IL", 499, [])]),
                        Roman("C", 100, [Roman("XC", 90, []), Roman("IC", 99, [])]),
                        Roman("D", 50, [Roman("XD", 40, []), Roman("ID", 49, [])]),
                        Roman("X",10,[Roman("IX", 9, [])]),
                        Roman("V", 5, [Roman("IV", 4,[])]),
                        Roman("I",1,[])]

    def parse(self, a_number):
        result = ""

        while a_number > 0:

            for r in self.romans:
                if r.can_parse(a_number):
                    result += r.symbol
                    a_number -= r.value
                    break

                for p in r.previous:
                    if p.can_parse(a_number):
                        result += p.symbol
                        a_number -= p.value
                        break

        return result

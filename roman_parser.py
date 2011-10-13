from roman import Roman, MIL, QUINIENTOS, CIEN, CINCUENTA, DIEZ, CINCO, UNO

class RomanParser(object):
    def __init__(self):
        self.romans = [MIL, QUINIENTOS, CIEN, CINCUENTA, DIEZ, CINCO, UNO]

    def parse(self, a_number):
        result = ""

        while a_number > 0:
           result, a_number = self._parse_number(result, a_number)

        return result

    def _parse_number(self, result, a_number):
        for r in self.romans:
            if r.can_parse(a_number):
                result, a_number = r.parse(result, a_number)
                break

            for p in r.previous:
                if p.can_parse(a_number):
                    result, a_number = p.parse(result, a_number)
                    break

        return result, a_number

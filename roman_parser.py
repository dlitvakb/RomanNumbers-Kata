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
        for roman in self.romans:
            if roman._can_parse(a_number):
                result, a_number = roman.parse(result, a_number)
                break

            result, a_number = roman._child_parse(result, a_number)

        return result, a_number

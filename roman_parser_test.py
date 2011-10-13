import unittest
from roman_parser import RomanParser

class RomanParserTest(unittest.TestCase):

    def test_decimal_uno_a_romano_I(self):
        self.assertEquals(RomanParser().parse(1), "I")

    def test_decimal_dos_a_romano_II(self):
        self.assertEquals(RomanParser().parse(2), "II")

    def test_decimal_tres_a_romano_III(self):
        self.assertEquals(RomanParser().parse(3), "III")

    def test_decimal_cuatro_a_romano_IV(self):
        self.assertEquals(RomanParser().parse(4), "IV")

    def test_decimal_cinco_a_romano_V(self):
        self.assertEquals(RomanParser().parse(5), "V")

    def test_decimal_seis_a_romano_VI(self):
        self.assertEquals(RomanParser().parse(6), "VI")

    def test_decimal_siete_a_romano_VII(self):
        self.assertEquals(RomanParser().parse(7), "VII")

    def test_decimal_ocho_a_romano_VIII(self):
        self.assertEquals(RomanParser().parse(8), "VIII")

    def test_decimal_catorce_a_romano_XIV(self):
        self.assertEquals(RomanParser().parse(14), "XIV")

    def test_decimal_1321_a_romano_MCCCXXI(self):
        self.assertEquals(RomanParser().parse(1321), "MCCCXXI")

    def test_decimal_2459_a_romano_MMCLDIX(self):
        self.assertEquals(RomanParser().parse(2459), "MMCLDIX")

    def test_decimal_1117_a_romano_MCXVII(self):
        self.assertEquals(RomanParser().parse(1117), "MCXVII")

    def test_decimal_944_a_romano_CMXDIV(self):
        self.assertEquals(RomanParser().parse(944), "CMXDIV")

if __name__ == "__main__":

    unittest.main()

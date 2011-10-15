import unittest
from roman_parser import RomanParser

romans = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI',
          7:'VII', 8:'VIII', 9:'IX', 10:'X', 11:'XI',
          12:'XII', 13:'XIII', 14:'XIV', 15:'XV',
          16:'XVI', 17:'XVII', 19:'XIX', 20:'XX',
          21:'XXI', 23:'XXIII', 24:'XXIV', 26:'XXVI',
          29:'XXIX', 30:'XXX', 31:'XXXI', 34:'XXXIV',
          39:'XXXIX', 40:'XL', 41:'XLI', 44:'XLIV', 48:'XLVIII',
          49:'XLIX', 50:'L', 1321:'MCCCXXI', 1439:'MCDXXXIX',
          1999:'MCMXCIX', 3948:'MMMCMXLVIII', 3949:'MMMCMXLIX',
	  321:'CCCXXI'}

class RomanParserTest(unittest.TestCase):
    def test_los_decimales_se_traducen_correctamente_a_romanos(self):
        for k, v in romans.items():
            self.assertEquals(v, RomanParser().parse(k))

if __name__ == "__main__":

    unittest.main()

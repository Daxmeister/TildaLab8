import unittest
from Syntax import *

class SyntaxTest(unittest.TestCase):

    def testLETTERletternum(self):
        self.assertEqual(kollaAtom("Hb5", "Formeln är syntaktiskt korrekt"))

    def testLETTERletterLETTER(self):
        self.assertEqual(kollaAtom("AbD", "För litet tal vid radslutet"))

    def testletter(self):
        self.assertEqual(kollaAtom("b5"), "Saknad stor bokstav vid radslutet")

if __name__ == __main__:
    unittest.main()


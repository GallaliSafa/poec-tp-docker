import unittest
from calc import apply_vat
class TestCalcMethods(unittest.TestCase):
    def test_price(self):
        self.assertEqual(apply_vat(100,20),120)

    def test_float(self):
        self.assertEqual(apply_vat(55.25,5.5),58.28874999999999)

    def test_null(self):
        with (self.assertRaises(ValueError)):
            apply_vat(0,10)

    def test_prix_negatif(self):
        with self.assertRaises(ValueError):
            apply_vat(-10.99, 10)

    def test_chaine(self):
        with self.assertRaises(ValueError):
            apply_vat('wrong value', 10)

    def test_percent_negatif(self):
        with self.assertRaises(ValueError):
            apply_vat(100, -10)

    def test_tva(self):
        with self.assertRaises(ValueError):
            apply_vat(100, 110)
if __name__ == '__main__':
    unittest.main()
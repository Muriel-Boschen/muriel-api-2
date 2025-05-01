import unittest
from matematica import soma, subtrai, multiplica, divide, eh_par

class TestMatematica(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(3, 4), 7)

    def test_subtrai(self):
        self.assertEqual(subtrai(10, 3), 7)

    def test_multiplica(self):
        self.assertEqual(multiplica(6, 5), 30)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_eh_par_true(self):
        self.assertTrue(eh_par(8))

    def test_eh_par_false(self):
        self.assertFalse(eh_par(9))

if __name__ == '__main__':
    unittest.main()

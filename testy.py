import unittest
import kalkulator

class TestyKalkulator(unittest.TestCase):

    def test_kalkulator_dodawanie(self):
        # given
        a = 8
        b = 13
        expected = 20
        # when
        result = kalkulator.dodawanie(a,b)
        # then
        self.assertEqual(result, expected)

    def test_kalkulator_odejmowanie(self):
        # given
        a = 15
        b = 7
        expected = 8
        # when
        result = kalkulator.odejmowanie(a,b)
        # then
        self.assertEqual(result, expected)

    def test_kalkulator_mnozenie(self):
        # given
        a = 2
        b = 3
        expected = 6
        # when
        result = kalkulator.mnozenie(a,b)
        # then
        self.assertEqual(result, expected)

    def test_kalkulator_dzielenie(self):
        # given
        a = 27
        b = 9
        expected = 3
        # when
        result = kalkulator.dzielenie(a,b)
        # then
        self.assertEqual(result, expected)

    def testTypDanych_dodawanie(self):
        # given
        a = 5
        b = 10
        expected_type = int
        # when
        result = kalkulator.dodawanie(a,b)
        # then
        self.assertEqual(type(result), expected_type)

if __name__ == '__main__':
    unittest.main()

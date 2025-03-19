import unittest

def calculate_discount(total_quantity):
    # Логика определения скидки в зависимости от объёма.
    if total_quantity > 300000:
        return 15
    elif total_quantity > 50000:
        return 10
    elif total_quantity > 10000:
        return 5
    else:
        return 0

class TestDiscount(unittest.TestCase):
    def test_get_discount(self):
        self.assertEqual(calculate_discount(0), 0)
        self.assertEqual(calculate_discount(10000), 0)
        self.assertEqual(calculate_discount(10001), 5)
        self.assertEqual(calculate_discount(50000), 5)
        self.assertEqual(calculate_discount(50001), 10)
        self.assertEqual(calculate_discount(300000), 10)
        self.assertEqual(calculate_discount(300001), 15)
import unittest
from prime_number import is_prime
class TestPrime(unittest.TestCase):
	def test_prime_not_prime(self):
		self.assertTrue(is_prime(2))
		self.assertTrue(is_prime(5))
		self.assertFalse(is_prime(9))
		self.assertTrue(is_prime(11))
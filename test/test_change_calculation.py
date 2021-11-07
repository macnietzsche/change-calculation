from unittest import TestCase
from services.change_calculation import has_enough_change

class TestChangeCalculation(TestCase):
    def test_change_calculation(self):
        # Case 1
        payments_received = [25, 25, 50]
        expected_response = "SI"
        response = has_enough_change(payments_received)
        self.assertEqual(expected_response,response)

        #Case 2
        payments_received = [25, 100]
        expected_response = "NO"
        response = has_enough_change(payments_received)
        self.assertEqual(expected_response,response)

        #Case 3
        payments_received = [25, 25, 50, 50, 100]
        expected_response = "NO"
        response = has_enough_change(payments_received)
        self.assertEqual(expected_response,response)
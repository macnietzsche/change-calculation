from unittest import TestCase
from services.change_calculation import has_enough_change, process_change

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


    def test_valid_inputs(self):
        #Case 1
        payments_received = [34, 45, 25]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

        #Case 2
        payments_received = [34, 45, 25, "a", "b"]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

        #Case 3
        payments_received = [25, -50, 25]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

        #Case 4
        payments_received = [25, "a", "h", 100]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

    def test_process_change(self):
        # Case 1
        current_bills = {25: 0, 50: 0, 100: 0}
        change = 0

        expected_result = sum(k * v for k, v in current_bills.items()) - change
        processed_change = process_change(change, current_bills)
        result = sum(k * v for k, v in processed_change.items())
        self.assertEqual(expected_result,result)

        # Case 2
        current_bills = {25: 6, 50: 1, 100: 0}
        change = 100

        expected_result = sum(k * v for k, v in current_bills.items()) - change
        processed_change = process_change(change, current_bills)
        result = sum(k * v for k, v in processed_change.items())
        self.assertEqual(expected_result,result)

        # Case 3
        current_bills = {25: 3, 50: 0, 100: 0}
        change = 100

        expected_result = None
        result = process_change(change, current_bills)
        self.assertEqual(expected_result,result)

        # Case 4
        current_bills = {25: 0, 50: 2, 100: 1}
        change = 175

        expected_result = None
        result = process_change(change, current_bills)
        self.assertEqual(expected_result,result)







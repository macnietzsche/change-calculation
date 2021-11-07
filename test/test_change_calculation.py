from unittest import TestCase
from services.change_calculation import has_enough_change,dot_product, process_change

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
        payments_received = [34, 45, 25]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

        payments_received = [34, 45, 25, "a", "b"]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

        payments_received = [25, -50, 25]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

        payments_received = [25, "a", "h", 100]
        with self.assertRaises(Exception):
            has_enough_change(payments_received)

    def test_dot_product(self):
        array_a = [1, 2, 3]
        arrab_b = [1, 2, 3]
        expected_result = 14
        result = dot_product(array_a, arrab_b)
        self.assertEqual(expected_result,result)

        array_a = [0, 2, 4, 6]
        arrab_b = [1, 4, 6, 90]
        expected_result = 572
        result = dot_product(array_a, arrab_b)
        self.assertEqual(expected_result,result)

        array_a = [-5, 7, 3, -5, -56]
        arrab_b = [1, 25, 13, 0, -5]
        expected_result = 489
        result = dot_product(array_a, arrab_b)
        self.assertEqual(expected_result,result)

    def test_process_change(self):
        # Case 1
        current_bills = {25: 0, 50: 0, 100: 0}
        change = 0

        values = list(current_bills.values())
        keys = list(current_bills.keys())
        
        expected_result = dot_product(values,keys) - change
        
        processed_change = process_change(change, current_bills)

        processed_values = list(processed_change.values())
        processed_keys = list(processed_change.keys())

        result = dot_product(processed_values,processed_keys)

        self.assertEqual(expected_result,result)

        # Case 2
        current_bills = {25: 6, 50: 1, 100: 0}
        change = 100

        values = list(current_bills.values())
        keys = list(current_bills.keys())
        
        expected_result = dot_product(values,keys) - change
        
        processed_change = process_change(change, current_bills)

        processed_values = list(processed_change.values())
        processed_keys = list(processed_change.keys())

        result = dot_product(processed_values,processed_keys)

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







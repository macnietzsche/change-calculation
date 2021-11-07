from typing import List
from itertools import product
TICKET_COST =  25
POSITIVE_RESPONSE = "SI"
NEGATIVE_RESPONSE = "NO"
VALID_INPUTS = {25: 0, 50: 0, 100: 0}

def dot_product(vector_a: List[float], vector_b: List[float])->float:
   if len(vector_a) != len(vector_b):
      return 0
   return sum(i[0] * i[1] for i in zip(vector_a, vector_b))

def process_change(required_value: int, current_cash: dict):
    numbers_of_bills = list(current_cash.values())
    bill_denominations = list(current_cash.keys())
    iterated_numbers_of_bills = list(map(lambda x: list(range(x + 1)), numbers_of_bills))

    posibilities = product(*iterated_numbers_of_bills)
    posibilities_as_dict = list(map(lambda item: dict(zip(bill_denominations, item)),posibilities))
    for posibility in posibilities_as_dict:
        values = list(posibility.values())
        keys = list(posibility.keys())

        amount = dot_product(values,keys)
        if amount == required_value:
            response = current_cash.copy()
            for key in keys:
                response[key] -= posibility[key]
            return response
    return None

def has_enough_change(payments_received: List[int]) -> str:
    current_cash = VALID_INPUTS
    for payment in payments_received:
        if not payment in VALID_INPUTS.keys():
            raise Exception("Input is not valid")
        
        change = payment - TICKET_COST
        current_cash = process_change(change,current_cash)
        if not current_cash:
            return NEGATIVE_RESPONSE
        current_cash[payment] += 1
    
    return POSITIVE_RESPONSE
from typing import List
from itertools import product

TICKET_COST =  25
POSITIVE_RESPONSE = "SI"
NEGATIVE_RESPONSE = "NO"
INITIAL_NUMBER_OF_BILLS = {25: 0, 50: 0, 100: 0}

def process_change(required_value: int, current_cash: dict):
    numbers_of_bills = list(current_cash.values())
    bill_denominations = list(current_cash.keys())

    iterated_numbers_of_bills = list(map(lambda x: list(range(x + 1)), numbers_of_bills))
    posibilities = product(*iterated_numbers_of_bills)
    posibilities_as_dict = list(map(lambda item: dict(zip(bill_denominations, item)),posibilities))
    for posibility in posibilities_as_dict:
        amount = sum(k * v for k, v in posibility.items())
        if amount == required_value:
            return {key: current_cash[key] - posibility.get(key, 0) for key in current_cash}
    return None

def has_enough_change(payments_received: List[int]) -> str:
    current_cash = INITIAL_NUMBER_OF_BILLS
    for payment in payments_received:
        if not payment in INITIAL_NUMBER_OF_BILLS.keys():
            raise Exception("Input is not valid")
        
        change = payment - TICKET_COST
        current_cash = process_change(change,current_cash)
        if not current_cash:
            return NEGATIVE_RESPONSE
        current_cash[payment] += 1
    
    return POSITIVE_RESPONSE
from typing import List

TICKET_COST =  25
INITIAL_CASH = 0
POSITIVE_RESPONSE = "SI"
NEGATIVE_RESPONSE = "NO"

def has_enough_change(payments_received: List[int]) -> str:
    current_cash = INITIAL_CASH
    for payment in payments_received:
        current_cash += 2 * TICKET_COST - payment
        if current_cash <= 0:
            return NEGATIVE_RESPONSE
    return POSITIVE_RESPONSE
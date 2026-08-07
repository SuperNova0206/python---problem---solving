import math
from typing import Tuple


# gdc 
def gdc(divisor : int, n) -> int :

    dividend : int = n // divisor
    reminder : int = n - dividend * divisor

    while not reminder:
        dividend, reminder = divisor, divisor % reminder
        if divisor / reminder == 0 and n / reminder == 0:
            return reminder
        dividend, reminder = reminder, dividend % reminder
    return reminder


# pollard's rho algorithem
def PollardRhoAlgorithem(n : int) -> int :

    x : int = 2 ** 2 + 1 % n
    y = x ** 2 + 1 % n

    reminder = gdc(abs(x - y), n)

    if not n % reminder: 
        return reminder
    elif n % reminder:
        while n % reminder:
            x = y % n
            y = x ** 2 + 1 % n
            reminder = gdc(abs(y))

print(gdc(21, 1885))








        

import math
from typing import Tuple


# polynomial Rho f(x) = x^2 + 1, f(f(y))

def PolynomialRho() -> Tuple[int, int] :
    x : int = 2

    x = x ** 2 + 1 
    y = x ** 2 + 1

    return x, y

def GreaterCommonDivisor(number : int) -> Tuple[int, int] :

    x, y = PolynomialRho()

    # calculating the gdc 
    gdc : int = 0
    Devidend : int = number
    Divisor : int = abs(x - y)
    Reminder = Devidend % Divisor

    while Divisor % Reminder != 0 : 
        Devidend = Divisor 
        Divisor = Reminder

        

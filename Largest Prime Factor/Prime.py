import math

PrimeFactors : list = []

def PollardRhoAlgorithm(n : int ) -> int :

    # initiative values 
    BeginX : int = 2
    BeginY : int = 2

    # polynomial function for x 
    PolynomialFunctionX : int = BeginX ** 2 + 1

    # polynomial function for y 
    PolynomialFunctionY : int = PolynomialFunctionX ** 2 + 1

def GreaterDivisableCommon_GDC(n : int, x : int, y : int) -> int :

    gdc : int = n % abs(x - y)


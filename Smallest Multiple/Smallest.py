from math import gcd

def LCM(start : int, end : int) -> int :
    result : int = start
    for n in range(start, end + 1) :
        result = (result * n) // gcd(result, n)
    return result

print(LCM(1, 20))
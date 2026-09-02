# def isPrime(n : int) -> bool :
#     if n < 2 :
#         return False
#     for i in range(2, int(n ** 0.5) + 1) :
#         if n % i == 0 :
#             return False
#     return True

# term = 6
# number = 2

# while term > 0 :
#     if isPrime(number) :
#         term -= 1
#     number += 1
# print(number - 1)

# Sieve of Eratosthenes 
class Solution :
    def __init__(self, term : int) :
        self.term = term

    def sieve_eratosthnes(self) -> int :
        start : int = 100
        primes : list = [[i, True] for i in range(2, start + 1)]

    def isPrime(self, n : int) -> bool :
        if n < 2 : 
            return False
        for i in range(2, int(n ** 0.5) + 1) :
            if n % i == 0 :
                return False
        return True



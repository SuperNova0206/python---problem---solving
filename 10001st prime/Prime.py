def isPrime(n : int) -> bool :
    if n < 2 :
        return False
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

term = 6
number = 2

while term > 0 :
    if isPrime(number) :
        term -= 1
    number += 1
print(number - 1)

# Sieve of Eratosthenes 
class Solution :

    def sieve_eratosthnes(self) -> int :
        start : int = 100
        values : list = [True] * (start + 1)

        # from True into False value to keep just the prime numbers
        for i in range(2, int(start ** 0.5)):
            for j in range(i * i, start + 1, i): 
                values[j] = False if values[j] else False

        primes = []
        for i in range(2, start + 1):
            if values[i]:
                primes.append(i)
        return primes

Primes = Solution()
print(Primes.sieve_eratosthnes())

        
            


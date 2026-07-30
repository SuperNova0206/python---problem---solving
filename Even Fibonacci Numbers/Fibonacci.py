
import math

class FibonacciClass:

    def __init__(self, values : list) -> None :
        self.values = values

    def next_term(self) -> int : 
        return self.values[len(self.values) - 1] + self.values[len(self.values) - 2]

    def term(self, value : int) -> int :
        return round(math.log( value * math.sqrt(5)) / math.log(1.618))
    
    def value(self, n : int) -> int :
        first_part = (1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n
        second_part = ( 2 ** n * math.sqrt(5))
        return round(first_part / second_part)

FibonacciSequence : FibonacciClass = FibonacciClass([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

sum : int = 0

for t in range(2, FibonacciSequence.term(value=4 * 10 ** 6) + 1, 1) :
    if FibonacciSequence.value(t) % 2 == 0:
        sum += FibonacciSequence.value(t)
print(sum)
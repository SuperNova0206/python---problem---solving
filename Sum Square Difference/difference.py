# The Square Pyramidal Numbers

FirstTerm : int = 1
CommonDifferent : int = 1
LastTerm : int = 10 ** 120

# number of terms
NumberOfTerms : int = (LastTerm - FirstTerm + CommonDifferent) // CommonDifferent

# sum of the arithmetic progression
SumArithmeticProgression : int = (NumberOfTerms * (NumberOfTerms + 1) * (2 * NumberOfTerms + 1)) // 6

# The second power arithmetic series
# Liner sum
SumPowerArithmeticSeries : int = ((NumberOfTerms * (NumberOfTerms + 1)) // 2 ) ** 2

# Different formula n(n + 1)(n - 2)(3n + 1) / 12
DifferentSums = SumPowerArithmeticSeries - SumArithmeticProgression
print(DifferentSums)

sum_sq : int = 0
sum_added : int = 0
for i in range(LastTerm) :
    sum_added += i
    sum_sq = sum_sq + i ** 2

print(sum_added ** 2 - sum_sq)
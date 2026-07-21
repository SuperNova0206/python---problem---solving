# The Square Pyramidal Numbers

FirstTerm : int = 1
CommonDifferent : int = 1
LastTerm : int = 100

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
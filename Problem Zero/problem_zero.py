"""
    1 - The sum of the first odd squares is 1 + 9 + 25 = 35
    odd is the number that his modulation with 2 equals 2
    2 - range 170,000
"""

sum : int = 0

for i in range(1, 170000, 1) :
    if (i**2) % 2 != 0 :
        sum += i ** 2

print(sum)
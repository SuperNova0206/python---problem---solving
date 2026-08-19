# Reverse algorithm 

def isPalindromic(number : int) -> True :
    Original  = number
    revers : int = 0
    while (number > 0) :
        a : int = number % 10
        revers = revers * 10 + a
        number //= 10
    return revers == Original

LargestPalindromicNumber : int | None = 0
Operation : str


for i in range(100, 999 + 1, 1):
    for j in range(i, 999 + 1, 1):
        Multiplication : int = i * j
        if isPalindromic(Multiplication) : 
            if LargestPalindromicNumber >= 0 and LargestPalindromicNumber < Multiplication:
                LargestPalindromicNumber = Multiplication

print(LargestPalindromicNumber)
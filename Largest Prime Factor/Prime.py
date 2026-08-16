number : int = int(input("Enter the number: "))
factor : int = 2
LastFactor : int | None = None

while number > 1 :
    if number % factor == 0:
        LastFactor = factor
        number //= factor
    factor += 1
print(LastFactor)

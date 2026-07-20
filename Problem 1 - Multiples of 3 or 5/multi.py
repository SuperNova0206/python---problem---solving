sum : int = 0

for i in range(1, 1000, 1) :
    if i % 3 == 0 or i % 5 == 0 :
        sum += i

print(sum)

# Solution 2

def neth(a, d, x) -> int :
    n : int = (x - a + d) // d
    return n

def last_term(a, d, n, x) -> int :
    l : int = a + (n - 1) * d
    while l >= x :
        n -= 1
        l = a + (n - 1) * d
    return l


def sum(a : int, d : int, x : int) -> int :
    n : int = neth(a, d, x)
    l : int = 999
    s : int = (n * (a + l)) // 2
    return s, l, n

def total() -> int : ...

print(sum(5, 5, 1000))
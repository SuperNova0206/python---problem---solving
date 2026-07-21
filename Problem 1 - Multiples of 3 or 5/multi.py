import time
sum : int = 0
run_time = time.time()
for i in range(1, 10000, 1) :
    if i % 3 == 0 or i % 5 == 0 :
        sum += i

print(sum)
print(time.time() - run_time)
# Solution 2

run_time = time.time()
def neth(a, d, x) -> int :
    n : int = (x - a + d) // d
    return n


# calculating the sum of multipliers
def sum(a : int, d : int, x : int) -> int :
    n : int = neth(a, d, x)
    l, n = verify_calculate_lt(n, x, d, a)
    s : int = (n * (a + l)) // 2
    return s
# verify and calculate the last term
def verify_calculate_lt(n : int, x : int, d : int, a : int) -> int :
    l : int = a + (n - 1) * d
    while l >= x :
        n -= 1
        l = a + (n - 1) * d
    return l, n

# calculating the total
def total() -> int :
    return sum(a=3, d=3, x=10000) + sum(a=5, d=5, x=10000) - sum(a=15, d=15, x=1000)

print(total())
print(time.time() - run_time)

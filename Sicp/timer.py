from timeit import Timer
primes=[]
def get_primes(n):
    global primes
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
Timer(get_primes(1000000)).timeit(1)
print primes[-1]

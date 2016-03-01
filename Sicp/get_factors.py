primes = [2, 3]


def nextPrime():
    global primes
    found = False
    test = primes[-1] + 2
    while not found:
        for prime in primes:
            divides = bool(test % prime == 0)
            broken = False
            if divides:
                broken = True
                break
        if not broken:
            primes.append(test)
            break
        else:
            test += 2


def get_factors(n):
    # gives a dictionary of primes with the time they divide a given number n.
    global primes
    prime_factors = {}
    while primes[-1] <= n:  # checking factors from the primes list.
        nextPrime()
    prime = primes[0]
    index = 0
    while prime <= n:
        while n % prime == 0:
            if prime in prime_factors:
                prime_factors[prime] += 1
            else:
                prime_factors[prime] = 1
            n /= prime
        index += 1
        prime = primes[index]
    return prime_factors

print get_factors(25)

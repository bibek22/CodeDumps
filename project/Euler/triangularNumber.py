import summation_of_primes as sop
primes = sop.primes_primitive(10000)
print primes
fileHandle = open("primes.txt", "w+")
for each in primes:
    print>>fileHandle, int(each)
with open("primes.txt", "w+") as f:
    primes = f.read().splitlines()


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


def factors_count(n):
    dict_factor = get_factors(n)
    count = 1
    for each in dict_factor:
        count *= dict_factor[each]+1
    return count


print primes
n = 1
last_triangular = 1
while factors_count(last_triangular) < 25:
    n += 1
    last_triangular += n  # generates next triangular number itself.
print n

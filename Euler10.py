#Problem:The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
#Solution: Using already known primes, we can sieve out composite numbers in a list and then sum up the remaining primes.
import math
sieve = [True] * 2000000
def isPrime(sieve, x):
    for i in range(x+x, len(sieve), x):
        sieve[i] = False

for x in range(2, int(math.sqrt(len(sieve))) + 1):
    if sieve[x]: isPrime(sieve, x)

print(sum(i for i in range(2, len(sieve)) if sieve[i]))

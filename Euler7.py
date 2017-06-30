#Problem:By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?
#Solution: Create a function that checks if a number is prime. Check numbers until we find the 10001st prime number
import math
def is_prime(n):
    if n%2 == 0: return False #if its even
    p = 3
    root = math.sqrt(n)
    while p < root+1:
        if n % p == 0: return False
        p += 2
    return True
 
def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime
print(nth_prime(10001))
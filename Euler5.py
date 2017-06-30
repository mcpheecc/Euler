#Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Solution: Multiply each number from 1 to 20 to get the product n. Check if n/2 is still divisible by each numbers 1 from 20. Repeat for each number until the smallest is found.
def isDivisible(x): #checks if x is divisible by each factor 1 to 20 
  for i in range(2,21):
    if(x%i!=0):
      return False
  return True
n = 1
for i in range(1,21):
  n = n*i
for i in range(2,21):
  while (isDivisible(n/i)):
    n=n/i
print(n)
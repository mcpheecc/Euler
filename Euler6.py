#Problem:
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Solution: Create a function that sums the squares and squares the sums of the first x natural numbers
def sumSquare(x): #returns the sum of the squares of the first x natural numbers
  result = 0 
  for i in range(x+1):
    result = result + i*i
  return result
def squareSum(x): #returns the square of the sum of the first x natural numbers
  result = 0
  for i in range(x+1):
    result = result + i
  return result*result
print(squareSum(100)-sumSquare(100))
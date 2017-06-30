#Problem:A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
#Solution: generate a list of numbers by multiplying each 3-digit number. check if they are palindromes, return the largest one 

def isPalindrome(x):
  i = str(x)
  j=0
  while (j<len(i)/2):
    if i[j]!=i[len(i)-j-1]:
      return False
    j = j+1 
  return True
gen = range(100,999)
result = []
for i in gen:
  for j in gen:
    prod = i*j
    if(isPalindrome(prod)):
      result.append(prod)
print(max(result))
  
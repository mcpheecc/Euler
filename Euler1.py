#Problem: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#Solution: Generate all multiples of 3 and 5 below 1000, exclude duplicates, and sum the list
result = []
i=0
while (i < 1000):
  result.append(i)
  i = i+3
i=0 
while (i <1000):
  if(i not in result):
    result.append(i)
  i = i+5
x = 0
for i in result:
  x = x+i
print(x)
#Problem:The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
#Solution: determine factors of 600851475143 up to square root of 600851475143 then check if each is prime, return highest prime factor
import math
root = int(math.floor(math.sqrt(600851475143)))
result = []
i=2
while (i<root):
  if (600851475143%i==0):
    result.append(i)
  i = i+1
for i in result:
  for j in result:
    if(i<j):
      if(j%i==0):
        result.remove(j)
print(max(result))

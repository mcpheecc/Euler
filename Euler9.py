#Problem:A Pythagorean triplet is a set of three natural numbers, a < b < c, for example: 3,4,5
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
#Find abc
#Solution:Loop over possible values from a and b and check if they form a Pythagorean triplet with c=1000-a-b. Limit to a to < 1000/3 and b to < 1000/2
for a in range(1,333):
  for b in range(1,500):
    c = 1000-a-b
    if (a*a+b*b==c*c):
      print(a,b,c,a*b*c)

# Sum of squares of even numbers using map, filter, reduce
# Problem: nums = [1,2,3,4] → 2^2 + 4^2 = 4 + 16 = 20.
from functools import reduce
li=[1,2,3,4]
ans= reduce(lambda x,y:x+y,map(lambda x:x*x,filter (lambda x:x%2==0,li)))
print(ans)

# filter use to filter even num
# map lambda use to sum of square
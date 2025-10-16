# 3.reduce
# for using reduce we have to first include library
# it will always take 2 arguments 
# 1 Find the sum of all numbers in a list using reduce().
# Input: [1, 2, 3, 4, 5] → Output: 15
from functools import reduce
li= [1, 2, 3, 4, 5]
ans=reduce(lambda x,y: x+y,li)
print(ans)


















































# 1) Square each number in a list using map()
# Problem: Given nums = [1, 2, 3, 4], return [1, 4, 9, 16].

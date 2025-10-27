# 3.reduce
# for using reduce we have to first include library
# it will always take 2 arguments 

# 1 Find the sum of all numbers in a list using reduce().
# Input: [1, 2, 3, 4, 5] → Output: 15
# from functools import reduce
# li= [1, 2, 3, 4, 5]
# ans=reduce(lambda x,y: x+y,li)
# print(ans)




# 2 Find the product of all numbers in a list.
# Input: [1, 2, 3, 4] → Output: 24
# from functools import reduce
# li = [1, 2, 3, 4]
# ans = reduce(lambda x, y: x * y, li)
# print(ans)


#3 Find the largest number in a list.
#Input: [5, 3, 8, 6, 2] → Output: 8
# from functools import reduce
# li = [5, 3, 8, 6, 2]
# ans = reduce(lambda x, y: x if x > y else y, li)
# print(ans)



# 4 Find the smallest number in a list.
# Input: [5, 3, 8, 6, 2] → Output: 2
# from functools import reduce
# li = [5, 3, 8, 6, 2]
# ans = reduce(lambda x, y: x if x < y else y, li)
# print(ans)


# 5 Find the sum of squares of all numbers.
# Input: [1, 2, 3, 4] → Output: 30
# from functools import reduce
# li = [1, 2, 3, 4]
# ans = reduce(lambda x, y: x + y**2, li, 0)
# print(ans)

# 6 Find the sum of even numbers in a list.
# Input: [1, 2, 3, 4, 5, 6] → Output: 12
# from functools import reduce
# li = [1, 2, 3, 4, 5, 6]
# ans = reduce(lambda x, y: x + (y if y % 2 == 0 else 0), li, 0)
# print(ans)


# 7 Count how many elements are positive numbers.
# Input: [-2, 5, -7, 9, 3, -1] → Output: 3
# from functools import reduce
# li = [-2, 5, -7, 9, 3, -1]
# ans = reduce(lambda x, y: x + (1 if y > 0 else 0), li, 0)
# print(ans)



# 8 Find factorial of a number using reduce().
# Input: 5 → Output: 120
# from functools import reduce
# num = 5
# ans = reduce(lambda x, y: x * y, range(1, num + 1))
# print(ans)


# 9 Find the longest word in a list using reduce().
# Input: ["apple", "banana", "cherry", "kiwi"] → Output: "banana"
from functools import reduce
li = ["apple", "banana", "cherry", "kiwi"]
ans = reduce(lambda x, y: x if len(x) > len(y) else y, li)
print(ans)































# 1) Square each number in a list using map()
# Problem: Given nums = [1, 2, 3, 4], return [1, 4, 9, 16].

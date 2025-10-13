# lambda fucntion is also known as anonymsa function  or single lin function 
# is it use with map filter and 
# syntax- lambda argument :code/logic
# def add (a,b):
#     return a+b
# print(add(5,5))
# # convert this in lambda
# ans =  lambda a,b:a+b
# print(ans(5,6))

# in single argument
# def plusone(num):
#     return num+1
# print(plusone(6))

#max number 
# ans=lambda x:x+1
# print(ans(60))

# def maxnum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# ans=lambda x,y:x if x>y else y
# print(ans(8,70))     


# que 
# 1 Write a lambda function to add two numbers.
# Input: a=5, b=7 → Output: 12
# ans =  lambda a,b:a+b
# print(ans(5,7))
# 2 Write a lambda function to find th+e square of a number.
# Input: 5 → Output: 25
# ans=lambda num:  num*num
# print(ans(5))
# 3 Write a lambda function to find the maximum of two numbers.
# ans=lambda x,y:x if x>y else y
# print(ans(8,70))  

# 4 Write a lambda function to check if a number is even or odd.
# Input: 7 → Output: "Odd"
ans=lambda num:"even" if  num%2==0 else "odd"
print(ans(7))
# 5 Write a lambda function to get the length of a given string.
# Input: "Mahesh" → Output: 6
x="mahesh"
ans =lambda x :len(x)
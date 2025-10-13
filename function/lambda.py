# lambda fucntion is also known as anonymsa function  or single lin function 
# is it use with map filter and reduce
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
# ans=lambda num:"even" if  num%2==0 else "odd"
# print(ans(7))
# 5 Write a lambda function to get the length of a given string.
# Input: "Mahesh" → Output: 6
# x="mahesh"
# ans =lambda x :len(x)
# print(ans(x))


#6 Write a lambda function to reverse a string.
# Input: "hello" → Output: "olleh"
# x="hello"
# ans=lambda x :x[::-1]
# print(ans(x))
#7 Write a lambda function to check if a string is a palindrome.
# Input: "level" → Output: True
# x="level"
# ans=lambda x :x==x[::-1]
# print(ans(x))
# #8 Write a lambda function to find the cube of a number.
# # Input: 3 → Output: 27
# ans=lambda num:  num**3
# print(ans(3))
# 9 Write a lambda function to find the largest number in a list using max() and key=lambda.
# Input: [5, 8, 2, 9, 1] → Output: 9
# x=[5, 8, 2, 9, 1]
# ans=lambda x:max(x)
# print(ans(x))
# by sir 
# li =[5, 8, 2, 9, 1]
# max(li,key=lambda x:x)
# 10 Write a lambda function to sort a list of tuples based on the second element.
# Input: [(2,5), (1,2), (4,1)] → Output: [(4,1), (1,2), (2,5)]
li=[(2,5), (1,2), (4,1)]
li=sorted(li,key=lambda x:x[1])
print(li)


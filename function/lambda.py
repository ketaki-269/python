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
ans=lambda x:x+1
print(ans(60))

def maxnum(a,b):
    if a>b:
        return a
    else:
        return b
ans=lambda x,y:x if x>y else y
print(ans(8,70))     
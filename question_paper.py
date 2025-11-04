

# Q.1(a) Write a Python program to change a given string to a newly string
# where the first and last chars have been exchanged.
# Example:
# Input:”welcome”
# Output:”eelcomw”

s="welcome"
ans= s[-1] + s[1:-1]+s[0]
print(ans)


# Or

# Q.1(b) Write a Python program to count the occurrences of each word in a
# given sentence.
# Example:
# Input:”welcome to cybrom”
# Output:{'welcome': 1, 'to': 1, 'cybrom': 1}

# s="welcome to cybrom "
# data=s.split()
# ans={}
# for i in data:
#     ans[i]=ans.get(i,0)+1
# print(ans)


# Q.2(a) Write a Python program to check the given number is prime or not.
# Example1 :
# Input:7
# Output:Prime Number
# Example2 :
# Input:70
# Output:Not Prime Number


# Or

# Q.2(b) Write a Python program to print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# Q.3(a) Write a Python program to get the smallest number from a list.
# Example:
# Input:[4,1,5,6,8]
# Output:1

# Or

# Q.3(b) Write a Python program to find the second smallest number in a
# tuple.
# Example:
# Input:(90,32,45,6,1)
# Output:6

# with fucntion 
# data=(90,32,45,6,1)
# data= sorted(data)
# print(data[1])

#with out function
# data=(90,32,45,6,1)
# minimum =data[0]
# sec_smallest =minimum
# for i in data:
#     if i<minimum:
#         sec_smallest =minimum
#         minimum = i
# print(sec_smallest)        

# Q.3(a) Write a Python program to get the smallest number from a list.
# Example:
# Input:[4,1,5,6,8]
# Output:1

# Or

# Q.3(b) Write a Python program to find the second smallest number in a
# tuple.
# Example:
# Input:(90,32,45,6,1)
# Output:6
# Q.4(a) Write a program to input basic salary of an employee and calculate
# its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
# Or

# Q.4(b) Write a program to find the sum of first and last digit of any number.
# Example:
# Input:34256
# Output:9

# s="34256"
# ans=int( s[-1]) +int(s[0])
# print(ans)
# Note:(Number should be greater than 2 digits)
# Q.5(a) Write a Python script to concatenate the following dictionaries to
# create a new one.
# to extend dictionary we use update
# d1={1:20,2:30}
# d2={2:30,4:40}
# d3={5:50,6:60}
# ans={}
# for i in (d1,d2,d3):
#     ans.update(i)
# print(ans)    
# Or

# Q.5(b)Write a python program to create class using factorial and power
# function.

# class ke under 2 fucntion bananne hai factorial or power 
# or dono ko call kern a hai 




# patterns
# *
# **
# ***
# ****
# *****
# ispe pehle star honga fir space but in vice versa its oppposite
# star or spaces ka combination is pattern hai 

# with single loop 
# print("*"*1+"1"*4)

# *
# **
# ***
# ****
# *****
# n=5
# for i in range (1,n+1):
#     print("*"*i +" "*(n-i))

#  ****
#   ***
#    **
#     *
n=5
for i in range (1,n+1):
    print(" "*i +"*"*(n-i))


# *****
# ****
# ***
# **
# *

# n=5
# for i in range (n):
#     print("*"*(n-i) + " "*i)

#    *
#   **
#  ***
# ****
#*****
# n=5
# for i in range (n):
#     print(" "*(n-i) + "*"*i)

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

#1
#12
#123
#1234
#12345
# n=5
# st=""
# for i in range(1,n+1):
#     st+=str(i)
#     print(st*i+ " "*(n-1)) #galkat


# char to int ord
int to char 
s="128"
for i in range (128):
    print(f"the ASCII value of {i} {} ")
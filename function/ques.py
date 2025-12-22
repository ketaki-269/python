# to store output we use return 
# to print output we use print

#q1 factorial
# 5
# 1*2*3*4*5=120
# def factorial(num):
#     ans=1
#     for i in range(1,num+1):
#         ans*=i
#     return ans
# print(factorial(5))    
# a=factorial(6)
# print(a)

#q2 print 1-10
# (non return type without argu) 
# def print1to10():
#     for i in range (1,11):
#         return i 
# print1to10(print1to10())    

# def print1to10():
#     for i in range (1,11):
#        print(i) 
#        return i 
# print1to10(print1to10())   

# def print1to10():
#     for i in range (1,11):
#        print(i,end="") 
# print1to10(print1to10())   

# # do all que with return or non return
# # que with return type  
# # q-3 prime number
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def prime_numbers(limit):
#     primes = []
#     for n in range(2, limit + 1):
#         if is_prime(n):
#             primes.append(n)
#     return primes
# print(prime_numbers(10))
# a = prime_numbers(20)
# print(a)
#diffrent way
# def is_prime(num):
#     return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
# def prime_numbers(limit):
#     return [n for n in range(2, limit + 1) if is_prime(n)]
# print(prime_numbers(10))
# a = prime_numbers(20)
# print(a)

# q-4 sum of natural number 
# def sum_natural(num):
#     total = 0
#     for i in range(1, num + 1):
#         total += i
#     return total
# print(sum_natural(5))
# a = sum_natural(10)
# print(a)

# q-5 reverse number 
# def reverse_number(num):
#     rev = 0
#     while num > 0:
#         rev = rev * 10 + num % 10
#         num //= 10
#     return rev
# print(reverse_number(1234))
# a = reverse_number(9876)
# print(a)

#q-6 pallindrom
# def is_palindrome(num):
#     original = num
#     rev = 0
#     while num > 0:
#         rev = rev * 10 + num % 10 
#         num //= 10
#     if original == rev:
#         return "Palindrome number"
#     else:
#         return "Not a palindrome number"
# print(is_palindrome(121))
# a = is_palindrome(123)
# print(a)
 
# q-7 amstrong
# def is_armstrong(num):
#     temp = num
#     count = len(str(num))
#     result = 0
#     while temp > 0:
#         result += temp % 10  ** count
#         temp //= 10
#     if result == num:
#         return "Armstrong number"
#     else:
#         return "Not an Armstrong number"
# print(is_armstrong(153))
# a = is_armstrong(123)
# print(a)

#que with non return type 
# que-3 WAP t print prime no. 
# def is_prime(num):
#     return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# def prime_numbers(limit):
#     primes = [n for n in range(2, limit + 1) if is_prime(n)]
#     print(primes)
# prime_numbers(10)
# prime_numbers(20)

# Que-4 Sum of natural numbers
# def sum_natural(num):
#     total = 0
#     for i in range(1, num + 1):
#         total += i
#     print("Sum of natural numbers", num, "is:", total)
# sum_natural(5)


# Que -5 Reverse number
# def reverse_number(num):
#     rev = 0
#     while num > 0:
#         rev = rev * 10 + num % 10 
#         num //= 10
#     print("Reversed number:", rev)
# reverse_number(1234)


# Que-6 Palindrome number
# def is_palindrome(num):
#     original = num
#     rev = 0
#     while num > 0:
#         rev = rev * 10 + num % 10
#         num //= 10
#     if original == rev:
#         print(original, "is a Palindrome number")
#     else:
#         print(original, "is Not a Palindrome number")
# is_palindrome(121)



# Q-7 Armstrong number
# def is_armstrong(num):
#     temp = num
#     count = len(str(num))
#     result = 0
#     while temp > 0:
#         result += temp%10 ** count
#         temp //= 10
#     if result == num:
#         print(num, "is an Armstrong number")
#     else:
#         print(num, "is Not an Armstrong number")
# is_armstrong(153)

#10-10-2025
# do all que with slicing 
# sum of all elements in a list
# def sum_of_list(data): 
#    ans=0
#    for i in data:
#       ans+=1
#       return ans
# li=[] 
# ans=sum_of_list(li)
# print(li)     


# 11-10-2025
# important for interview
# print fucntion - use to display value
# def print1to10():
#     for i in range(1,11):
#         print(i)
# print1to10() 
# # return function 
# def print1to10():
#     for i in range(1,11):
#         return i
# print1to10()    
#next function - use to print value again and again 
# def print1to10():
#     for i in range(1,11):
#         yield i
# ans= print1to10()    
# print(next(ans))
# print(next(ans))
# print(next(ans))
# print(next(ans))
#important
# yield function-  also know as generator ,it works on single memory 
# def print1to10():
#     for i in range(1,11):
#         yield i
# ans= print1to10()
# for i in ans:
#     print(i,end=" ")


#we do not use retyurn in large data set , as it allocate the memory till end 
# def print1to10():
#     for i in range (1,11):
#             for j in range (10,20):
#              return j
#     return i 
# ans= print1to10()
# print(ans)
#
# we can use generator in large data set 
# def print1to10():
#     for i in range (1,11):
#             for j in range (10,20):
#              yield j
#     yield i 
# ans= print1to10()
# print(ans)

# types of argument 
# 1.positional argument - 
# 2. keyword argument
# 3.defoult argument
# 4.valriable length argument
# 5.keyword variable length argument

# 1.positional argument - sunction jitne argument mang raha hai use utne hi chahiye hote hai 
# def student_data(num,rolno):
#     print(f"hello(name)your rollno is (rollno)")
# student_data("raj",1023)
# 2.keyword argument -  like ispe specify kerdengi key deke jise name name me hi jake store ho bhale line of  code me kahi bhi diya ho 
# def student_data(num,rollno):
#     print(f"hello(name)your rollno is (rollno)")
# student_data(rollno=1023,name="raj")
# 3.defoult argument -   single fucntion me jab multiple task perfrom kerne ho toh iska jada use hota hai 
# def addtion (a,b):
#     print(a+b)
# addtion(10,50)    
# like if in this ager kisi ne ek hi argument diya kisine toh vo wrroe na deke second value defuat lele 
# jese ese 
# def addtion (a=0,b=0):
#     if b==0:
#         print(a)
#     elif a==0 and b==0:
#         print("both are zero")
#     elif a!=0 and b!=0:
#        print(a+b)    
#     else:     
#      print(a+b)
# addtion()

# fucntion overloading defualt funtion ke trough hi archive hoti hai python me kyuki  vese fucntion overloading pyhton me nhi hoti 
# 4.valriable length argument-  * is use  or ye list me nhi ayegna
# def sumofallnumber(*num):
#    ans=0
#    for i in num:
#       ans+=i
#    return ans
# sumofallnumber(1,2,3,4,6,34,6,6)
# 5.keyword variable length argument - ** is use ,it use to store data in key and value pattern 
# def printdata(**data):
#     for i,j in data.items():
#         print(f"hello {i} rollno {j}")
# printdata(raj=101,jatin=20)        

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
#         digit = num % 10
#         rev = rev * 10 + digit
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
#         digit = num % 10
#         rev = rev * 10 + digit
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
#         digit = temp % 10
#         result += digit ** count
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
#     print("Sum of natural numbers up to", num, "is:", total)
# sum_natural(5)
# sum_natural(10)

# Que -5 Reverse number
# def reverse_number(num):
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#     print("Reversed number:", rev)

# reverse_number(1234)
# reverse_number(9876)

# Que-6 Palindrome number
# def is_palindrome(num):
#     original = num
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#     if original == rev:
#         print(original, "is a Palindrome number")
#     else:
#         print(original, "is Not a Palindrome number")

# is_palindrome(121)
# is_palindrome(123)


# Q-7 Armstrong number
def is_armstrong(num):
    temp = num
    count = len(str(num))
    result = 0
    while temp > 0:
        digit = temp % 10
        result += digit ** count
        temp //= 10
    if result == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is Not an Armstrong number")

is_armstrong(153)
is_armstrong(123)

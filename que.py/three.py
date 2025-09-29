#8 check number is palindrome  number or not by number count ?
# num = int(input("Enter a number: "))
# real=num
# reversed =0
# while (num != 0):
#         remainder = num % 10
#         reversed = reversed * 10 + remainder
#         num /= 10
    

# if real == reversed:
#     print ("Palimdrome")
# else:
#     print("Not a Palindrome")     

#1  print table of 2 
# num=int(input("Enter a number : "))
# i=int
# ans=num*i
# for i in range (1,11):
#     print (ans)

#2  print table of 1-10

# for i in range (1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()    

#3  target sum ?
# ex={1,2,6,7}    target =7
# ouput=1,6

# list=[1,2,6,7]
# target=7
# for i in range (len(list)):
#     for j in range (i+1,len(list)):
#         if list[i]+ list[j]==target:
#             print (list[i],list[j])


    
   


#4  ex{3,6,1,5,4} target = 10
# output =6,4 

# list=[3,6,1,5,4]
# target=10
# ans=False
# for i in range (len(list)):
#     for j in range (i+1,len(list)):
#         if list[i]+ list[j]==target:
#             print (list[i],list[j])
#             ans = True
#     if ans==True:
#         break
        
#5  print prime number ?        
# n = int(input("Enter a number: "))

# print("Prime numbers up to", n, "are:")

# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# n = int(input("enter a number :"))
# count = 0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j%i==0 and j%n==0:
#             count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")





    # by sir 

# n = int(input("enter a number :"))
# count = 0
# for i in range(1,n+1):
#         if n%i==0:
#             count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")

# 27-9-25

#6 move zero in the end of the list?
# ex-{3,0,5,6,0,7}
# out-{3,5,6,7,0,0}

# list =[3,0,5,6,0,7]
# count = 0
# list= []
# for i in list:
#     if i!=0:
#         list.append(i)
#     else:
#         count+=1
# for i in range (count):
#     list.append(0)
# print (list)


# nonzero=[]
# zero=[]
# list =[3,0,5,6,0,7]
# for i in range (len(list)):
#     if list [i] !=0:
#         nonzero.append(list[i])
#     else:
#         zero.append(list[i])
# print(nonzero+zero)       



# num = [3, 0, 5, 6, 0, 7]

# # Move zeros into new list 
# result = [i for i in num if i != 0 ]+ [0] * num.count(0)

# print(result)  


# nums = [3, 0, 5, 6, 0, 7]

# pos = 0
# for num in nums:
#     if num != 0:
#         nums[pos] = num
#         pos += 1

# while pos < len(nums):
#     nums[pos] = 0
#     pos += 1

# print(nums) 


#7  check number is armstrong number or not or for three digit  ?
# ex -153 


# num = int(input("Enter a number: "))
# real = num
# result = 0
# while real != 0:
#     remainder = real % 10
#     result += remainder ** 3   
#     real //= 10  

# if result == num:
#     print(num, "is an Armstrong number.")
# else:
#     print(num, "is Not an Armstrong number.")

#8 check number is armstrong number or not by number count ?
# ex- 1634 or any number 

# num = int(input("Enter a number: "))
# real = num
# result = 0

# count = len(str(num))

# while real != 0:
#     remainder = real % 10
#     result += remainder ** count   
#     real //= 10  

# if result == num:
#     print(num, "is an Armstrong number.")
# else:
#     print(num, "is Not an Armstrong number.")


# 9. remove duplicate data from the list 
# ex- [1,1,2,2,3,4,5,3]
# o/p - [1,2,3,4,5]
   
# list =[1,1,2,2,3,4,5,3]
# result = []
# for i in list:
#     if i not in result:
#         result.append(i)
# print(result)   




li =[1,1,2,2,3,4,5,3]
li= set [li]
li=list(li)
print(li)

# q- add digit  till it become single digit here we will use two loops 
# ex - 155
# 1+5+5 = 11
# 1+1 =  2

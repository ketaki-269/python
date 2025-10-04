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




# li =[1,1,2,2,3,4,5,3]
# li= set [li]
# li=list(li)
# print(li)

# q- 10 add digit  till it become single digit here we will use two loops 
# ex - 155
# 1+5+5 = 11
# 1+1 =  2

# num = int(input("Enter a number: "))
# while num >= 10:  
#     temp = num
#     sum_digits = 0

#     while temp > 0:   
#         sum_digits += temp % 10
#         temp //= 10
#     num = sum_digits   
# print("Single digit:", num)


# 11.  fibbonaci series 

# num = int (input("Enter a number for fibonacci series: "))
# a=0
# b=1
# count = 0
# while num > count:
#     print(a , end=" ")
#     a, b=b ,a+b
#     count += 1

# num =int(input("Enter the number: "))
# a=0
# b=1
# for i in range(num) :
#     print(a, end=" ")
#     a, b =b ,a+b

# num =int(input("Enter the number: "))
# a=0
# b=1
# for i in range(num) :
#     if i == 0: 
#      print(a, end=" ")
#      continue
#     if i ==1:
#        print(b,end=" ")
#        continue
#     c =a+b
#     a =b
#     b =c
#     print(b, end=" ")

# num =int(input("Enter the number: "))
# a=0
# b=1
# print(a,b, end=" ")
# for i in range(num-2) :
#     c= a+b
#     a= b
#     b=c
#     print(b, end=" ")


# 12. count the frequency of each element in list

# data={1:2,2:6}
# data[4]=7
# print(data.get(90,0))               (0 vo value hai jo rreturn honi hai)
# print(data)


# li= [1,4,3,2,4,5,4,4,2,2,2,1]                #( list )
# data={}                                       #(dictionary create kerdi)
# for i in li:                                  #(ek ek kerke data ayenga )
#     data[i] = data.get(i,0)+1                  # key change nhi hongi hamesha value change hongi 
# print(data)    




# 13. count the frequency of word in string 
# ex= stri="helloword" output  {h:1,e:1,l:3}

# stri="helloword"
# data={}
# for i in stri:
#     data[i]=data.get(i,0)+1
# print(data)    


#14 .convert string into set of character 
# like- store this string stri="helloword" into set 
# stri="helloword"
# data = set()
# print(stri)

# stri="helloword"
# data = set(stri)
# print(data)

# # by sir 
# stri="helloword"
# ans=set()
# for i in stri:
#     ans.add(i)
# print(ans)    

#15.find a unique word from a sentence (hello word) using a set 
# stri="helloword"
# data={}
# ans=set()
# for i in stri:
#     data[i]=data.get(i,0)+1

# for key,value in data.items():
#     if value==1:
#         ans.add(key)

# print(ans)

#16 write a program to create a dictionary where keyy are number from 1-10 and values are their square.

# data={}
# for i in range(1,11):
#     data[i]=i*i
# print(data)    

#17 give n a dictionary of students and marks ,find the student with the highest marks .

# student_marks={
#     "raj":50,
#     "rahul":80,
#     "rohit":90,
#     "radhika":20
# }
# maximum = student_marks["raj"]
# topper=""
# for student,marks in student_marks.items():
#     if marks>maximum:
#         topper=student
#         maximum=marks

# print(f"the topper name is {topper} with  {maximum} marks")       


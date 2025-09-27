# print table of 2 
# num=int(input("Enter a number : "))
# i=int
# ans=num*i
# for i in range (1,11):
#     print (ans)

# print table of 1-10

# for i in range (1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()    

# target sum ?
# ex={1,2,6,7}    target =7
# ouput=1,6

# list=[1,2,6,7]
# target=7
# for i in range (len(list)):
#     for j in range (i+1,len(list)):
#         if list[i]+ list[j]==target:
#             print (list[i],list[j])


    
   


# ex{3,6,1,5,4} target = 10
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
        
# print prinme number ?        
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

n = int(input("enter a number :"))
count = 0
for i in range(1,n+1):
        if n%i==0:
            count+=1
if count==2:
    print("prime number")
else:
    print("not prime number")

# move xero in the end of the list?
# ex-{3,0,5,6,0,7}
# out-{3,5,6,7,0,0}
#creation
# list=[10,"A","B",20,30]
# print(list)
# print(type(list))

#creation with dynamic input
# list=[]
# n=int(input("Enter number of elements going to be in List"))
# for i in range(0,n):   
#  i=input()
#  list.append(i)
# print(list)

#accessing elements of list
# this can be done in to ways by using indexing or slicing 
#  with indexing
# list=[10,"A","B",20,30] # like we we want to access "A" from this we can easily access this with its index number 
# print(list[1])
# print(list[-1])


#with slicing
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])

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
# n=[1,2,3,4,5,6,7,8,9,10]
# print(n[2:7:2])
# print(n[4::2])
# print(n[3:7])
# print(n[8:2:-2])
# print(n[4:100])

#mutability
# list=[1,2,3,5,6]
# print(list)
# list[3]=4
# print(list)




#functions(inbuild)
# 1.append
# list=[1,2]
# list.append("A")
# print(list)

# 2.insert
# list=[1,2,4]
# list.insert(2,3)
# print(list)
# 3.extend
# list=[1,2,3,4]
# list2=[5,6,7,8]
# list.extend(list2)
# print(list)

# 4.remove
# list=[1,2,6,3,4,5,6]
# list.remove(6)
# print(list)
# 5.pop 
# list=[1,2,3,4,5,6]
# list.pop()
# print(list)
# 6.len
# list = [1,2,3,4,5,5,6,0,6,7,8,9]
# print(len(list))
# 7.count
# list = [1,2,3,4,5,5,6,0,6,7,8,9]
# print(list.count(6))
# 8.Index
# list=[1,2,3,4,5] 
# print(list.index(2)) 
# 9.reverse 
# list=[1,2,3,4]
# list.reverse()
# print(list)
# 10.sort
#list=[1,2,"A","B"] # it will give error as while use sort we can only sort same type of data
# list=[4,2,683,25,62,7,1,4,0]
# list.sort()
# print(list)
# 11.clear
# list=[4,2,683,25,62,7,1,4,0]
# list.clear()
# print(list)


#traversing -  "traversing" refers to the process of visiting each element within a data structure, such as a list, string, tuple, array, tree, or graph, typically to perform an operation on each element. This operation could be printing the element, searching for a specific value, modifying the element, or applying a function to it.
# WAP if the elements of list is greater than list length then incremenets the value  
# list=[0,1,2,3,6]
# i=0
# while i<len(list):
#   if list[i]>len(list):
#    list[i] +=1
#   i += 1 
# print(list)


#with for loop
# n=[0,1,2,3,4,5,6,7,8,9,10]
# for n in n:
#   print(n)


#nested list
# list=[1,2,3,4,[2,3,4]]
# print(type(list))

#aliasing
list_a = [1, 2, 3]
list_b = list_a
print(list_b)
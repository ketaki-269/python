#1 list

# li =[]
# for i in range (1,11):
#     li.append(i)
# print (li)    

# li= [ i for i in range (1,11)]
# print(li)

# WAP to stor data of table
# data=[i for i in range (2,21,2)]
# print (data)

# WAP evenn num.
# data=[i for i in range (1,21,) if i%2==0]
# print (data)


# WAP odd num.
# data=[i for i in range (1,21,) if i%2!=0]
# print (data)

#WAP square of a number from 1 to 10
# data= [i**2 for i in range(1, 11)] 
# print(data)



#WAP sqaure of num which is divisible by 3
# data=[i for i in range (1,21,) if i**2%3]
# print (data) galat 

# # by sir 
# data= [i for i in range(1, 21) if i%3==0] 
# print(data)



#WAP sqaure of num which is divisible by 5,6
# data=[i for i in range (1,21,) if i**2 % 5 and 6]
# print (data) galat 
# by sir 
# data= [i for i in range(1, 40) if i%5==0  and i%6==0] 
# print(data)

#WAP store only vowels from th list ex= "pyhton world"-output= [o,o]
# s= "python world" 
# data= [ i for i in s if i in "aeiouAEIOU"]
# print(data)

#WAP store only positive data in a list  ex - [-1,2,4,-8,7,2,-8,-2]  output=[2,4,7,2,]
# data= [ -1,2,4,-8,7,2,-8,-2]
# li = [i for i in data if i>=0]
# print(li)


# WAP to store even and odd in string

# for i in range (1,11):
#     if i%2==0:
#         print ("even")
#     else :
#         print("odd")    

# ans = ["even" if i%2==0  else "odd" for i in range(1,11)]
# print( ans)

#WAP to check the person is pass or fail passing marks is above 33
# li=[11,56,34,67,89,,23,16,90] output = [56,67,89,99,34]
# li = [11, 56, 34, 67, 89, 23, 16, 90]
# passed = [mark for mark in li if mark > 33]
# print("Passed students' marks:", passed)


# WAP to only store a word which length is above 5
# li = ["python", "c++","java","cybrom"] output=["python","cybrom "]
# li = ["python", "c++", "java", "cybrom"]
# result = [word for word in li if len(word) > 5]
# print("Words with length above 5:", result)

# WAP to convert each character in a string= "world" in uppecase  output = "WORLD"
# string = "world"
# result = string.upper()
# print(result)

#WAP to add 5 to each number in list    
li = [1, 2, 3, 4]
result = [i + 5 for i in li]
print(result)

#2 set

# set ={}
# for i in range (1,11):
#     set.append(i)
# print (li)    

# set= { i for i in range (1,11)}
# print(set)
#3 tuple (generator)

#4dictionary
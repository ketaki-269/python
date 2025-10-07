#1 list

# li =[]
# for i in range (1,11):
#     li.append(i)
# print (li)    

# li= [ i for i in range (1,11)]
# print(li)

# WAP to store data of table
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
# li = [1, 2, 3, 4]
# result = [i + 5 for i in li]
# print(result)


# List Comprehension Questions

# 1. Generate a list of even numbers from 1 to 20.
# data=[i for i in range (1,21,) if i%2==0]
# print (data)
# 2. Convert all characters of a string "python" into uppercase.
# string= "python"
# output=string.upper()
# print(output)

# 3. Create a list of cubes of odd numbers from 1 to 15.
# data=[i*3 for i in range (1,16,) if i%2!=0]
# print (data)
# 4. Extract vowels from the string "comprehension".
# s= "comprehension" 
# data= [ i for i in s if i in "aeiouAEIOU"]
# print(data)
# 5. From a list [10, 25, 30, 45, 60, 75, 90], create a new list containing only numbers greater than 40.
# li = [10, 25, 30, 45, 60, 75, 90]
# result = [i for i in li if i>40]
# print(result)

# 6. Create a list of the first letter of each word in ["apple", "banana", "cherry"].
# li = ["apple", "banana","cherry"]
# result= [ i[0] for i in li ]
# print(result)
# 7. Flatten a nested list [[1,2],[3,4],[5,6]] into a single list. in comprehension
# list =  [[1,2],[3,4],[5,6]]
# li = [[1,2],[3,4],[5,6]]
# data = [i for list in li  for i in list]
# print(data)


# 8. Create a list of (x, y) pairs where both are between 1 and 3 (Cartesian product).


# 9. Extract all words longer than 4 letters from "Python list comprehension is powerful".
# li = ["Python" ,"list" , "comprehension"  , "is" , "powerful"]
# # li= "Python list comprehension is powerful"
# result = [i for i in li if len(i) > 4]
# print(result)

# sentence = "Python list comprehension is powerful"
# result = [word for word in sentence.split() if len(word) > 4]
# print(result)

# 10. From a sentence, extract words that start with a vowel.
s = "From a sentence, extract words that start with a vowel."
result = [i for i in s.split() if i[0] in 'aeiouAEIOU']
print(result)


#---------------------------------------------------------------------------------------------------
#2 set
# set ={}
# for i in range (1,11):
#     set.append(i)
# print (li)    

# set= { i for i in range (1,11)}
# print(set)

# 1. Create a set of squares from 1 to 10. {x**2 for x in range(1,11)}
# data={i**2 for i in range (1,11,) }
# print (data)
# 2. Create a set of even numbers from 1 to 20.
# data={i for i in range (1,21,) if i%2==0}
# print (data)
# 3. Create a set of characters from "banana".
# 4. From [1,2,2,3,4,4,5], create a set of unique elements.
# 5. Create a set of numbers from 1–30 divisible by 3 or 5.
# 6. Generate a set of cubes for numbers 1–10 but only include cubes < 100.
# 7. Create a set of squares for only odd numbers between 1 and 15.
#------------------------------------------------------------------------------------------
#3 tuple (generator)
# 1. Create a tuple of squares from 1 to 5.
# tuple(x**2 for x in range(1,6))
# 2. Create a tuple of even numbers from 2 to 10.
# 3. Convert a list ['a', 'b', 'c'] to uppercase letters as a tuple.
# 4. Create a tuple of cubes of numbers from 1 to 7.
# 5. Create a tuple of lengths of words in ["hi", "python", "list"].
# 6. Generate a tuple of numbers divisible by 7 between 1 and 50.
# 7. Convert the characters of a string "hello" into a tuple.
# 8. Create a tuple of all vowels present in "education".
#-------------------------------------------------------------------------------------------

#4dictionary
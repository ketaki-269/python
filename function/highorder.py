# 1 map- returns multiple data
# 2.filter  - returns only that data which fullfill the  condition
# 3. reduce  - returns single data
# commun in 3 ( function, iterable - object)


#add 10 to each i a list
# [1,2,3],o/p[11,12,13]
# li=[1,2,3]
# ans=list(map(lambda x:x+10,li))
# print(ans)

# questions 
# 1. Convert a list of integers into their squares using map().
# Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]
# li=[1,2,3,4]
# ans=list(map(lambda x:x**2,li))
# print(ans)
# 2. Convert all strings in a list to uppercase using map().
# Input: ["python", "map", "function"] → Output: ["PYTHON", "MAP", "FUNCTION"]
# li=["python", "map", "function"]
# ans=list(map(lambda x:x.upper(),li))
# print(ans)
# 3. Convert a list of integers to strings using map().
# Input: [1, 2, 3] → Output: ["1", "2", "3"]
# li=[1,2,3]
# ans=list(map(lambda x:str(x),li))
# print(ans)
# 4. Find the length of each word in a list using map().
# Input: ["apple", "banana", "kiwi"] → Output: [5, 6, 4]
# li= ["apple", "banana", "kiwi"]
# ans=list(map(lambda x:len(x),li ))
# print(ans)
# 5. Double all numbers in a list using map().
# Input: [3, 6, 9] → Output: [6, 12, 18]
# li=[3,6,9]
# ans=list(map(lambda x:x*2,li))
# print(ans)

Add 10 to every number in a list using map().
Input: [1, 2, 3] → Output: [11, 12, 13]
7. Convert temperatures from Celsius to Fahrenheit using map().
Formula: (C * 9/5) + 32
Input: [0, 20, 30] → Output: [32.0, 68.0, 86.0]
8. Extract the first character of each word using map().
Input: ["apple", "banana", "cherry"] → Output: ["a", "b", "c"]
9. Check if each number in a list is even or odd using map().
Input: [1, 2, 3, 4] → Output: ["Odd", "Even", "Odd", "Even"]
10. Convert a list of binary strings to integers using map().
Input: ["101", "111", "1001"] → Output: [5, 7, 9]
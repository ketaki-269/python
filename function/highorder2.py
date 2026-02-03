# 2.filter 

# lis=[14,13,54,33,57,29,31,10]
# ans=list(filter(lambda x: x>20,lis))
# print (ans)
#1. Filter even numbers from a list.
# Input: [1, 2, 3, 4, 5, 6] → Output: [2, 4, 6]
li=[1,2,3,4,5,6]
ans=list(filter(lambda x: x%2==0,li))
print (ans)
# 2 Filter odd numbers from a list.
# Input: [10, 15, 20, 25, 30] → Output: [15, 25]
# li=[10,15,20,25,30]
# ans=list(filter(lambda x: x%2!=0,li))
# print (ans)
#3  Filter numbers greater than 50.
# Input: [10, 60, 45, 70, 30] → Output: [60, 70]
# li=[10, 60, 45, 70, 30]
# ans=list(filter(lambda x: x>50,li))
# print (ans)
#4  Filter strings with length greater than 4.
# Input: ["apple", "bat", "ball", "hi"] → Output: ["apple", "ball"]
# li=["apple", "bat", "ball", "hi"]
# ans=list(filter(lambda x: len(x)>4,li))
# print (ans)
#5  Filter positive numbers.
# Input: [-2, 0, 5, 9, -7, 3] → Output: [5, 9, 3]
# li=[-2, 0, 5, 9, -7, 3]
# ans=list(filter(lambda x: x>0,li))
# print (ans)

#6 Filter words that start with the letter 'a'.
# Input: ["apple", "banana", "avocado", "cherry"] → Output: ["apple", "avocado"]
# li = ["apple", "banana", "avocado", "cherry"]
# ans = list(filter(lambda x: x[0] == 'a', li))
# print(ans)
#7 Filter palindrome words.
# Input: ["madam", "python", "level", "wow", "cat"] → Output: ["madam", "level", "wow"]
# li = ["madam", "python", "level", "wow", "cat"]
# ans = list(filter(lambda x: x == x[::-1], li))
# print(ans)
#8 Filter vowels from a list of characters.
# Input: ['a', 'b', 'e', 'i', 'o', 'p', 'u'] → Output: ['a', 'e', 'i', 'o', 'u']
# li = ['a', 'b', 'e', 'i', 'o', 'p', 'u']
# ans = list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], li))
# print(ans)
#9 Filter numbers    divisible by both 3 and 5.
# Input: [10, 15, 30, 42, 60, 70] → Output: [15, 30, 60]
# li=[10, 15, 30, 42, 60, 70]
# ans=list(filter(lambda x: x%3==0 and x%5==0,li))
# print (ans)

#10 Filter names that contain the letter 'a' or 'A'.
# Input: ["Rahul", "Raj", "Python", "Code"] → Output: ["Rahul", "Raj"]
li = ["Rahul", "Raj", "Python", "Code"]
ans = list(filter(lambda x: 'a'  in x, li))
print(ans)

#11 Filter numbers whose square is greater than 50.
# Input: [2, 4, 6, 8, 10] → Output: [8, 10]
# li = [2, 4, 6, 8, 10]
# ans = list(filter(lambda x: x**2>50, li))
# print(ans)
#12 Filter words ending with 'ing'.
# Input: ["running", "play", "eating", "dance"] → Output: ["running", "eating"]
# li = ["running", "play", "eating", "dance"]
# ans = list(filter(lambda x: x.endswith('ing'), li))
# print(ans)
#13 Filter elements that are strings from a mixed list.
# Input: [1, "apple", 3.5, "banana", True, "cherry"] → Output: ["apple", "banana", "cherry"]





#14 Filter employees older than 25 from a list of tuples (name, age).
# Input: [("Rohit", 22), ("Rahul", 26), ("Raj", 30)]
# Output: [("Rahul", 26), ("Raj", 30)]
# li=[("Rohit", 22), ("Rahul", 26), ("Raj", 30)]
# ans = list(filter(lambda x: x[1]>25, li))
# print(ans)
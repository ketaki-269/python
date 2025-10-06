# Set Questions

# 1. Create a set with numbers 1–10
# Example: {1,2,3,4,5,6,7,8,9,10}

# set={1,2,3,4,5,6,7,8,9,10}
# print(set)

# 2. Check if an element exists
# "apple" in {"apple","banana","cherry"} → True


# fruits = {"apple", "banana", "cherry"}  
# fruit= input("Enter fruit:")

# if fruit in fruits:
#     print("Yes, 'apple' is present in the set.")
# else:
#     print("No, 'apple' is not present in the set.")


# 3. Convert list with duplicates into a set
# [1,2,2,3,4,4] → {1,2,3,4}

# numbers_list = [1, 2, 2, 3, 4, 4]

# numbers_set = set(numbers_list)

# print(numbers_set)


# 4. Find length of a set
# {10,20,30} → length = 3

# Define a set
numbers = {10, 20, 30}

length = len(numbers)

print("Length of the set:", length)


# 5. Remove duplicate words from a sentence
# "this is is a test" → {'this','is','a','test'}

sentence = "this is is a test"

unique_words = set(sentence.split())

print(unique_words)


# 6. Unique values from list of tuples
# [(1,2),(2,3),(3,4)] → {1,2,3,4}

pairs = [(1, 2), (2, 3), (3, 4)]

unique_values = set()

for pair in pairs:
    unique_values.update(pair)

print(unique_values)



# 7. Uncommon elements between lists
# L1=[1,2,3], L2=[2,3,4] → {1,4}
# 8. Elements in all three lists
# [1,2,3], [2,3,4], [3,4,5] → {3}



# Dictionary Questions

# 1. Create dictionary of students
# {"Aman":85, "Ravi":92, "Neha":78}



# 2. Access value by key
# marks["Ravi"] → 92



# 3. Add/Update value
# marks["Neha"]=80



# 4. Delete a key
# del marks["Aman"]



# 5. Check if key exists
# "Ravi" in marks → True



# 6. Lists to dictionary
# keys=["a","b"], vals=[1,2] → {"a":1,"b":2}



# 7. Invert dictionary
# {"a":1,"b":2} → {1:"a",2:"b"}



# String Questions

# 1. Length without len()
# "hello" → 5



# 2. Reverse string
# "python" → "nohtyp"



# 3. Count vowels & consonants
# "apple" → vowels=2, consonants=3




# 4. Palindrome
# "madam" → True



# 5. Remove spaces
# "I am here" → "Iamhere"



# 6. Replace substring
# "I like apple".replace("apple","mango") → "I like mango"



# 7. Longest word
# "I love programming" → "programming"



# 8. Count digits, alphabets, special
# "Hello123!" → alphabets=5, digits=3, special=1
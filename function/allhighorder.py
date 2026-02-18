#1 Sum of squares of even numbers using map, filter, reduce
# Problem: nums = [1,2,3,4] → 2^2 + 4^2 = 4 + 16 = 20.
# from functools import reduce
# list=[1,2,3,4]
# ans= reduce(lambda x,y:x+y,map(lambda x:x*x,filter (lambda x:x%2==0,list)))
# print(ans)

# filter use to filter even num
# map lambda use to sum of square


#2 Convert all strings in a list to uppercase using map()
# Problem: words = ["hello", "world"] → ['HELLO', 'WORLD']
# words = ["hello", "world"]
# ans = list(map(lambda x: x.upper(), words))
# print(ans)

#3 Add 10 to each number using map()
# Problem: nums = [5, 10, 15] → [15, 20, 25]
# num = [5, 10, 15]
# ans = list(map(lambda x: x + 10, num))
# print(ans)

#4 Filter out even numbers using filter()
# # Problem: nums = [1,2,3,4,5] → [1,3,5]
# num = [1, 2, 3, 4, 5]
# ans = list(filter(lambda x: x % 2 != 0, num))
# print(ans)

#5 Filter strings starting with 'A'
# Problem: names = ['Alice', 'Bob', 'Alex'] → ['Alice', 'Alex']
# names = ['Alice', 'Bob', 'Alex']
# ans = list(filter(lambda x: x.startswith('A'), names))
# print(ans)

#6 Sum of numbers using reduce()
# Problem: nums = [1,2,3,4] → 10
# from functools import reduce
# nums = [1, 2, 3, 4]
# ans = reduce(lambda x, y: x + y, nums)
# print(ans)

#7 Product of numbers using reduce()
# Problem: nums = [2,3,4] → 24
# from functools import reduce
# nums = [2, 3, 4]
# ans = reduce(lambda x, y: x * y, nums)
# print(ans)

#8 Filter words with length > 5
# Problem: words = ['apple','banana','kiwi','avocado'] → ['banana','avocado']
# word = ['apple', 'banana', 'kiwi', 'avocado']
# ans = list(filter(lambda x: len(x) > 5, word))
# print(ans)

#9 Convert integers to strings using map()
# # Problem: nums = [1,2,3] → ['1','2','3']
# num = [1, 2, 3]
# ans = list(map(lambda x: str(x), num))
# print(ans)

#10 Find maximum using reduce()
# Problem: nums = [3,7,1,9,4] → 9
# from functools import reduce
# num = [3, 7, 1, 9, 4]
# ans = reduce(lambda x, y: x if x > y else y, num)
# print(ans)

#average

#1 Squares only of even numbers using map()
# Problem: nums = [1,2,3,4,5] → [4, 16]
# num = [1, 2, 3, 4, 5]
# ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, num)))
# print(ans)

#2 Filter palindromes using filter()
# Problem: words = ['level', 'test', 'radar', 'hello'] → ['level','radar']
# word = ['level', 'test', 'radar', 'hello']
# ans = list(filter(lambda x: x == x[::-1], word))
# print(ans)

#3 Concatenate strings using reduce()
# Problem: parts = ['I', 'love', 'Python'] → 'I love Python'
# from functools import reduce
# part = ['I', 'love', 'Python']
# ans = reduce(lambda x, y: x + ' ' + y, part)
# print(ans)

#4 Convert Celsius to Fahrenheit using map()
# Problem: c = [0, 20, 37] → [32.0, 68.0, 98.6]
# a = [0, 20, 37]
# ans = list(map(lambda x: round((x * 9/5) + 32, 1), a))
# print(ans)

#5 Remove None or empty strings using filter()
# Problem: items = ['a', '', None, 'b'] → ['a','b']
# items = ['a', '', None, 'b']
# ans = list(filter(lambda x: x not in [None, ''], items))
# print(ans)

#6 Find longest word using reduce()
# Problem: words = ['hi','hello','greetings'] → 'greetings'
# from functools import reduce
# words = ['hi', 'hello', 'greetings']
# ans = reduce(lambda x, y: x if len(x) > len(y) else y, words)
# print(ans)

#7 Filter people aged 18+ from list of tuples
# Problem: people = [('A',17),('B',20)] → [('B',20)]
# peoples = [('A',17), ('B',20)]
# ans = list(filter(lambda x: x[1] >= 18, peoples))
# print(ans)

#8 Extract first names using map()
# Problem: full = ['Mahesh Soni', 'John Doe'] → ['Mahesh', 'John']
# full = ['Mahesh Soni', 'John Doe']
# ans = list(map(lambda x: x.split()[0], full))
# print(ans)

#9 Double only even numbers using filter() + map()
# Problem: nums = [1,2,3,4] → [4,8]
# nums = [1, 2, 3, 4]
# ans = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
# print(ans)

#10 Average using reduce()
# Problem: nums = [10,20,30] → 20.0
# from functools import reduce
# nums = [10, 20, 30]
# total = reduce(lambda x, y: x + y, nums)
# ans = total / len(nums)
# print(ans)


# # hard
#1 From list of dicts: filter salary > 50000 and map names
# Problem:
# emps = [{'name':'A', 'salary':60000},{'name':'B', 'salary':40000}]
# Return ['A']
# emps = [
#     {'name': 'A', 'salary': 60000},
#     {'name': 'B', 'salary': 40000}
# ]
# ans = list(map(lambda x: x['name'], filter(lambda x: x['salary'] > 50000, emps)))
# print(ans)

#2 Sum of squares of even numbers using map, filter, reduce
# Problem: nums = [1,2,3,4] → 2^2 + 4^2 = 4 + 16 = 20
# from functools import reduce
# nums = [1, 2, 3, 4]
# ans = reduce(lambda x, y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
# print(ans)

#3 Uppercase words longer than 3 letters using map + filter
# Problem: words = ['a','hello','sun','moon'] → ['HELLO','MOON']
# words = ['a', 'hello', 'sun', 'moon']
# ans = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 3, words))) 
# print(ans)

#4 Count total characters across strings using map() + reduce()
# Problem: ['hi','there'] → 7 (2 + 5)
# from functools import reduce
# words = ['hi', 'there']
# ans = reduce(lambda x, y: x + y, map(lambda x: len(x), words))
# print(ans)

#5 Count total words across sentences using map() + reduce()
# Problem: sentences = ['hi there','I love Python'] → 5 words.
# from functools import reduce
# sentences = ['hi there', 'I love Python']
# ans = reduce(lambda x, y: x + y, map(lambda s: len(s.split()), sentences))
# print(ans)

#7 Sum of all odd numbers greater than 10 using filter() + reduce()
# Problem: nums = [5,11,13,20,15] → 11+13+15 = 39
# from functools import reduce
# nums = [5, 11, 13, 20, 15]
# ans = reduce(lambda x, y: x + y, filter(lambda x: x % 2 != 0 and x > 10, nums))
# print(ans)

#8 Product of all even numbers using map() + filter() + reduce()
# Problem: nums = [1,2,3,4] → 2 * 4 = 8
# from functools import reduce
# nums = [1, 2, 3, 4]
# ans = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, nums))
# print(ans)

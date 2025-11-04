#createion of set
# s={10,20,30,40}
# print(s)
# print(type(s))

#
# s=set(range(5))
# print(s)


# while creating empty set we should use set () function as if not complier will treat it as dictionary 

# like this wikl create dict not set
# s={}
# print(s)
# print(type(s))

# this will create set
# s=set()
# print(s)
# print(type(s))

# functions 
# 1. add()
# s={10,20,30,40}
# s.add(40)
# print(s)

# 2. update()
# s={10,20,30,40}
# s.update(50,60,70)
# print(s)

s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)
# 3.copy()
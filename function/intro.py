# 9-10-2025
# functions 
# - resusability of code
# -readability of code 
# syntax---------
# def function_name(parameter):
#     code
# fucntion_name(argument)  
# types of function -
# 1- return type  
    # a- with argument 
    # b- without argument
# 2.non return type
    # a- with argument 
    # b- without argument
# 3.yield (generator)


# ex- make a function that will pritn a message  (this is non return type and without argument )
# def hello():
#     print("hello")
# hello()  


# (this is return type and without argument ) 
# def plusone(num):
#     return num+1
# plusone(2) 

# by print 
# def plusone(num):
#     return num+1
# print(plusone(2))

# def hello():
#     return"hello"
# print(hello())

# (this is return type and with argument ) 
# def addtion(a,b):
#     return a+b
# #addtion(10,20) # ye run toh karegna but show nhi kerenga so to print we have to use
# ans = addtion(10)
# print(ans)
# by input value 
# def addtion (a,b):
#     return a+b
# num1 =int(input("enter number1:"))
# num2 =int(input("enter number2:"))
# ans = addtion(num1,num2)
# print(ans)
# def plusone(num):
#     print (num+1)
# print(plusone(10))

# def plusone(num):
#     print( num+1)
# ans= plusone(10)
# print(ans)

# def plusone(num):
#     return( num+1)
# ans= plusone(10)
# print(ans)

# (this is  non return type and with argument ) 
def plusone(num):
    print(num+1)
plusone(10)    

# (this is  non return type and with argument ) 
def hello():
    print("hello")
hello()    
# when we have to print we use print 
# when we have to make calculation we use return 
# value ke need hoti hai tab return type ke pass jate hai kyuki non return hamesha none return kerta hai 
  
  
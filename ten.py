
# conditional statement
# if 
# syntax of if
# if condition:
#     print()

# if else
# if condition:
#     print()
# else:
#     print()

# if elseif else




# 1.greatest between two without input value
a= int(input("Enter an number1:"))
b= int(input("Enter an number2:"))
if a>b :
    print(a )
else:
    print(b )

# 2.greatest between two

 # 3.smallest between two number
a= int(input("Enter an number1:"))
b= int(input("Enter an number2:"))
if a<b :
    print(a)
else:
    print(b)

#4.check the number is above 50 or not
num=int(input("Enter number: "))
if num<50:
    print("Above")
else:
    print("Not Above")  

# #5. check the password is correct or not password is 1234
password=int(input("Enter Password:"))
if password==1234 :
    print("Correct")
else:
    print("Not correct")


# #6. check the number is even or odd
n=int(input("Enter number: "))
if n%2==0:
    print("Even")
else:
    print("odd")   

# #7. check the number is divisible by 5 or not
num=int(input("Enter number: "))
if num%5==0:
    print("Divisible")
else:
    print("Not divisible")   

# #8. check the person is eligible for vote or note
num=int(input("Enter number: "))
if num>18:
    print("Eligible")
else:
    print("Not Eligiable") 


# #9. check the number is divisible by 7 or not
num=int(input("Enter number: "))
if num%7==0:
    print("Divisible")
else:
    print("Not divisible")   

# #10. check the year is leap year or not
year=int(input("Enter year: "))
if year%4==0:
    print("Leap year")
else:
    print("Not leap year")
   
# #11. check the no is negative or positive
num=int(input("Enter number: "))
if num>0:
    print("Positive")
else:
    print("Negative")   

# #12. check the no. is between 0-50
num=int(input("Enter number: "))
if num>0 and num<50:
    print("Between")
else:
    print("Not between")   

# #13. check the number is multiple of 3 or not
num=int(input("Enter number: "))
if num%3==0:
    print("Multiple")
else:
    print("Not Multiple")   

# #14. check username=user@gmail.com password=1234
username=input("Enter username: ")
password=int(input("Enter Password:"))
if password==1234 and username =="user@gmail.com":
    print("Successfull")
else:
    print("Not successfull")


 #15. check number is divisible by 2 and 4
num=int(input("Enter number: "))
if num%2==0 and num%4==0:
    print("Divisible")
else:
    print("Not divisible")    

#16. check character constant or vowel 
value =input("Enter character: ")
if value=="a"or value=="e"or value=="i"or value=="o"or value=="u" or value=="A" or value=="E"or value=="I"or value=="O"or value=="U":
    print("VOWEL")
else:
    print("Constant")

#28-10-25
# in interview we have to give reallife example with oops related answer 
# oops - object oriented programming - real life entity ko programming me leke ata hai 
# 1- class- collection of data member and member function , all datatype can be said as datatype
#2 - object-  it is a blueprint of the class or we can say key to access member of class , objects can be multiple , all variable can be said as variable
# pillars of oops
# 1- encapsulation- data wrapping in single unit
# 2- inheritance- parent child
# 3- polymorphism- many forms
# 4- abstraction - to show only needed data and hide other or backgroud details



#method -  class ke ander fucntion banene ko method bolte hai
# class student :
#     def show(self,num): #method
#         self.number = num
#         print("hello",self.number)

# obj1= student()        #object
# obj2=student()
# obj1.show()    #.(Dot ) is  a member function 
# obj2.show()   ye galat 


# class student :
#     def show_data(self): #method
#         print(f"the student name is {self.name} and the roll no is {self.roll}")
#     def student_data(self,name,roll):    
#         self.name=name
#         self.roll=roll

# obj1= student()        #object
# obj2=student()
# obj1.student_data("jatin",10)
# obj2.student_data("raj" ,11)
# obj1.show_data()    #.(Dot ) is  a member function 
# obj2.show_data()

#29-10-2025
# class student :
#     def student_data(self,name,roll):    
#         self.name=name
#         self.roll=roll
#     def show_data(self): #method
#         print(f"the student name is {self.name} and the roll no is {self.roll}")
    
# obj1= student()        #object
# obj2=student()
# obj1.student_data("jatin",10)
# obj2.student_data("raj" ,11)
# obj1.show_data()    #.(Dot ) is  a member function 
# obj2.show_data()


#enccapsulation - 
# example - # ek class  ek fucntion ek variable

# constructor- its is a special function as it ia a funtion with no name 
# jese hi ovject create ho vese hi ye phase runn ho hi isliye constructor use kerte hei 
# jese is uska object banata hai vese hi call hojainga 
# constructor over loading nhi hai hota bhhi hai toh default se hota hai 
# constructor is onject depended 
#create using - __init__
# defult constructor
# parametarize constructor 
# instance  Variable -
# constructor with out parameter --------------
# class student :
#     def __init__(self):
#         print("constructor")

# obj = student()           # it is use to call , to call first we create object 


# constructor with  parameter 
# class student :
#     def __init__(self,a,b):
#         print(a+b)

# obj = student(2,3)      


class student :
    def __init__(self,a=0,b=0):
        if a==0 and b==0:            #this will run if obj = student( ) 
            print("value was not given")
        if a!=0 and b==0:             # this will run if obj = student(1 ) 
            print(a)
        if a!=0 and b!=0:                 # this will run if obj = student(1,1 ) 
            print(a+b)    
obj = student(1,1 )   


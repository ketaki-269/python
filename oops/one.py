#28-10-25
# in interview we have to give reallife example with oops related answer 
# oops - object oriented programming - real life entity ko programming me leke ata hai 
# 1- class- collection of data member and member function , all datatype can be said as datatype
#2 - object-  it is a blueprint of the class or we can say key to access member of class , objects can be multiple , all variable can be said as variable
# pillars of oops
# 1- encapsulation- data wrapping
# 2- inheritance- parent child
# 3- polymorphism- many forms
# 4- abstraction - to show only needed data and hide other or backgroud details


# def add (a,b):
#     return a+b
# add(6,8)

#method -  class ke ander fucntion banene ko method bolte hai
# class student :
#     def show(self,num): #method
#         self.number = num
#         print("hello",self.number)

# obj1= student()        #object
# obj2=student()
# obj1.show()    #.(Dot ) is  a member function 
# obj2.show()   ye galat 


class student :
    def show_data(self): #method
        print(f"the student name is {self.name} and the roll no is {self.roll}")
    def student_data(self,name,roll):    
        self.name=name
        self.roll=roll

obj1= student()        #object
obj2=student()
obj1.student_data("jatin",10)
obj2.student_data("raj" ,11)
obj1.show_data()    #.(Dot ) is  a member function 
obj2.show_data()
# 30-10-2025
# inheritance
# types
#1 single inheritance
#2 multiple inheritance
#3 multilevel inheritance
#4 hyrarcical inheritance
#5 hybird inheritance

#single inheritance
class A: #parent class/base class
    pass
class B(A):
    pass #child class / derived class

class A: #parent class/base class
    def show(self):
        print(A)
class B(A): #child class / derived class
    def display(self):
        print("B")
obj =B()
obj.display()
obj.show()


# diamond problem which is known as MRO (method resolution )problem in python 
# MRO problem - like if there is fucntions having same name so it does not decide whom to give priority
#super method 
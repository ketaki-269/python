# 30-10-2025
# inheritance
# types
#1 single inheritance
#2 multiple inheritance
#3 multilevel inheritance
#4 hyrarcical inheritance
#5 hybird inheritance

# #single inheritance
# class A: #parent class/base class
#     pass
# class B(A):
#     pass #child class / derived class

# class A: #parent class/base class
#     def show(self):
#         print(A)
# class B(A): #child class / derived class
#     def display(self):
#         print("B")
# obj =B()
# obj.display()
# obj.show()


# diamond problem which is known as MRO (method resolution )problem in python 
# MRO problem - like if there is fucntions having same name so it does not decide whom to give priority
#super method 
# diamond problem mostly multiple me ati hai but kabhi kabhii hybird me bhi ati hai but ager interview mw pucha toh sirf multiple hi bolnna hai 
#diamond problem(MRO Problem - solution apn iska order decide kerte hai like apn bata te hai ki kis ke badh kya prin tkerna hai  )


#31-10-2025
#multiple  in hertance (ye padha rahe tab me clg ka assignments ker rhi thi)
# mutiple Inheritene ->
# Diamond problem ( MRO (method resolution order) problem )

class A:
  def show(self):
   print("A")
class B(A):
  def show(self):
   super().show()
print("B")
class C(A):
   def show(self):
    super().show()
    print("C")
class D(B,C,A):
   def display(self):
    print("D")
obj = D()
# obj.show()
print(D.mro())


#multilevel inheritance
class A :
    def showA (self):
        print("A")
class B(A) :
     def showB (self):
        print("B")
class C(B):
    def showB (self):
        print("C")
class D(C):
     def showB (self):
        print("D") 

obj  = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()




#hyrarcical inheritance
class A :
     def showA (self):
         print("A")
class B(A) :
      def showB (self):
         print("B")
class C(A):
     def showB (self):
        print("C")
class D(A):
      def showB (self):
         print("D") 
obj1 = D()
obj2 = C()
obj3 =B()
obj.show

#hybird inheritance- two or more than 2 inheritance are use the it is hybird 
class A :
     def showA (self):
         print("A")
class B(A) :
      def showB (self):
         print("B")
class C(B):
     def showB (self):
        print("C")
class D(A,B,C):
      def showB (self):
         print("D") 
obj1 = D()
obj2 = C()
obj3 =B()
obj.show
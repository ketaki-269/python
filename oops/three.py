#polymorphism 
# c++ me alag hota hai pyhton me alg hota hai as python me pointer nhi hota 
# print(len("jatin"))
# print(len([1,2,3,4]))
# print(len((1,3,4,5,)))


# print(10+20)
# print("jatin" + "singh")

# with opps
# polymorphism  - one fucntion can use to display multiple things
# like show function is use to display diffrent things
# jiske hisab se call horha hai uske hisab se output derha hai
# with loop 
# class A :
#     def show(self):
#         print("class A")
# class B:
#     def show(self):
#         print("class B")        
# class C:
#     def show(self):
#         print("class C")          
# obj= [A(),B(),C()]
# for i in obj:
#     i.show()        


#with fucntion
# class A :
#     def show(self):
#         print("class A")
# class B:
#     def show(self):
#         print("class B")        
# class C:
#     def show(self):
#         print("class C")    
# def  show_data(data):
#     data.show()            
# obj= [A(),B(),C()]
# for i in obj:
#     i.show()            

#  calculation addtion polymorphism example
# def addition (a=0 , b=0 ,c=0):
#     return a+b+c
# ans = addition (1,3,5)
# print(ans)
# ans = addition(1,3)
# print(ans)
# ans = addition(1)
# print(ans)
# ans = addition()
# print(ans)

# addtion polymorphism  with class example 
class calculation:
   def addition (self,a=0 , b=0 ,c=0):
    return a+b+c
obj=calculation()
ans = obj.addition (1,3,5)
print(ans)
ans = obj.addition(1,3)
print(ans)
ans = obj.addition(1)
print(ans)
ans = obj.addition()
print(ans)


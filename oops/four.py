#Abstraction - to show meaning data and hides backgroud data
# abstract class 
# abstract method
# parent class ko hi abstract class banate hai or use pass dete hai meaning nhi dte kyuki vo 
# to use abstract class we need to import abstractmethod
# abstract class - jo ek bhi abstract method contain kerta hai 
# abstrct class ka normal object nhi banata 

from abc import ABC,abstractmethod

class RBI(ABC):                    # abstract class 
    @abstractmethod
    def fd(self):
        pass
    def bank(self):
        print("hello thi sis RBI")
class SBI(RBI):
    def fd(self):
        print("7% interst")
       
    def bank(self):
        print("Hello this is os SBI ")
        super().bank()                         # 
class Kotak(RBI):
    def fd(self):
        print("6% interst") 
    def bank(self):
        print("Hello this is os Kotak ")       
obj =SBI()
obj1= Kotak()
obj1.bank()
obj.bank()        
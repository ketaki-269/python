# core- logical ability
#advance()-  numpy
#1 numpy - numerical python ,in this we work on array, high mathematical imputation per from ker rah hai 
#2panda- TO MANIPULATE DATA by need and show result on bases of manipulation 
#3 matppotlib -
#4 seaborn- 

# a=[1,2,[4,5,[7,8,9]]]
# print(a)
# print(a[2])
# print(a[2][2])
# print(a[2][2][2])

#05-11-2025
#array
#array()  this function is use to create array
import numpy as np
a=[1,23,3,4]
print(type(a))

arr1 = np.array([1,2,3,4])
print(type(arr1))

#
import time
size=10000000
list1=range(size)
list2=range(size)
start = time.time()  # program ke run hon evale time ko store kerlenga 
result = [x+y for x,y in zip(list1,list2) ]
end=time.time()        # program ke end hone ka time 
print("the time of list program :", end - start)

array1 = np.arange(size)
array2 = np.arange(size)
start= time.time()
result = array1+array2
end= time.time()
print("the time of array program :", end - start)

# library-->package -->module 
# module is like single page  
# package - it is like book collection of multiple module is package 
# collection of multiple __package__ is library 

# np.random.randint 
# np - library 
# random- package 
# randint - modulw 



#pandas
# .read_csv()- it is a pandas function , () iske unther file/ or data ka path or path ke is \ symbol ko / convert kerna hai
# file ka name or fir csv extention

import pandas as pd 
pd.read_csv("C:/Users/DELL/Desktop/powerbi/gym.csv")

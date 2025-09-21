# tuple
# li=[1,2,5,2,34,12,3]
# li[0]=100
# print(li)

# li=(1,2,4,2,4,5,6,8,667,34)
# print(li.index(1))
# print(li.count(2))
# print(min(li))
# print(max(li))
# print(len(li))
# print(li)


# que- list inside tuple 

# student_data= [("Amit",79), ("raj",80)]
# print(student_data)
student_data= [("Amit",79), ("raj",80)]
# add student 
number_of_studets= int(input("Enter number od students data you want to enter"))
for i in range (number_of_studets):
     name=input("enter student name: ")
     marks=int(input("enter marks: "))
     student_data.append((name,marks))
# display all student data

for i in range(len(student_data)):
     print(f"  {i+1} student name is {student_data[i][0]} and the student marks is {student_data[i][1]}")

# for i in range(len(student_data)):
#      print(i,end=" ")
# for i in student_data:
#      print(i,end=" ")     
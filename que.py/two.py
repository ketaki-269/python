# reverse a list without using reverse fumction 

# li = [1,6,3,32,8,4]
# i= 0
# j=len(li)-1
# temp= li[i]
# li[i]=li[j]
# li[j]=temp
# print (li)

li = [1,6,3,32,8,4]
i= 0
j=len(li)-1
while i<j:
 temp= li[i]
 li[i]=li[j]
 li[j]=temp
 i+=1
 j-=1

print (li)

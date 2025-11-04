# representation- 
# t=10,20,30,40
# print(t)
# print(type(t))

# t=(10,)
# print(type(t))

# t=10,20,30,40
# print(type(t))

# t=10
# print(type(t))


# list=[10,20,30]
# t=tuple(list)
# print(t)

#accessing elements - 
# t=(10,20,30,40,50,60)
# print(t[0]) #10
# print(t[-1]) #60



# # t=(10,20,30,40,50,60)
# # print(t[2:5:1])



# # mathematical operator 
# # * and + for tuple 
# # t1=(10,20,30)
# # t2=(40,50,60)
# # t3=t1+t2
# # print(t3)

# # fucntions

# # 1.len 
# t=(10,20,30,40,50,60)
# print(len(t))
# # 2.count
# t=(10,20,30,10,50,60)
# print(t.count(10))
# # 3.index 
# t=(10,20,30,10,50,60)
# print(t.index(10))
# 4. sorted  
# t=(80,30,40,10,20,10)
# print(sorted(t))
# t=sorted(t,reverse=True)
# print(t) 

# # 5. min()
# t=(80,30,40,10,20,10)
# print(min(t))\

# 5. max()
# t=(80,30,40,10,20,10)
# print(max(t))


# tuple packing 
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)

#unpacking 
t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)
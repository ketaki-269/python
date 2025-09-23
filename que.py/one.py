# to reverse no. 
# num=int (input("Enter number: "));
# rev=0; 
# while (num>0):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)    


num=int (input("Enter number: "))
rev=0; 
ans=1
while (num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
    if (ans==rev):
        print("Palindrom")
    else:
        print("NOT")



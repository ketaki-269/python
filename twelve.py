
# create ATM program?
# Available_balance=5000
# select=input("Select operation")
# select= "withdrawl" or "deposit" or "Balance check"
# if select== "withdrawl":
#     print(withdrawl=int(input("Enter withdrawl amount: ")))
# elif select== "deposit":
#     print(deposit=int(input("Enter withdrawl amount: ")))

# elif  withdrawl<Available_balance:
#     print(Available_balance-withdrawl)
# elif withdrawl>Available_balance:
#     print("Not sufficient Balance")  
# elif     




# Available_balance=5000
# selectoption=(input("Enter select option : "))
# selectoption= "withdrawl" or "deposit" or "Balance check"

# if selectoption=="withdrawl" :
#     withdrawlamount = int(input("Enter withdrwal amount: "))
#     Available_balance-=withdrawlamount
#     print(Available_balance)

# elif selectoption=="deposit":
#     depositamount = int(input("Enter deposit amount: "))
#     Available_balance+=depositamount
#     print(Available_balance)

# elif selectoption=="Balance check":
#     print("currect balance is =",Available_balance)



balance = 6000 
password = int(input("Enter Password: "))

if password == 1234:
    print("Correct\n")

print("ATM MENU ")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful. New Balance:", balance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. Remaining Balance:", balance)
    else:
        print("Insufficient balance!")

else:
    print("Invalid choice!")

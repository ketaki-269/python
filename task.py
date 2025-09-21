# Task 1:
# Ask the user of their age and if it is greater than or equals to 18 with Ternary operator and display the result in alert.
# age = int(input("Enter your age: "))
# print("You are adult" if age >= 18 else "You are not adult")

# Task 2:
# Ask the user if they have completed a course and have a certificate by (Confirm)
# if both Ok then give a "Completed" message by Alert otherwise "Not completed".
# course = input("Have you completed a course? (yes/no): ").lower()
# certificate = input("Do you have a certificate? (yes/no): ").lower()
# if course == "yes" and certificate == "yes":
#     print("Completed")
# else:
#     print("Not completed")

# Task 3:
# Ask the user for the price of an item and (Confirm) whether they have a discount coupon.
# Apply a 10% discount if they confirm.
# price = int(input("Enter the price of the item: "))
# coupon = input("Do you have a discount coupon? (yes/no): ").lower()
# if coupon == "yes":
#     price = price * 0.9   # 10% discount
# print("Final Price:", price)

# Task 4:
# Ask the user for their exam score and determine if they passed or failed. (Above 33 Pass)
# score = int(input("Enter exam score: "))
# if score > 33:
#     print("Pass")
# else:
#     print("Fail")

# Task 5:
# Check Entered number is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Task 6:
# Ask for conformation "Are you sure to delete" if Ok give message "Item Deleted" otherwise "Cancelled".
# confirm = input("Are you sure to delete? (yes/no): ").lower()
# if confirm == "yes":
#     print("Item Deleted")
# else:
#     print("Cancelled")

# Task 7:
# Check Entered number is Positive or Negative.
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Task 8:
# Print 1-10 number in console by while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Task 9:
# Keep asking the user to input a number until they enter a number greater than 10. by Do while loop.
while True:
    n = int(input("Enter a number greater than 10: "))
    if n > 10:
        break
print("You entered:", n)

# Task 10:
# Ask the user to enter a day of the week (1 for Monday, 2 for Tuesday, etc.) and display the name of the day. by Switch Case.

# number=int(input("Enter week number "))
# if number==1:
#     print("Monday")
# elif number ==2:
#     print("Tuesday")
# elif number==3: 
#     print("Wednesday")
# elif number ==4:
#     print("Thursday")
# elif number==5: 
#     print("Friday") 
# elif number==6:
#     print("Saturday")
# elif number==7:
#     print("Sunday")   
# else:
#     print("Invalid")            

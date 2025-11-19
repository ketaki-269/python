# website= input("Enter website name:  ").lower
# if website =="amazon":
#     website =  input("Enter shoes or clothes: ").lower
#     if website =="shoes":
#        pass
# elif website =="clothes":
#      pass
#      else:
#      print("Invalid")
# else:
#     print("Invalid")
#        pass

# que  1- 
website = input("Enter a website name: ").lower()

if website =="amazon":
    website = input("Enter product or service: ").lower()
    if website =="product":
        website=input("Enter shoes or clothes: ").lower()

        if website =="shoes":
            print("1000")
        elif website =="clothes":
            print("2000")
        else:
            print("Invalid")
    elif website =="service":
        print("Not Available")
    else:
        print("Invalid")  
else:
    print("Invalid")



#que- 2

# cardamount = int(input("Enter amount :" ))
# if cardamount>5000:
#     cardamount=input("Enter Membership: ").lower
#     if cardamount=="Gold"
#     cardamount = input("Enter  paymentmode: ").lower()
#       if cardamount =="Card":
#         cardamount=input("Enter UPI or CARD: ").lower()
#         if cardamount =="UPI":
#             print(cardamount-(cardamount*15/100))
#         elif cardamount=="CARD":
#             print(cardamount-(cardamount*20/100))
#         else:
#             ("Invalid")
#     else:
#         ("Invalid")
cart = int(input("Enter Cart Amount: "))
membership = input("Enter Membership Type (Gold/Silver): ").lower()
payment = input("Enter Payment Mode (Card/UPI/Cash): ").lower()

if cart >= 5000:
    if membership == "gold":
        if payment == "card":
            print("20% Discount")
        elif payment == "upi":
            print("15% Discount")
        else:
            print("No Discount")
    elif membership == "silver":
        if payment == "card":
            print("10% Discount")
        elif payment == "cash":
            print("5% Discount")
        else:
            print("No Discount")
    else:
        print("No Discount")
else:
    if membership == "gold":
        print("5% Discount")
    else:
        print("No Discount")



que -3
stream = input("Enter Stream (Science/Commerce/Arts): ").lower()
marks = int(input("Enter Marks: "))
entrance = int(input("Enter Entrance Exam Score: "))

if stream == "science":
    if marks >= 70:
        if entrance >= 60:
            print("Eligible for B.Sc")
        else:
            print("Eligible for Diploma")
    else:
        print("Not Eligible for Science")

elif stream == "commerce":
    if marks >= 65:
        if entrance >= 55:
            print("Eligible for B.Com")
        else:
            print("Eligible for Diploma in Accounts")
    else:
        print("Not Eligible for Commerce")

elif stream == "arts":
    if marks >= 60:
        if entrance >= 50:
            print("Eligible for B.A")
        else:
            print("Shortlisted for Interview")
    else:
        print("Not Eligible for Arts")

else:
    print("Invalid Stream")

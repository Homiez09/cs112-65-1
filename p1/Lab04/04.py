jk = input("Enter your buffet choice: ")

if jk == "Japanese":
    wedCheck = input("Is today Wednesday (yes/no)? ")
    if wedCheck == "yes":
        print(f"Your payment is 850.00 Baht.")
    else:
        print("Your payment is 1000.00 Baht.")
elif jk == "Korean":
    wedCheck = input("Is today Wednesday (yes/no)? ")
    if wedCheck == "yes":
        print(f"Your payment is 1275.00 Baht.")
    else:
        print("Your payment is 1500.00 Baht.")
else:
    print(f"Sorry, there is no {jk} buffet.")
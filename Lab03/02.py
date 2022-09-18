amount = float(input("Enter buying amount: "))
result = amount 
if amount >= 3000:
    print(f"Amount due after discount is {result * 0.85:.2f} baht.")
elif amount >= 1000:
    print(f"Amount due after discount is {result * 0.9:.2f} baht.")
else:
    print(f"Amount due after discount is {result:.2f} baht.")
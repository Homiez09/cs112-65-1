w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w/(h**2)
print(f"BMI is {bmi:.1f}")
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")
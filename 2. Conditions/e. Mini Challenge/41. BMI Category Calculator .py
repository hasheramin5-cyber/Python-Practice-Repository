weight = float(input("\nEnter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
    

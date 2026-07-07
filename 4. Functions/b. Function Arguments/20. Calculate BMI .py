# A Program to calculate Body Mass Index (BMI) using a function.

# Definition:
# Body Mass Index (BMI) is a value used to estimate whether a person's weight is appropriate for their height. It is calculated using the formula: BMI = Weight (kg) ÷ Height² (m²).

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("BMI =", round(bmi, 2))

calculate_bmi(70, 1.75)

# Explanation:
# The program defines a function that calculates the Body Mass Index (BMI). It accepts a person's weight in kilograms and height in meters as parameters. Using the BMI formula, the function calculates the result and displays it rounded to two decimal places. BMI is commonly used as a general indicator to assess whether a person's weight is appropriate for their height.
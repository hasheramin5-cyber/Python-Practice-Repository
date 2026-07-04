# Temperature Converter in Python.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")  # here .nf is used to round the value to n decimal places.

# Explaination:
# In this code snippet, we take the temperature in Celsius as input from the user and convert it to Fahrenheit using the formula (Celsius * 9/5) + 32. We then print the result in a formatted string, showing the Celsius temperature and its equivalent in Fahrenheit rounded to two decimal places.
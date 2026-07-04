# # Using Type Casting to convert a float to an integer in Python.

number = 99.99

converted_number = int(number)

print(converted_number)
print(type(converted_number))

# Explaination:
# In this code snippet, we have a variable 'number' that holds a float value 99.99. We then use the int() function to convert this float into an integer and store it in the variable 'converted_number'. Finally, we print the converted number and its type to confirm that the conversion was successful. The output will show that 'converted_number' is now of type <class 'int'>. Note that when converting a float to an integer, the decimal part is truncated, and only the whole number part is retained.
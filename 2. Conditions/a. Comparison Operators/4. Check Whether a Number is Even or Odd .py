# Check Whether a Number is Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even Number.")
else:
    print(number, "is Odd Number.,")

# Explanation:
# In this code snippet, we take a number as input from the user and convert it to an integer. We then check if the number is even or odd using the modulus operator (%). If the remainder when the number is divided by 2 is 0, we print "Even Number". Otherwise, we print "Odd Number". This code helps in determining whether the entered number is even or odd.
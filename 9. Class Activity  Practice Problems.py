'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.



Write a program to check if a number is positive, negative, or zero.
'''

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


Create a program to determine whether a given year is a leap year.


# Check if the year is a leap year
if (year % 400 == 0):
    print(f"{year} is a leap year.")
elif (year % 100 == 0):
    print(f"{year} is NOT a leap year.")
elif (year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")



Build a simple calculator that asks for two numbers and an operator (+, -, *, /) and prints the result.


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        result = None
else:
    print("Invalid operator.")
    result = None




Write a Python program that accepts a student's marks and prints the appropriate grade based on the following criteria:
A: 85 and above
B: 70 to 84
C: 50 to 69
F: Below 50

# Determine grade based on marks
if marks >= 85:
    grade = 'A'
elif 70 <= marks < 85:
    grade = 'B'
elif 50 <= marks < 70:
    grade = 'C'
else:
    grade = 'F'
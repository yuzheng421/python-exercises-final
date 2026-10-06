"""Exercise 3.0 — Computing with what the user typed"""

# 1. In: The user enters two numbers.
# 2. Process: Calculate addition, subtraction, multiplication, and division.
# 3. Out: Display the results of the four operations.
# 4. If the second number is zero, display a message instead of dividing by zero,
#    because division by zero is not allowed.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number == 0:
    print("Division: Cannot divide by zero.")
else:
    print("Division:", first_number / second_number)

# Test with 7 and 2:
# The division result is 3.5 because / performs normal division in Python.
"""Exercise 3.1 — Odd or even (homework)"""

# 1. In: The user enters a positive whole number N.
# 2. Process: Check every number from 1 to N to see whether it is odd or even.
# 3. Out: Display each number followed by "odd" or "even".
# 4. Special cases:
#    - If N is 0, display a message because there are no numbers from 1 to 0.
#    - If N is negative, display a message asking for a positive number.
#    - If N is greater than 100, do not print all the numbers because the output
#      would be too long.

number = int(input("Enter a positive whole number: "))

if number == 0:
    print("There are no numbers from 1 to 0.")
elif number < 0:
    print("Please enter a positive number.")
elif number > 100:
    print("The number is too large. Please enter a number from 1 to 100.")
else:
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(i, "even")
        else:
            print(i, "odd")
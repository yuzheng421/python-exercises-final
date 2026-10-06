"""Exercise 5.0 — Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A customer satisfaction score from 0 to 100.
# 2. Process: Compare the score with four defined ranges.
# 3. Out: A message describing the customer's satisfaction level.
# 4. My ranges, my boundaries, my messages:
# 0-49: Low satisfaction
# 50-69: Moderate satisfaction
# 70-84: Good satisfaction
# 85-100: Excellent satisfaction
# These boundaries separate dissatisfied, average, satisfied, and highly satisfied customers.


# Your code below

score = int(input("Enter customer satisfaction score (0-100): "))

if score < 0 or score > 100:
    print("Please enter a score from 0 to 100.")
elif score <= 49:
    print("Low satisfaction")
elif score <= 69:
    print("Moderate satisfaction")
elif score <= 84:
    print("Good satisfaction")
else:
    print("Excellent satisfaction")
    
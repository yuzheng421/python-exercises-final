"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The same list of eight marketing channels from exercise 4.0.
# 2. Process: Display the list in four different orders without changing the original.
# 3. Out: Four reordered versions and the original list at the end.
# 4. My four orders, and which ones modify the original:
# I chose original order, alphabetical order, reverse alphabetical order,
# and reversed original order.
# sorted() and reversed() return new results, so the original list is not modified.


# Your code below

marketing_channels = [
    "Instagram",
    "TikTok",
    "YouTube",
    "Google Ads",
    "Email",
    "Facebook",
    "LinkedIn",
    "Influencer Marketing"
]

print("1. Original order:", marketing_channels)
print("2. Alphabetical order:", sorted(marketing_channels))
print("3. Reverse alphabetical order:", sorted(marketing_channels, reverse=True))
print("4. Reversed original order:", list(reversed(marketing_channels)))

print("Original list at the end:", marketing_channels)

"""Exercise 2.1 — Transforming text (homework)"""

# 1. In: The user enters a sentence.
# 2. Process: Apply four different string transformations to the sentence.
# 3. Out: Display the four transformed versions of the sentence.
# 4. My four transformations, and when each is useful:
#    1. strip() removes spaces at the beginning and end, useful for cleaning user input.
#    2. upper() makes all letters uppercase, useful for headings.
#    3. lower() makes all letters lowercase, useful for standardizing text.
#    4. title() capitalizes each word, useful for titles or names.
#
# Test result:
# With spaces at both ends and a capital in the middle,
# all four transformations produced the results I expected.

sentence = input("Enter a sentence: ")

print("Stripped:", sentence.strip())
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
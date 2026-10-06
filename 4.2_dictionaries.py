"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a marketing campaign.
# 2. Process: Store the information in a dictionary, read a field, change a field,
#    remove a field, and display the remaining fields.
# 3. Out: The campaign information after the changes.
# 4. My object, my five fields, and why those:
# I chose a marketing campaign with name, platform, budget, target audience, and status.
# These fields are useful for identifying, planning, targeting, and tracking a campaign.
# When I asked for a field that did not exist, direct access would cause a KeyError.
# I used get() so the program survives and displays a message instead.


# Your code below

campaign = {
    "name": "Fall Fashion Campaign",
    "platform": "Instagram",
    "budget": 5000,
    "target_audience": "Young adults",
    "status": "Planned"
}

print("Campaign name:", campaign["name"])

campaign["status"] = "Active"

del campaign["budget"]

print("Missing field:", campaign.get("end_date", "Field not found"))

print("Campaign information:")
for field, value in campaign.items():
    print(field, ":", value)
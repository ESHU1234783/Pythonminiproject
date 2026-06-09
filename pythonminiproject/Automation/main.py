import re

# Read data from input file
with open("input.txt", "r") as file:
    text = file.read()

# Find all email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails to a new file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print(" Email addresses extracted successfully!")
print(f"Total emails found: {len(emails)}")
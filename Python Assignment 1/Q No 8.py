# Create a program that checks if a given string is a palindrome.


text = input("Enter a string: ")

# Normalize the string by converting it to lowercase and removing spaces
normalized_text = text.replace(" ", "").lower()

# Check if the string is the same forwards and backwards
if normalized_text == normalized_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Explanation:
# Input: The program asks the user to enter a string and stores it in text.

# Normalization:

# text.replace(" ", "") removes spaces from the string.
# .lower() converts the string to lowercase, making the check case-insensitive.

# Palindrome Check:

# normalized_text[::-1] reverses the string.
# The program then compares the original normalized_text with its reverse. If they are the same, it’s a palindrome; otherwise, it’s not.
# Example:
# Input: "Madam"

# Output: "The string is a palindrome."

# Input: "Hello"

# Output: "The string is not a palindrome."
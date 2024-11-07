# Create a program to calculate the sum of the digits of an inputted integer.

# Get an integer from the user
number = input("Enter an integer: ")

# Initialize sum variable
digit_sum = 0

# Loop through each character in the string representation of the number
for digit in number:
    # Check if the character is a digit
    if digit.isdigit():
        digit_sum += int(digit)  # Convert to integer and add to sum

# Print the result
print("The sum of the digits is:", digit_sum)

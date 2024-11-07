# Use a loop to count the number of digits in an integer.

# Input: integer from the user
number = int(input("Enter an integer: "))
count = 0

# Handle negative numbers by taking the absolute value
number = abs(number)

# Loop to count the digits
while number > 0:
    number //= 10  # Remove the last digit
    count += 1    # Increment the digit count

# If the input was zero, we need to handle that case
if count == 0:
    count = 1  # Zero has one digit

print("The number of digits is:", count)

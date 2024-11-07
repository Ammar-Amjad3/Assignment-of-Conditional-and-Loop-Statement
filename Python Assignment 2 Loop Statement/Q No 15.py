# Print the sum of even and odd numbers separately up to a given number.

# Get a number from the user
upper_limit = int(input("Enter a number: "))

# Initialize sums for even and odd numbers
even_sum = 0
odd_sum = 0

# Loop through each number from 1 to the given number
for num in range(1, upper_limit + 1):
    if num % 2 == 0:  # Check if the number is even
        even_sum += num  # Add it to even_sum
    else:  # The number is odd
        odd_sum += num  # Add it to odd_sum

# Print the results
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

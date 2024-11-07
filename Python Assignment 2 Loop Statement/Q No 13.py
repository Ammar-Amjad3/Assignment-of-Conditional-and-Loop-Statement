# Use nested loops to print a pyramid pattern of *.

# Number of rows in the pyramid
rows = 5

# Outer loop for each row
for i in range(rows):
    # Print spaces to center the pyramid
    for j in range(rows - i - 1):
        print(" ", end="")
    
    # Print asterisks for the pyramid
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line after each row
    print()

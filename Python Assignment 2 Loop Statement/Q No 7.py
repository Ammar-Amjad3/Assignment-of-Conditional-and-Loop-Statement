# Find the factorial of a number using a while loop.

number = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= number:
    factorial *= i  # Multiply current value of factorial by i
    i += 1  # Move to the next integer

print("The factorial of", number, "is:", factorial)

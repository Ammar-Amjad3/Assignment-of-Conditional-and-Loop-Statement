# Write a program that breaks the loop when a certain condition is met.

while True:  # Start an infinite loop
    number = int(input("Enter a number (0 to exit): "))  # Prompt the user for input
    
    if number == 0:  # Check if the input number is 0
        print("Exiting the loop.")
        break  # Exit the loop if the condition is met
    
    print(f"You entered: {number}")  # Print the entered number

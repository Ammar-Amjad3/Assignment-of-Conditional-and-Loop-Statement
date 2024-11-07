# Create a program that simulates a countdown timer starting from a given number down to zero.


import time

# Get the starting number for the countdown

start = int(input("Enter the starting number for the countdown: "))

# Countdown loop

for number in range(start, -1, -1):
    print(number)
    time.sleep(1)  # Pause for 1 second

print("Countdown complete!")

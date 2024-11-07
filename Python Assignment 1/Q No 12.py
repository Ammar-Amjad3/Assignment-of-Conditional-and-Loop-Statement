# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temperature = float(input("Enter the temperature in Celsius: "))

if temperature <= 0:
    print("It's freezing.")
elif 0 < temperature <= 25:
    print("The temperature is moderate.")
else:
    print("It's hot.")

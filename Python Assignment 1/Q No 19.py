#  Check if a string input is uppercase, lowercase, or a mix.

user_input = input("Enter a string: ")

if user_input.isupper():
    print("The string is all uppercase.")
elif user_input.islower():
    print("The string is all lowercase.")
elif user_input.isalpha() and not user_input.isalnum():
    print("The string contains letters but is a mix of upper and lower case.")
else:
    print("The string is a mix of uppercase and lowercase letters.")

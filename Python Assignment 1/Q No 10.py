# Write a program to determine if a given character is a vowel or consonant

char = input("Enter a character: ")
char = char.lower()
if char in 'aeiou':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")

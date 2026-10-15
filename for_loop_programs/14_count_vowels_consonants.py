text = input("Enter a string: ")
vowels = 0
consonants = 0

for character in text:
    if character.lower() in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)

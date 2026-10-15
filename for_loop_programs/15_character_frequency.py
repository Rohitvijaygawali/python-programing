text = input("Enter a string: ")
counted_characters = []

for character in text:
    if character not in counted_characters:
        counted_characters.append(character)
        count = 0
        for candidate in text:
            if candidate == character:
                count += 1
        label = repr(character) if character.isspace() else character
        print(f"{label} = {count}")

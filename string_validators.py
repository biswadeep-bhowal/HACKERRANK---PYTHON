string = input()

print(any(character for character in string if character.isalnum()))

print(any(character for character in string if character.isalpha()))

print(any(character for character in string if character.isdigit()))

print(any(character for character in string if character.islower()))

print(any(character for character in string if character.isupper()))
"""EX01 - Chardle: A cute step toward Wordle."""

__author__ = "730673957"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    exit(print("Error: Word must contain 5 characters"))

single_character: str = input("Enter a single character: ")
    
if len(single_character) != 1: 
    exit(print("Error: Character must be a single character."))

print("Searching for " + single_character + " in " + five_character_word)

if str(five_character_word[0]) == single_character:
    print(single_character + " found at index 0")
if str(five_character_word[1]) == single_character:
    print(single_character + " found at index 1")
if str(five_character_word[2]) == single_character:
    print(single_character + " found at index 2")
if str(five_character_word[3]) == single_character:
    print(single_character + " found at index 3")
if str(five_character_word[4]) == single_character:
    print(single_character + " found at index 4")

instances_of_single_character: int = 0

if str(five_character_word[0]) == single_character:
    instances_of_single_character += 1
if str(five_character_word[1]) == single_character:
    instances_of_single_character += 1
if str(five_character_word[2]) == single_character:
    instances_of_single_character += 1
if str(five_character_word[3]) == single_character:
    instances_of_single_character += 1
if str(five_character_word[4]) == single_character:
    instances_of_single_character += 1

if int(instances_of_single_character) == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
if int(instances_of_single_character) == 1: 
    print("1 instance of " + single_character + " found in " + five_character_word)
if int(instances_of_single_character) >= 2:
    print(str(instances_of_single_character) + " instances of " + single_character + " found in " + five_character_word)
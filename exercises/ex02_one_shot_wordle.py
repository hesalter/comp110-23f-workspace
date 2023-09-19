"""EX02 - One Shot Wordle."""

__author__: str = "730673957"

secret_word: str = "python"
len_of_word: int = len(secret_word)

wordle: str = input(f"What is your {len_of_word}-letter guess? ")
len_of_guess: int = len(wordle)
idx_of_guess: int = 0
emoji_string: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len_of_guess != len_of_word:
    if len_of_word != len_of_guess:
        wordle: str = input(f"That was not {len_of_word} letters! Try again: ")
        len_of_guess: int = len(wordle)

alt_indices: int = 0
guessed_character: bool = False

while (idx_of_guess < len_of_word) and guessed_character == False:
    if str(wordle[idx_of_guess]) == str(secret_word[idx_of_guess]): 
        emoji_string = emoji_string + GREEN_BOX
    else:
        if str(secret_word[alt_indices]) == str(wordle[idx_of_guess]):
            guessed_character == True
            emoji_string = emoji_string + WHITE_BOX
        else:
            alt_indices += 1
            emoji_string = emoji_string + YELLOW_BOX
    idx_of_guess += 1

while len_of_guess == len_of_word: 
    if wordle == secret_word:
        print(emoji_string)
        exit(print("Woo! You got it!"))
    print(emoji_string)
    exit(print("Not quite. Play again soon!"))

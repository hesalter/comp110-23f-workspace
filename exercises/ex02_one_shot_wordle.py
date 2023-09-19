"""EX02 - One Shot Wordle."""

__author__: "730673957"

secret_word: str = "python"
len_of_word: int = len(secret_word)

wordle: str = input(f"What is your {len_of_word}-letter guess? ")
len_of_guess: int = len(wordle)

while len_of_guess != len_of_word:
    if len_of_word != len_of_guess:
        wordle: str = input(f"That was not {len_of_word} letters! Try again: ")
        len_of_guess: int = len(wordle)
while len_of_guess == len_of_word: 
    if wordle == secret_word:
        exit(print("Woo! You got it!"))
    exit(print("Not quite. Play again soon!"))
    
words = [
    {
        "name": "banana",
        "hint": [
            "Yellow fruit",
            "Often found in bunches",
            "Peel before eating",
            "Rich in potassium",
            "Can be used in smoothies and desserts",
            "Has a curved shape",
            "Typically has black spots when ripe",
            "Source of natural sugar",
        ],
    },
    {
        "name": "elephant",
        "hint": [
            "Large mammal",
            "Has a trunk",
            "Big ears",
            "Has tusks (typically males)",
            "Gray or brown skin",
            "Lives in herds",
            "Known for its memory",
            "Symbol of strength and wisdom",
        ],
    },
    {
        "name": "computer",
        "hint": [
            "Electronic device",
            "Used for processing data",
            "Has a keyboard and screen",
            "Can be a desktop, laptop, or tablet",
            "Connects to the internet",
            "Stores and retrieves information",
            "Used for communication, entertainment, and work",
            "Runs on software programs",
        ],
    },
]

# Sets the initial number of lives for the game.
remaining_lives = 5


# Defines a function to handle the guessing of words.
def guess_the_word(round_number):
    # Allows access to the global variable 'remaining_lives' within the function.
    global remaining_lives
    # Retrieves the current word to guess based on the round number.
    current_word = words[round_number]
    # The solution is the actual word that needs to be guessed.
    solution = current_word["name"]
    print("Unscramble this word:")
    # Creates a string of underscores representing the unguessed letters of the solution.
    blank_word = f'{"_" * len(solution)}'
    print(blank_word)
    # Prints the first clue for the word.
    print("Clue:\n" + current_word["hint"].pop(0))
    # Initializes the count of guesses made.
    guesses_made = 0
    # Creates a list of guessed letters, initially filled with underscores.
    guessed_letters = list(blank_word)

    # Starts an infinite loop for the guessing process.
    while True:
        # Prompts the user to enter a letter.
        guess = input("Enter a letter ->")
        # Checks if the user wants to exit the game.
        if guess != "exit":
            # Checks if the guessed letter is incorrect.
            if guess != solution[guesses_made]:
                print("Incorrect guess")
                # Provides the next clue.
                print("Clue:\n" + current_word["hint"].pop(0))
                # Decreases the number of remaining lives.
                remaining_lives -= 1
                print(f"Remaining lives: {remaining_lives}")
                # If only one life remains, provides two additional clues.
                if remaining_lives == 1:
                    print("Clue:\n" + current_word["hint"].pop(0))
                    print("Clue:\n" + current_word["hint"].pop(0))
            else:
                # If the guessed letter is correct, updates the guessed letters list.
                print("Correct letter!")
                guessed_letters[guesses_made] = guess
                # Increments the count of guesses made.
                guesses_made += 1
                # Prints the current state of the guessed word.
                print("".join(guessed_letters))
            # Checks if the entire word has been guessed correctly.
            if "".join(guessed_letters) == solution:
                break
        else:
            # If the user enters 'exit', ends the game.
            return 0
        # If all lives are lost, ends the game.
        if remaining_lives == 0:
            return 0


# Checks if the script is being run directly (not imported).
if __name__ == "__main__":
    # Initializes the round number.
    round_number = 0
    # Prompts the user to start the game.
    start_game = input(
        """welcome to save your boat game :D
Description :
1) you have a boat that have 5 lives when boat lives end it will drown
2) you should guess the word by choosing a letter from the English alphabet
3) if you got a letter wrong you will lose a live
4) when you guess the letter right you will be provided with the updated word
5) if you guess everything right you will win
6) if you finish your lives and did not guess the word you will lose
7) to quit you can write exit
wanna play ? (y,n)"""
    )

    # Continues to prompt for rounds until the user exits or says 'no'.
    while start_game.lower() != "n" and start_game.lower() != "exit":
        # Calls the function to start a round of guessing.
        result = guess_the_word(round_number)
        # Increments the round number for the next word.
        round_number += 1
        # Checks if the game is over due to running out of lives or the user exiting.
        if remaining_lives == 0 or result == 0:
            print("Game Over")
            break
        # Checks if all words have been used.
        if round_number > len(words) - 1:
            print("Game Over")
            break

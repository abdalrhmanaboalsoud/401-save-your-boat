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

remaining_lives = 5 
def guess_the_word(round_number):
    global remaining_lives
    current_word = words[round_number]
    solution = current_word["name"]
    print("Unscramble this word:")
    blank_word = f'{"_" * len(solution)}'
    print(blank_word)
    print("Clue:\n" + current_word["hint"].pop(0))
    guesses_made = 0
    guessed_letters = list(blank_word)

    while True:
        guess = input("Enter a letter ->")
        if guess != "exit":
            if guess != solution[guesses_made]:
                print("Incorrect guess")
                print("Clue:\n" + current_word["hint"].pop(0))
                remaining_lives -= 1
                print(f"Remaining lives: {remaining_lives}")
                if remaining_lives == 1:
                    print("Clue:\n" + current_word["hint"].pop(0))
                    print("Clue:\n" + current_word["hint"].pop(0))
            else:
                print("Correct letter!")
                guessed_letters[guesses_made] = guess
                guesses_made += 1
                print("".join(guessed_letters))
            if "".join(guessed_letters) == solution:
                break
        else:
            return 0
        if remaining_lives == 0:
            return 0


if __name__ == "__main__":
    round_number = 0
    start_game = input("Do you want to play? (y/n)")

    while start_game.lower() != "n" and start_game.lower() != "exit":
        result = guess_the_word(round_number)
        round_number += 1
        if remaining_lives == 0 or result == 0:
            print("Game Over")
            break
        if round_number > len(words) - 1:
            print("Game Over")
            break

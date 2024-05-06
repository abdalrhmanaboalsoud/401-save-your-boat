words = [
    {
        'name': "banana",
        'hint': [
            "Yellow fruit",
            "Often found in bunches",
            "Peel before eating"
        ]
    },
    {
        'name': "elephant",
        'hint': [
            "Large mammal",
            "Has a trunk",
            "Big ears"
        ]
    },
    {
        'name': "computer",
        'hint': [
            "Electronic device",
            "Used for processing data",
            "Has a keyboard and screen"
        ]
    }
]

lives = 5
def guess_the_letter(attempts):
    global lives
    word = words[attempts]
    answer = word['name']
    print("Guess this")
    guess_blank = f'{"_" * len(answer)}'
    print(guess_blank)
    print("hint :\n" + word['hint'].pop(0))
    counter = 0
    guess_list = list(guess_blank)

    while(True): 
        guess = input("choose a letter ->")
        if guess != "exit":
            if(guess != answer[counter]):
                print("wrong answer") 
                print("hint :\n" + word['hint'].pop(0))
                lives-=1
                print(f'boat lives {lives}')
                if lives == 1:
                    print("hint :\n" + word['hint'].pop(0))
                    print("hint :\n" + word['hint'].pop(0))
            else:
                print("Correct answer")
                guess_list[counter] = guess
                counter+=1
            print("".join(guess_list))
            if("".join(guess_list) == word['name'] ):
                break
            if(lives == 0):
                return 0
        else:
            return 0
        
if __name__=="__main__":
    attempts=0
    response=input("do you want to play (y,n)")

    while response.lower() != "n" and response.lower() !="exit":
        flag = guess_the_letter(attempts)
        attempts +=1
        if(lives == 0 or flag == 0):
            print("Game over")
            break
        if attempts > len(words)-1:
            print("Game over")
            break

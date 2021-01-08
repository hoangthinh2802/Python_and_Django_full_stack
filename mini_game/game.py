import random

def get_guess():
    return list(input("what is your guess?"))

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code, userGuess):
    if userGuess == code:
        return "CODE CRACKED"

    clues = []

    for ind, num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

print ("Welcome Code Breaker, please guess a 3 digit number")
seccretCode = generate_code()
clueReport = []
while clueReport != "CODE CRACKED":
    guess = get_guess()
    clueReport = generate_clues(guess, seccretCode)
    print("Here is the result of your guess: ")
    for clue in clueReport:
        print(clue)
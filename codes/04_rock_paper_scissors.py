# Rock beats scissors
# Scissors beats paper
# Paper beats rock
import random


def compare(u1,u2):
    translator = {"r": "Rock", 's': "Scissors", 'p': "Paper"}
    print("User choose: ", translator[u1])
    print("Computer choose: ", translator[u2])

    if u1 == u2:
        return "tie"

    elif u1 == "r":
        if u2 == "s":
            return "Rock wins"
        else:
            return "Paper wins"

    elif u1 == 's':
        if u2 == 'p':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'p':
        if u2 == 'r':
            return("Paper wins!")
        else:
            return("Scissors win!")   
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")


user = input("Rock, Paper, Scissors? r/p/s: ")
computer = random.choice(["r",'s','p'])
print(compare(user,computer))

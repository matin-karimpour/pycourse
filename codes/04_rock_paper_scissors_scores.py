# Rock beats scissors
# Scissors beats paper
# Paper beats rock
import random


def compare(u1,u2):
    translator = {"r": "Rock", 's': "Scissors", 'p': "Paper"}
    print("User choose: ", translator[u1])
    print("Computer choose: ", translator[u2])
    
    if u1 == u2:
        return "tie", (0,0)

    elif u1 == "r":
        if u2 == "s":
            return "Rock wins", (1,0)
        else:
            return "Paper wins", (0,1)

    elif u1 == 's':
        if u2 == 'p':
            return "Scissors win!" , (1,0)
        else:
            return "Rock wins!" , (0,1)

    elif u1 == 'p':
        if u2 == 'r':
            return "Paper wins!", (1,0)
        else:
            return "Scissors win!", (0,1)

    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")



def cal_score(u1,u2, result):
    return u1 + result[0], u2 + result[1]
user_score, computer_score = (0,0)
for i in range(3):
    user = input("Rock, Paper, Scissors? r/p/s: ")
    computer = random.choice(["r",'s','p'])
    result,score=compare(user,computer)
    user_score, computer_score= cal_score(user_score, computer_score,score)
    print(result)
    print("user score: ",user_score)
    print("computer score: ", computer_score,"\n")

if user_score > computer_score:
    print("User WIN!")
elif user_score < computer_score:
    print("computer WIN!")
else:
    print("It's a tie!")
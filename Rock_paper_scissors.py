
from random import randrange

while True:
    random_number = randrange(3)
    if random_number ==0:
        rand=str("rock")
    elif random_number == 1:
        rand = str("scissors")
    else:
        rand=str("paper")
    answer = input("Rock, paper, scissors? ")
    if answer == rand:
        print( answer + " and " + rand + " Try again")
        continue
    elif answer == "rock" and rand == "Scissors" or answer == "scissors" and rand == "paper" or answer == "paper" and rand == "rock":
        print(answer + " and " + rand + " You win!")
        break
    else:
        print(answer + " and " + rand + " You loose!")
        continue



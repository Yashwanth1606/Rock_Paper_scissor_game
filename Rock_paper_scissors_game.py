import random

#Rock papper and scissors game
def game(comp , you):
    # if two values are equal then it is a tie
    if (comp == you):
        return None
    
    # check all the possibiltes when comp retrun rock
    elif (comp == 'rock'):
        if (you == 'scissor'):
            return False
        elif (you == 'paper'):
            return True
    
    # check all the possibiltes when comp retrun paper
    elif (comp == 'paper'):
        if (you == 'rock'):
            return False
        elif (you == 'scissor'):
            return True
    
    # check all the possibiltes when comp retrun scissor
    elif (comp == 'scissor'):
        if (you == 'paper'):
            return False
        elif (you == 'rock'):
            return True




print("comp turn Rock(1), Paper(2),Scissors(3):")
random_number = random.randint(1,3)
if random_number == 1:
    comp = 'rock'
elif random_number == 2:
    comp = 'paper'
elif random_number == 3:
    comp = 'scissor'


you = input("your turn rock,paper,scissor:")
final = game(comp,you)

print("computer has chossen ",comp)
print("You have choosen ",you)

if final == None:
    print("It's a tie!")
elif final == True:
    print("You Win!")
else :
    print("You Lose!")

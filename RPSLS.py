# Rock-paper-scissors-lizard-Spock

# imports
import random

# helper functions
def number_to_name(number):    
    if number == 0:
        return 'rock'    
    elif number == 1:
        return 'Spock'    
    elif number == 2:
        return 'paper'   
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'     
    else:
        return 'INVALID NAME'
    
def name_to_number(name):
    if name == 'rock' :
        return 0    
    elif name == 'Spock':
        return 1    
    elif name == 'paper':
        return 2  
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4     
    else:
        return 'INVALID NUMBER'

def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    
    # determine winner
    if difference == 0:
        results = 'Player and computer tie!'
    elif difference >= 1 and difference <= 2:
        results = 'Player wins!'
    elif difference >= 3 and difference <= 4:
        results = 'Computer wins!'
    else:
        results = "Couldn't determine winner"
    
    # convert comp_number to name using number_to_name
    computer_num_to_name = number_to_name(comp_number)
    
    # print results
    print 'Player chooses', name
    print 'Computer chooses', computer_num_to_name
    print results
    print ''
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



# "Guess the number" mini-project
import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
random_number = 0
guesses_left = 0

# define event handlers for control panel
def init():
    range100()
    f.start()
    
def range100():
    # button that changes range to range [0,100) and restarts
    global random_number, guesses_left, num_range
    num_range = 100
    random_number, guesses_left = random.randrange(0, 100), 7
    print "New game. Range is from 0 to 100"
    print "Number of guesses remaining: ", guesses_left, "\n"
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global random_number, guesses_left, num_range
    num_range = 1000
    random_number, guesses_left = random.randrange(0, 1000), 10
    print "New game. Range is from 0 to 1000"
    print "Number of guesses remaining: ", guesses_left, "\n"
    
def within_range(guess):
    # make sure user is entering a number that falls within the
    # specified range
    global num_range
    if int(guess) >= 0 and int(guess) < num_range:
        return True
    else:
        return False
    
def get_input(guess):
    # main game logic goes here	
    global guesses_left, random_number
    guesses_left -= 1
    print "Guess entered: ", guess
    print "Number of remaining guesses is ", guesses_left
    
    if int(guess) > random_number and within_range(guess) and guesses_left != 0:
        print "Lower!\n"
    elif int(guess) < random_number and within_range(guess) and guesses_left != 0:
        print "Higher!\n"
    elif int(guess) == random_number:
        print "You got it right!\n"
        range100()
    elif guesses_left == 0 and int(guess) != random_number:
        print "You ran out of guesses, the correct number is ", random_number, "\n"
        range100()
    else:
        print "Guess does not fall within range, Try Again.\n"
    
    
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
init()
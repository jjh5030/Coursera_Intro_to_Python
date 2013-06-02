# implementation of card game - Memory
import simplegui
import random

list_cards = []
list_status = []
cards_clicked = []
num_moves = 0
# helper function to initialize globals
def init():
    global list_cards, list_status, num_moves
    temp_list1 = range(0,8)
    temp_list2 = range(0,8)
    list_cards = temp_list1 + temp_list2
    random.shuffle(list_cards)
    list_status = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    del cards_clicked[:]
    num_moves = 0
     
# define event handlers
def mouseclick(pos):
    global list_cards, list_status, cards_clicked, num_moves
    # add game state logic here
    if num_moves == 0:
        num_moves += 1
        
    if list_status[pos[0] // 50] == 0:
        list_status[pos[0] // 50] = 1
        cards_clicked.append(pos[0] // 50)
        
    if len(cards_clicked) == 3:
        num_moves += 1
        if list_cards[cards_clicked[0]] == list_cards[cards_clicked[1]]:
            list_status[cards_clicked[0]] = 2
            list_status[cards_clicked[1]] = 2
            del cards_clicked[:2]
        else:
            list_status[cards_clicked[0]] = 0
            list_status[cards_clicked[1]] = 0
            del cards_clicked[:2]
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list_cards, list_status, num_moves
    position = 15
    cover = 0
    check = 0
    box = 0
    for x in list_cards:
        if list_status[check] != 0:
            canvas.draw_text(str(x), (position, 65), 48, "Red")
        else:
            canvas.draw_polygon([[box, 0], [box + 50, 0], [box + 50, 100], [box,100]], 1, "white", "green")
        position += 50
        check += 1
        box += 50
        label.set_text("Moves = " + str(num_moves))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
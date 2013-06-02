# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [300, 200]
ball_vel = [0.0, 0.0]
score1 = 0
score2 = 0
status = False

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel# these are floats
    ball_pos = [300, 200]
    if right == True:
        x = - random.randrange(120, 240) / 60
    else:
        x = random.randrange(120, 240) / 60
    y = - random.randrange(60, 180) / 60
    ball_vel = [x, y]

# define event handlers
def reset():
    global ball, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel# these are floats
    global score1, score2, status  # these are ints
    paddle1_pos = 200
    paddle2_pos = 200
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    ball_pos = [300, 200]
    ball_vel = [0.0, 0.0]
    status = False

def new_game():
    global status  # these are ints    
    if status == True:
        ball_init(True)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    elif paddle1_pos + paddle1_vel < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    else:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel 
    elif paddle2_pos + paddle2_vel < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    else:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # update ball
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score2 += 1
            ball_init(False)
            
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score1 += 1
            ball_init(True)
            
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), (150, 50), 48, "White")
    c.draw_text(str(score2), (450, 50), 48, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, status
    acc = 6
    if key==simplegui.KEY_MAP["w"] and status == True:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"] and status == True:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["down"] and status == True:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"] and status == True:
        paddle2_vel -= acc    
    elif key==simplegui.KEY_MAP["b"] and status == False:
        status = True
        new_game()        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label("Hit the letter 'b' to begin")
frame.add_button("Reset", reset, 150)

# start frame
frame.start()
reset()
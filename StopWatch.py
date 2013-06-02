# "Stopwatch: The Game"

# Import modules
import simplegui

# define global variables
display_text = "0:00.0"
interval = 100
timer_count = 0
a = 0
b = 0
c = 0
success_stops = 0
failed_stops = 0
total_stops = 0
results = "0 / 0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):  
    return get_min(t) + ":" + get_sec(t) + "." + get_milli_sec(t)

# get milli seconds
def get_milli_sec(t):
    global c
    t = str(t)
    c = int(t[-1])
    return t[-1]

# get seconds
def get_sec(t):
    t = str(t)
    if len(t) == 2 and int(t) < 600:
        b =  t[0]
    elif len(t) == 3 and int(t) < 600:
        b = t[:2]
    elif int(t) > 600:
        b = str((int(t) % 600) // 10)
    else:
        b = "00"
    return pad_sec(b)

# get minutes
def get_min(t):
    if t >= 600:
        a = str(t // 600)
    else:
        a = "0"        
    return a

# pad out seconds to 2 digits
def pad_sec(t):
    if len(t)== 0:
        t = "00"
    elif len(t) == 1:
        t = "0" + t
    else:
        t = t
    return t
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    timer.start()

def button_stop():
    if timer.is_running():
        timer.stop()        
        global timer_count, success_stops, failed_stops, total_stops, results
        #print timer_count, get_milli_sec(timer_count)
        total_stops += 1        
        if int(get_milli_sec(timer_count)) == 0:
            success_stops += 1
        else:
            failed_stops += 1     
        results = str(success_stops) + " / " + str(total_stops)

def button_reset():
    timer.stop()
    global timer_count, a, b, c, success_stops, failed_stops, results, total_stops
    timer_count = 0
    a = 0
    b = 0
    c = 0
    failed_stops = 0 
    success_stops = 0
    total_stops = 0
    results = "0 / 0"
    #print "\nNew Game\n"

# define event handler for timer with 0.1 sec interval
def tick():
    global timer_count
    timer_count += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(timer_count), [60, 110], 36, "White")
    canvas.draw_text(results, [140, 25], 24, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
frame.add_button("Start", button_start, 100)
frame.add_button("Stop", button_stop, 100)
frame.add_button("Reset", button_reset, 100)

# start frame
frame.start()

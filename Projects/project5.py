import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
# message_sprite.hideturtle()
message_sprite = create_sprite("alien", -350,150)
message_sprite.hideturtle()
message_sprite.write("tag the other person")
set_background("bikini_bottom")
sprite_list = []

who_is_it = "sponge_bob"
points2 = 0
points = 0
x1 = -1
y1 = -200
s1 = create_sprite("sponge_bob.gif",x1,y1)

x1 = 150
y1 = 150
p1 = create_sprite("Patrick.gif",x1,y1)

def move_up():
    x = s1.xcor()
    y = s1.ycor() + 4
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 4
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 6
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 6
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")





def move_up():
    x = p1.xcor()
    y = p1.ycor() + 4
    p1.goto(x,y)
        
def move_down():
    x = p1.xcor()
    y = p1.ycor() - 4
    p1.goto(x,y)
    
def move_left():
    x = p1.xcor() - 6
    y = p1.ycor() 
    p1.goto(x,y)
    
def move_right(): 
    x = p1.xcor() + 6
    y = p1.ycor() 
    p1.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")





# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000): 
    message_sprite.clear()
    message_sprite.write(f"points: {points}:",font=("Arial",30,"normal"))

    if get_distance(s1 , p1) < 100:
        if who_is_it == "sponge_bob":
            points += 1
            who_is_it = "patrick"
            s1.goto (-1, -200)
            p1.goto (150, 150)
        elif who_is_it == "patrick":
            points2 += 1 
            who_is_it = "sponge_bob"
            s1.goto (-1, -200)
            p1.goto (150, 150)








    # if get_distance(s1,p1 ) <100:
    #     points += 1
   
   
   
   
   
   
   
   
    # TODO - add code for automatic actions


    # TODO - make an if statement for ending the game

    time.sleep(0.01)
    window.update()
       

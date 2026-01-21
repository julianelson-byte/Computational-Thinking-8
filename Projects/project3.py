import turtle, time, 
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -150
y1 = 100
x2 = -150
y2 = 50
x3 = -150
y3 = 0
x4 = -150
y4 = -50


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("barn")
t1 = create_sprite("dog",x1,y1)
t2 = create_sprite("flower",x2,y2)
t3 = create_sprite("basketball",x3,y3)
t4 = create_sprite("fish",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
#The dog will be the fastest because its speed is set to 17 which is the highest. basketball will be the slowest because its speed is the slowest
for i in range(30):random
    x1 += 17
    x2 += 15
    x3 += 10
    x4 += 15

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Dog wins!!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("Dog wins!") 
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("Dog Wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    print("Dog wins!")



turtle.exitonclick()
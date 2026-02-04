import turtle, time, random
from utils import *

# Section 1 - setup
set_background("barn")
raindrop = 10
flower = 10

x1 = -80
y1 = -200

w1 = create_sprite("flower.gif",x1,y1)
waterlist = []
message_sprite = create_sprite("alien", -350,150)
message_sprite.hideturtle()
message_sprite.write("keep your flower alive by giving it sun water and keeping it healthy")



def water_flower ():
    global raindrop
    raindrop += 1
    x = random.randint (-200,200)
    y = 200
    w1 = create_sprite("water_flower",x,y)
    waterlist.append(w1)
window.onkeypress(water_flower,"space")
#Press "the space key" to make raindrops come down on screen
def message ():
    w1.write ("can you please water me!",font = ("Arial", 20, "normal"))
    window.update()
    time.sleep(3)
    w1.clear()
window.onkeypress(message, "a")

#press the "a" key to make the "flower say can you please water me!" and the message will go away after 3 seconds.

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()

    message_sprite.write(f"flower: {flower}", font=("Arial", 30, "normal"))
    # TODO - put any automatic actions here
    for w1 in waterlist:
        w1.setheading(270)
        w1.forward(5)

    time.sleep(0.01)
    window.update()
    
#the goal of my game is to get the flower to say a message with "a" key and water it with the "space key"
   
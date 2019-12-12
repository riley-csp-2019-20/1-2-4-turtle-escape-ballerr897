import random 
import turtle as trtl
keagan = trtl.Turtle()

player_bot = trtl.Turtle()

keagan.speed(0)
wall_width = 10
distance = 15 
keagan.left(90)
door_width = 10
keagan.ht()






def drawDoor():
    keagan.penup()
    keagan.forward(door_width)
    keagan.pendown()


def drawBarrier():
    keagan.right(90)
    keagan.forward(wall_width*2)
    keagan.backward(wall_width*2)
    keagan.left(90)



for i in range (25):
    if i > 4:
        door = random.randint(wall_width, distance - 2 * door_width)
        barrier = random.randint(wall_width, distance - 2 * door_width)
 
        if (door < barrier):
            keagan.forward(door)
            keagan.penup()
            keagan.forward(door_width)
            keagan.pendown()
            keagan.forward(barrier - door - door_width)
            keagan.right(90)
            keagan.forward(wall_width)
            keagan.backward(wall_width)
            keagan.left(90)
            keagan.forward(distance - barrier)
        elif (door > barrier): 
            keagan.forward(barrier)
            keagan.right(90)
            keagan.forward(wall_width)
            keagan.backward(wall_width)
            keagan.left(90)
            keagan.forward(door - barrier)
            keagan.penup()
            keagan.forward(door_width)
            keagan.pendown()
            keagan.forward(distance - door - door_width)
    keagan.left(90)
    distance += wall_width






def up():
    player_bot.setheading(90)
    player_bot.forward(5)




def down():
    player_bot.setheading(270)
    player_bot.forward(5)



def left():
    player_bot.setheading(180)
    player_bot.forward(5)



def right():
    player_bot.setheading(0)
    player_bot.forward(5)



wn = trtl.Screen()

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.listen()
wn.mainloop()
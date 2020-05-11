#Diamond  Ship - Part 1
#Set up the screen
# 
import turtle 
import os 

# Set up the screen 
wn = turtle.Screen()
wn.bgcolor("purple")
wn.title("Diamond Ship") 

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen._color("pink")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtlre
player = turtle.Turtle()
player.color("pink")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Create the enemy
enemy = turtle.Turtle()
enemy.color("pink")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed =2
#Move the plater left and right
def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x = -280
    player.setx(x) 


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
       x = 280    
    player.setx(x)



#Create keyboared bindings
turtle.Screen().listen()
turtle.Screen().onkey(move_left, "Left")
turtle.Screen().onkey(move_right, "Right")









#Main game loop 
while True:

    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move the enemy back and down 
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40 
        enemyspeed *= -1
        enemy.sety(y)










delay = input ("Press enter to finsh.")
from itertools import count
import turtle as turtle
import time
import math
import random

screen = turtle.Screen()

screen.screensize(1024,768)
screen.setup(1024,768)
screen.bgcolor("black")
screen.title("Cubes") 


# turtles
t1 = turtle.Turtle()
t1.hideturtle()
t1.speed(5)
t1.color("red")
t2 = turtle.Turtle()
t2.hideturtle()
t2.speed(3)
t2.color("yellow")
t3 = turtle.Turtle()
t3.hideturtle()
t3.speed(4)
t3.color("green")

turtles = (t1,t2,t3)

turtle.tracer(20,0)
#turtle.tracer(0,0)


#turtle.mode('world')
turtle.speed(0)
turtle.hideturtle()
screen = turtle.Screen()

firstRun = True


def generate_cube(turtles, x_extremity, x_rear, origin, angle, heading):
    global firstRun
    #if firstRun == True:
    t1_extremity = x_extremity
    t1_rear = x_rear
    t1_angle = angle
    t1_heading = heading

    t2_extremity = x_extremity - random.uniform(20,50)
    t2_rear = x_rear - random.uniform(90,100) 
    t2_angle = angle - random.uniform(20,90)
    t2_heading = heading - 60

    t3_extremity = x_extremity - random.uniform(10,30)
    t3_rear = x_rear - random.uniform(60,80)
    t3_angle = angle - random.uniform(170,270)
    t3_heading = heading - 120
    
    while t1_extremity > 0 and t2_extremity > 0 and t3_extremity > 0:
        for my_pen in turtles:
            if my_pen == t1:
                x_extremity = t1_extremity
                x_rear = t1_rear
                angle = t1_angle
                heading = t1_heading
            if my_pen == t2:
                x_extremity = t2_extremity
                x_rear = t2_rear
                angle = t2_angle
                heading = t2_heading
            if my_pen == t3:
                x_extremity = t3_extremity
                x_rear = t3_rear
                angle = t3_angle
                heading = t3_heading
            #time.sleep(0.1)
            #heading += 30
            #angle += 10
            #x_extremity -= 5
            #x_rear -= 2

            my_pen.clear() 

            my_pen.penup()
            
            #draw top point
            my_pen.setheading(heading)
            my_pen.forward(x_extremity)
            front_top_right = my_pen.pos()
            x_extremity -= 2

            my_pen.pendown()
            my_pen.right(90)

            #calculate horizontal distance
            if (angle != 90):
                a = ((math.sin(angle) * x_extremity)/(math.sin(180-(90+angle))))
            else:
                a = ((math.sin(angle) * x_extremity)/(math.sin(180-(90+89.99999))))

            my_pen.forward(a)
            front_bottom_right = my_pen.pos()
            my_pen.right(90)
            my_pen.forward(a)
            front_bottom_left = my_pen.pos()
            my_pen.right(90)
            my_pen.forward(a)
            front_top_left = my_pen.pos()
            my_pen.right(90)
            my_pen.forward(a)
            front_top_right = my_pen.pos()

            #x_extremity -= 3
            my_pen.penup()
            my_pen.goto(0,0)

            my_pen.forward(x_rear)
            my_pen.pendown()
            back_top_right = my_pen.pos()



            my_pen.right(90)
            if (angle != 90):
                a2 = ((math.sin(angle) * x_rear)/(math.sin(180-(90+angle))))
            else:
                a2 = ((math.sin(angle) * x_rear)/(math.sin(180-(90+89.99999))))
            my_pen.forward(a2)
            back_bottom_right = my_pen.pos()
            my_pen.right(90)
            my_pen.forward(a2)
            back_bottom_left = my_pen.pos()
            my_pen.right(90)
            my_pen.forward(a2)
            back_top_left = my_pen.pos()
            my_pen.right(90)
            my_pen.forward(a2)
            back_top_right = my_pen.pos()

            
            # make rear converge differently
            if (a != 0):
                x_rear -= ((a2 * 1) / a)
            
            # connect squares
            my_pen.goto(front_top_right)
            my_pen.penup()
            my_pen.goto(front_bottom_right)
            my_pen.pendown()
            my_pen.goto(back_bottom_right)
            my_pen.penup()
            my_pen.goto(back_bottom_left)
            my_pen.pendown()
            my_pen.goto(front_bottom_left)
            my_pen.penup()
            my_pen.goto(front_top_left)
            my_pen.pendown()
            my_pen.goto(back_top_left)
            my_pen.penup()
            my_pen.goto(back_top_right)
            my_pen.pendown()
            my_pen.goto(front_top_right)
            my_pen.penup()

            
            my_pen.penup()
            my_pen.goto(origin)
            #time.sleep(1)
            if heading >= 360:
                heading = 0
            firstRun = False
            if my_pen == t1:
                t1_extremity = x_extremity
                t1_rear = x_rear
                t1_angle = angle
                t1_heading = heading
            if my_pen == t2:
                t2_extremity = x_extremity
                t2_rear = x_rear
                t2_angle = angle
                t2_heading = heading
            if my_pen == t3:
                t3_extremity = x_extremity
                t3_rear = x_rear
                t3_angle = angle
                t3_heading = heading


#Generate cubes of differing locations

origin = (0,0)
heading = 0
for i in range (0,16):
    x_extremity = random.uniform(512,600)
    generate_cube(turtles, x_extremity,x_extremity-random.uniform(50,150),origin,random.uniform(5,30),heading)

    
#    heading += random.uniform(0,10)

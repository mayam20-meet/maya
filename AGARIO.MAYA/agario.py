import turtle
import time 
import random
import math 
from ball import Ball

#part 1 create a ball


turtle.tracer(0)
turtle.hideturtle()
turtle_gameover = turtle.clone()
runinng =  True 
screen_width = turtle.getcanvas().winfo_width()/2
screen_hight = turtle.getcanvas().winfo_height()/2
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

my_ball = Ball(100,35,21,23,50,random_color())

number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
Balls=[]

for i in range (number_of_balls):
    x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    y = random.randint(-screen_hight + maximum_ball_radius,screen_hight - maximum_ball_radius)
    dx = random.randint(minimum_ball_dx,maximum_ball_dx)
    dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    r = random.randint(minimum_ball_radius,maximum_ball_radius)
    color = random_color()
    my_new_ball = Ball(x,y,dx,dy,r,color)
    Balls.append(my_new_ball)

# Part 2 :move the balls
def move_all_balls ():
    for ball in Balls:
        ball.move(screen_width,screen_hight)

# Part 3 : check for ball collisions

def collide (ball_a,ball_b):
    if ball_a == ball_b:
        return False
    d = math.sqrt(math.pow(ball_a.pos()[0]-ball_b.pos()[0], 2) + math.pow(ball_a.pos()[1] - ball_b.pos()[1], 2))
    if (ball_a.r + ball_b.r >=d):
        return True
    else:
        return False

#part 4 : check collisions

def check_all_collisions ():
    all_balls =[]
    all_balls.append(my_ball)

    for ball in Balls:
        all_balls.append(ball)
    for ball_a in all_balls:
        for ball_b in all_balls:
            if collide(ball_a, ball_b):
                r_ba = ball_a.r
                r_bb = ball_b.r

                x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
                y = random.randint(-screen_hight + maximum_ball_radius,screen_hight - maximum_ball_radius)
                dx = random.randint(minimum_ball_dx,maximum_ball_dx)

                while (dx == 0):
                    dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                while (dy == 0):
                    dy = random.randint(minimum_ball_dy,maximum_ball_dy)

                r = random.randint(minimum_ball_radius,maximum_ball_radius)
                color = random_color()

                if r_ba < r_bb:
                    ball_a.new_ball(x,y,dx,dy,r,color)
                    ball_b.r = ball_b.r + 5
                    ball_b.shapesize((ball_b.r+1)/10)
                    if ball_a == my_ball:
                        turtle_gameover.write("GAME OVER",font=("Arial Black", 80, "normal"),align="center")
                        print("GAME OVER")
                        quit()
                    
                elif r_ba > r_bb:
                    ball_b.new_ball(x,y,dx,dy,r,color)
                    ball_a.r = ball_a.r + 5
                    ball_a.shapesize((ball_a.r+1)/10)
                    if ball_b == my_ball:
                        turtle_gameover.write("GAME OVER")
                        print("GAME OVER",font=("Arial Black", 80, "normal"),align="center")
                        running = False
                    
                    
                else:
                    
                    pass
                
#part 5
def movearound ():
    my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width*2 , screen_hight*2 - turtle.getcanvas().winfo_pointery())


running = True
while running is True:
    print(len(Balls))
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_hight = turtle.getcanvas().winfo_height()/2

    movearound()
    move_all_balls()
    check_all_collisions()

    time.sleep(.1)
    turtle.update()

turtle.update()
turtle.mainloop()
                
                    
                    
                

    
    




# This file was created by: Kiran Bogusky
# This file was created by: Chris Cozort

'''
Goals -
when a user clicks on their choice, the computer chooses randomly and display the results.

Current progress:
    Started to merge old rps game and turtle, but have nut integrated them properly.

'''

# import package
import turtle
from turtle import *
from random import randint
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))



# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choiceposx = -300
bg_img = os.path.join(images_folder, 'rps_bg')
# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="#aae5ff")
rps_choices = ["rock", "paper", "scissors"]
# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# creating the functions to be called later. each function summons an instance of a designated shape, either for the computer or the cpu.
def show_rock(x, y):
    global rock_instance
    # setup the rock image using the os module as rock_image
    rock_image = os.path.join(images_folder, 'rock.gif')
    # instantiate (create an instance of) the Turtle class for the rock
    rock_instance = turtle.Turtle()
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # assign vars for rock position
    rock_pos_x = x
    rock_pos_y = y
    # set the position of the rock_instance
    rock_instance.setpos(rock_pos_x,rock_pos_y)

def CPU_show_rock(x, y):
    global CPU_rock_instance
    # setup the rock image using the os module as rock_image
    rock_image = os.path.join(images_folder, 'rock.gif')
    # instantiate (create an instance of) the Turtle class for the rock
    CPU_rock_instance = turtle.Turtle()
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    CPU_rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    CPU_rock_instance.penup()
    # assign vars for rock position
    CPU_rock_pos_x = x
    CPU_rock_pos_y = y
    # set the position of the rock_instance
    CPU_rock_instance.setpos(CPU_rock_pos_x,CPU_rock_pos_y)

def show_paper(x, y):
    global paper_instance
    # setup the paper image using the os module as paper_image
    paper_image = os.path.join(images_folder, 'paper.gif')
    # instantiate (create an instance of) the Turtle class for the paper
    paper_instance = turtle.Turtle()
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # assign vars for paper position
    paper_pos_x = x
    paper_pos_y = y
    # set the position of the paper_instance
    paper_instance.setpos(paper_pos_x,paper_pos_y)
def CPU_show_paper(x, y):
    global CPU_paper_instance
    # setup the paper image using the os module as paper_image
    paper_image = os.path.join(images_folder, 'paper.gif')
    # instantiate (create an instance of) the Turtle class for the paper
    CPU_paper_instance = turtle.Turtle()
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    CPU_paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    CPU_paper_instance.penup()
    # assign vars for paper position
    CPU_paper_pos_x = x
    CPU_paper_pos_y = y
    # set the position of the paper_instance
    CPU_paper_instance.setpos(CPU_paper_pos_x,CPU_paper_pos_y)

def show_scissors(x, y):
    global scissors_instance
    # setup the scissors image using the os module as scissors_image
    scissors_image = os.path.join(images_folder, 'scissors.gif')
    # instantiate (create an instance of) the Turtle class for the scissors
    scissors_instance = turtle.Turtle()
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # assign vars for scissors position
    scissors_pos_x = x
    scissors_pos_y = y
    # set the position of the scissors_instance
    scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
def CPU_show_scissors(x, y):
    global CPU_scissors_instance
    # setup the scissors image using the os module as scissors_image
    scissors_image = os.path.join(images_folder, 'scissors.gif')
    # instantiate (create an instance of) the Turtle class for the scissors
    CPU_scissors_instance = turtle.Turtle()
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    CPU_scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    CPU_scissors_instance.penup()
    # assign vars for scissors position
    CPU_scissors_pos_x = x
    CPU_scissors_pos_y = y
    # set the position of the scissors_instance
    CPU_scissors_instance.setpos(CPU_scissors_pos_x,CPU_scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

# this function uses an x and y value of the mouse, an obj parameter and the width and height of the image to determine whether the mouse is inside of a chosen image.
# compared
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick
def mouse_pos(x, y):
    # this function detects if the mouse has collided with the hitboxes. it is split into three hitboxes, modeled the same.
    # this is rock's. it uses the colide function to see if the x and y coordinates match the hitboxes.
    if collide(x,y,rock_instance,rock_w,rock_h):

        print("I chose rock")
        # write above -300, the player's choice
        text.penup()
        text.goto(-300, int(3*(HEIGHT/10)))
        text.write('''player chooses:
        rock''', False, "center", ("Roboto", 24, "normal"))
        # sets player value to choice
        player="rock"
        # hides the other instances
        scissors_instance.hideturtle()
        paper_instance.hideturtle()
        # creates a random cpu choice
        CPU_choose = rps_choices[randint(0, len(rps_choices)-1)]
        # this then checks the cpu choice, and shows that
        if CPU_choose == "rock":
            CPU_show_rock(300, 0)
            print("CPU chose rock")
            text.penup()
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            rock''', False, "center", ("Roboto", 24, "normal"))
            # hides the unused instances.
            scissors_instance.hideturtle()
            paper_instance.hideturtle()
            # runs evaluate function to compare the others.
            evaluate(player, CPU_choose)
        elif CPU_choose == "paper":
            CPU_show_paper(300, 0)
            print("CPU chose paper")
            text.penup
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            paper''', False, "center", ("Roboto", 24, "normal"))

            scissors_instance.hideturtle()
            paper_instance.goto(300, 0)
            evaluate(player, CPU_choose)
        elif CPU_choose == "scissors":
            CPU_show_scissors(300, 0)
            text.penup()
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            scissors''', False, "center", ("Roboto", 24, "normal"))
            paper_instance.hideturtle()
            scissors_instance.goto(300, 0)
            evaluate(player, CPU_choose)

    elif collide(x,y,paper_instance,paper_w,paper_h):
        print("I chose paper")
        text.penup()
        text.goto(300, int(3*(HEIGHT/10)))
        text.write('''CPU chooses:
        paper''', False, "center", ("Roboto", 24, "normal"))
        player="paper"
        scissors_instance.hideturtle()
        rock_instance.hideturtle()
        paper_instance.goto(-300, 0)
        CPU_choose = rps_choices[randint(0, len(rps_choices)-1)]
        if CPU_choose == "rock":
            CPU_show_rock(300, 0)
            print("CPU chose rock")
            text.penup()
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            rock''', False, "center", ("Roboto", 24, "normal"))
            scissors_instance.hideturtle()
            evaluate(player, CPU_choose)
        elif CPU_choose == "paper":
            CPU_show_paper(300, 0)
            print("CPU chose paper")
            text.penup
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            paper''', False, "center", ("Roboto", 24, "normal"))

            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            paper_instance.goto(300, 0)
            evaluate(player, CPU_choose)
        elif CPU_choose == "scissors":
            CPU_show_scissors(300, 0)
            text.penup()
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            scissors''', False, "center", ("Roboto", 24, "normal"))
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            scissors_instance.goto(300, 0)
            evaluate(player, CPU_choose)
        
        
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        print("I chose scissors")
        text.penup()
        text.goto(-300, int(3*(HEIGHT/10)))
        text.write('''CPU chooses:
        scissors''', False, "center", ("Roboto", 24, "normal"))
        player="scissors"

        scissors_instance.goto(-300, 0)
        CPU_choose = rps_choices[randint(0, len(rps_choices)-1)]
        if CPU_choose == "rock":
            CPU_show_rock(300, 0)
            print("CPU chose rock")
            text.penup()
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            rock''', False, "center", ("Roboto", 24, "normal"))
            paper_instance.hideturtle()
            evaluate(player, CPU_choose)
        elif CPU_choose == "paper":
            CPU_show_paper(300, 0)
            print("CPU chose paper")
            text.penup
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            paper''', False, "center", ("Roboto", 24, "normal"))


            rock_instance.hideturtle()
            paper_instance.goto(300, 0)
            evaluate(player, CPU_choose)
        elif CPU_choose == "scissors":
            CPU_show_scissors(300, 0)
            text.penup()
            text.goto(300, int(3*(HEIGHT/10)))
            text.write('''CPU chooses:
            scissors''', False, "center", ("Roboto", 24, "normal"))
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            scissors_instance.goto(300, 0)
            evaluate(player, CPU_choose)

        
    else:
        print("You chose nothing, you fool. you absolute buffoon! you must be flogged in the street for such impertinence!")
    
# this calls the show functions to make the images appear.
show_paper(0, 0)
show_rock(-300, 0)
show_scissors(300, 0)


def evaluate(player, CPU):
# Each of these segments compares player to cpu to find out the score. if the score is correct, it writes the result.
    if player == CPU:
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("It's a tie!", False, "center", ("Roboto", 24, "normal"))
    elif player == "rock" and CPU == "scissors":
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("Player wins!", False, "center", ("Roboto", 24, "normal"))
    # These continue on with more comparisons.
    elif player == "scissors" and CPU == "paper":
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("Player wins!", False, "center", ("Roboto", 24, "normal"))

    elif player == "paper" and CPU == "rock":
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("Player wins!", False, "center", ("Roboto", 24, "normal"))

    elif player == "paper" and CPU == "scissors":
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("CPU wins!", False, "center", ("Roboto", 24, "normal"))

    elif player == "rock" and CPU == "paper":
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("CPU wins!", False, "center", ("Roboto", 24, "normal"))

    elif player == "scissors" and CPU == "rock":
        text.goto(0, int(3*(HEIGHT/10)))
        text.write("CPU wins!", False, "center", ("Roboto", 24, "normal"))


screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()

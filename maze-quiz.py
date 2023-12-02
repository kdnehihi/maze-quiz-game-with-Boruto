# Maze and Quiz with Boruto game
# authors: Dinh Dang Khoa Tran and Rohan

import turtle
import random
import math

turtle.tracer(False)
s = turtle.Screen()
s.bgcolor("black")
s.title("Boruto: The world discovery")
t1 = turtle.Turtle()
t1.speed(0)
turtle.addshape("play.gif")
turtle.addshape("shuriken.gif")
turtle.addshape("screen_bg.gif")
turtle.addshape("victory.gif")
turtle.addshape("victory_cup.gif")
for i in range(1, 11):  #add shapes for all questions
  turtle.addshape("ques" + str(i) + ".gif")
  turtle.addshape("ans" + str(i) + "A" + ".gif")
  turtle.addshape("ans" + str(i) + "B" + ".gif")
  turtle.addshape("ans" + str(i) + "C" + ".gif")
  turtle.addshape("ans" + str(i) + "D" + ".gif")
turtle.addshape("correct.gif")
turtle.addshape("incorrect.gif")
turtle.addshape("gameover.gif")
turtle.addshape("tryagain.gif")
g1 = turtle.Turtle()  #game over screen image
g1.hideturtle()
questionsFile = open("questions.txt")
questions = questionsFile.readlines()
for q in range(len(questions)):
  questions[q] = questions[q].strip()  #strip whitespace


correct_list = open("correct.txt").readlines()
for c in range(len(correct_list)):
  correct_list[c] = correct_list[c].strip()  #strip whitespace

t1.shape("play.gif")
t1.goto(0, 0)
t1.showturtle()

t_text = turtle.Turtle()  #to write questions from txt file

t = turtle.Turtle()
turtle.addshape("character.gif")
s.screensize(650, 650)
s.setup(675, 675)
t.hideturtle()
t.speed(100)

square_side = 25
ypos = 1  #pos based on index
xpos = 1
quesNum = 0  #keeps track of what question player is on
timesIncorrect = 0
w = turtle.Turtle()
w.shape("character.gif")
w.shapesize(1, 1, 1)


def draw_cell(color, pen_color):
  t.pencolor(pen_color)
  t.fillcolor(color)
  t.begin_fill()
  for i in range(4):
    t.forward(square_side)
    t.right(90)
  t.end_fill()


def up():
  global xpos
  global ypos
  if (maze_list[ypos - 1][xpos]
      in [" ",
          "@"]):  #checks based on indexes of maze_list to see if "#" or " "
    w.penup()
    w.setheading(90)
    w.forward(25)
    ypos -= 1  #update position
    check()
    victory()


def down():
  global xpos
  global ypos
  if (maze_list[ypos + 1][xpos] in [" ", "@"]):
    w.penup()
    w.setheading(270)
    w.forward(25)
    ypos += 1
    check()
    victory()


def right():
  global xpos
  global ypos
  if (maze_list[ypos][xpos + 1] in [" ", "@"]):
    w.penup()
    w.setheading(0)
    w.forward(25)
    xpos += 1
    check()
    victory()


def left():
  global xpos
  global ypos
  if (maze_list[ypos][xpos - 1] in [" ", "@"]):
    w.penup()
    w.setheading(180)
    w.forward(25)
    xpos -= 1
    check()
    victory()


def check():
  for clone in clones:
    if (w.distance(clone.xcor(), clone.ycor()) < 20):
      clone.hideturtle()
      clones.remove(clone)
      display_quiz()


used_indices = []


def display_quiz():

  # Create a list to keep track of used question indices

  # Select a random index that has not been used
  random_index = random.choice(
      [i for i in range(len(questions)) if i not in used_indices])

  # Mark the selected index as used
  used_indices.append(random_index)

  # Use the selected index to access the question and answer
  randomQ = questions[random_index]

  global quiz_screen
  global ansA
  global ansB
  global ansC
  global ansD
  global q1
  ind = questions.index(randomQ)

  quiz_screen = turtle.Turtle()
  quiz_screen.shape("screen_bg.gif")
  t_text.penup()
  t_text.goto(0, -100)
  t_text.write(questions[ind],
               False,
               align="center",
               font=("Arial", 16, "normal"))
  q1 = turtle.Turtle()
  q1.shape("ques" + str(ind + 1) + ".gif")
  q1.penup()
  q1.goto(0, 150)
  ansA = turtle.Turtle()
  ansA.shape("ans" + str(ind + 1) + "A.gif")
  ansA.penup()
  ansA.goto(-200, -150)
  if (str(ind + 1) + "A") in correct_list:
    ansA.onclick(correct)
  else:
    ansA.onclick(incorrect)
  ansB = turtle.Turtle()
  ansB.shape("ans" + str(ind + 1) + "B.gif")
  ansB.penup()
  ansB.goto(-200, -250)
  if (str(ind + 1) + "B") in correct_list:
    ansB.onclick(correct)
  else:
    ansB.onclick(incorrect)
  ansC = turtle.Turtle()
  ansC.shape("ans" + str(ind + 1) + "C.gif")
  ansC.penup()
  ansC.goto(200, -150)
  if (str(ind + 1) + "C") in correct_list:
    ansC.onclick(correct)
  else:
    ansC.onclick(incorrect)
  ansD = turtle.Turtle()
  ansD.shape("ans" + str(ind + 1) + "D.gif")
  ansD.penup()
  ansD.goto(200, -250)
  if (str(ind + 1) + "D") in correct_list:
    ansD.onclick(correct)
  else:
    ansD.onclick(incorrect)
  s.listen()


def game_over():

  def show_turtle():
    g1.shape("gameover.gif")
    g1.showturtle()

  turtle.ontimer(show_turtle, 2000)
  s.listen()


def victory():
  if w.distance(cup.xcor(), cup.ycor()) < 25:
    global vic
    vic = turtle.Turtle()
    vic.shape("victory.gif")
    vic.showturtle()


clones = []
maze_list = [
    "##########################", "#          ######## ######",
    "# #        ######## ######", "#@################# ######",
    "#  @     ########## ######", "###     @          @   ###",
    "###    @    ####    ######", "### ###  #################",
    "### ###  #################", "### ###  #################",
    "### ###  @               #", "### ###  #################",
    "### ###  #################", "#######  @  #####    @  ##",
    "######### ############  ##", "######### ############  ##",
    "######### ############  ##", "###                @    ##",
    "###  #######  ########  ##", "###  #######  ########  ##",
    "############  ########  ##", "############  ########  ##",
    "###   @       ########  ##", "###           ########  ##",
    "###### ###############  ##", "###### ###################",
    "###### ###################"
]


def game(x, y):
  t1.hideturtle()
  g1.hideturtle()
  global cup
  cup = turtle.Turtle()
  cup.shape("victory_cup.gif")
  cup.pencolor("")
  cup.goto(-162.5, -313.5)

  for i in range(len(maze_list)):  #create maze
    t.penup()
    t.goto(-square_side * 13, square_side * 13 - i * square_side)
    t.pendown()
    for j in maze_list[i]:
      if j == "#":
        draw_cell("white", "black")
      elif j == "@":
        clone = turtle.Turtle()
        clone.pencolor("")
        clone.shape("shuriken.gif")
        clone.penup()
        t.right(45)
        t.forward(math.sqrt(square_side**2))
        clone.goto(t.position())
        t.right(180)
        t.forward(math.sqrt(square_side**2))
        t.right(135)
        clones.append(clone)
      else:
        draw_cell("", "")
      t.pencolor("")
      t.forward(square_side)
  w.pencolor("")
  w.goto(-287.5, 287.5)  #set player position

  turtle.tracer(True)  #player movement not instantaneous


def cleanup_quiz_screen():
  # Clean up the quiz screen
  quiz_screen.hideturtle()
  t_text.hideturtle()
  q1.hideturtle()
  ansA.hideturtle()
  ansB.hideturtle()
  ansC.hideturtle()
  ansD.hideturtle()
  q1.hideturtle()
  correct1.hideturtle()
  t_text.clear()
  g1.hideturtle()
  # Call the game function to display the main screen with the maze


def correct(x, y):
  global correct1
  correct1 = turtle.Turtle()
  correct1.shape("correct.gif")
  turtle.ontimer(cleanup_quiz_screen, 2000)


def incorrect(x, y):
  global timesIncorrect
  timesIncorrect = timesIncorrect + 1
  if (timesIncorrect >= 5):
    game_over()
  incorrect = turtle.Turtle()
  incorrect.shape("incorrect.gif")

  def hide_turtle():
    incorrect.hideturtle()

  # Show the turtle
  incorrect.showturtle()

  # Schedule the hide_turtle function to be called after 2 seconds (2000 milliseconds)
  turtle.ontimer(hide_turtle, 2000)


s.listen()
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(right, "Right")
s.onkeypress(left, "Left")
t1.onclick(game)

turtle.listen()
turtle.mainloop()



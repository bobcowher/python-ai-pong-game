# Code originally taken from https://data-flair.training/blogs/create-pong-game-using-python-project/

import turtle

# Creating the screen with name and size
screen = turtle.Screen()
screen.title("DataFlair Pong game")
screen.setup(width=1000 , height=600)

# Creating the left paddle
paddle1 = turtle.Turtle()
#Setting its speed as zero, it moves only when key is pressed
paddle1.speed(0)
#Setting shape, color, and size
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=6, stretch_len=2)
paddle1.penup()
#The paddle is left-centered initially
paddle1.goto(-400, 0)
# Creating the right paddle
paddle2 = turtle.Turtle()
#Setting its speed as zero, it moves only when key is pressed
paddle2.speed(0)
#Setting shape, color, and size
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=6, stretch_len=2)
paddle2.penup()
#The paddle is right-centered initially
paddle2.goto(400, 0)

# Ball of circle shape
ball = turtle.Turtle()
#Setting the speed of ball to 0, it moves based on the dx and dy values
ball.speed(0)
#Setting shape, color, and size
ball.shape("circle")
ball.color("green")
ball.penup()

#Ball starts from the centre of the screen
ball.goto(0, 0)

#Setting dx and dy that decide the speed of the ball
ball.dx = 2
ball.dy = -2

# Initializing the score of the two players
player1 = 0
player2 = 0
# Displaying the score
score = turtle.Turtle()
score.speed(0)
score.penup()
#Hiding the turtle to show text
score.hideturtle()
#Locating the scoreboard on top of the screen
score.goto(0, 260)
#Showing the score
score.write("Player1 : 0 Player2: 0", align="center", font=("Courier", 20, "bold"))

# Function to move the left paddle up
def movePad1Up():
     y = paddle1.ycor() #Getting the current y-coordinated of the left paddle
     y += 15
     paddle1.sety(y) #Updating the y-coordinated of the paddle
# Function to move the left paddle down
def movePad1Down():
    y = paddle1.ycor()#Getting the current y-coordinated of the left paddle
    y -= 15
    paddle1.sety(y)#Updating the y-coordinated of the paddle
# Function to move the right paddle up
def movePad2Up():
    y = paddle2.ycor()#Getting the current y-coordinated of the right paddle
    y += 15
    paddle2.sety(y)#Updating the y-coordinated of the paddle
# Function to move the right paddle down
def movePad2Down():
   y = paddle2.ycor()#Getting the current y-coordinated of the right paddle
   y -= 15
   paddle2.sety(y)#Updating the y-coordinated of the paddle
# Matching the Keyboard buttons to the above functions=
screen.listen()
screen.onkeypress(movePad1Up, "Left")
screen.onkeypress(movePad1Down, "Right")
screen.onkeypress(movePad2Up, "Up")
screen.onkeypress(movePad2Down, "Down")

#The main game
while True:
  #Updating the screen every time with the new changes
  screen.update()
  #Moving the ball by updating the coordinates
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)
  # Checking if ball hits the top of the screen
  if ball.ycor() > 280:
   ball.sety(280)
   ball.dy *= -1 #Bouncing the ball
  # Checking if ball hits the bottom of the screen
  if ball.ycor() < -280:
   ball.sety(-280)
   ball.dy *= -1#Bouncing the ball
  #Checking if the ball hits the left or right walls, the player missed the hit
  if ball.xcor() > 480 or ball.xcor() < -480:
   if(ball.xcor() <-480):
    player2 += 1 #Increasing the score of right player if left player missed
   else:
    player1 += 1 #Increasing the score of left player if right player missed
   #Starting ball again from center towards the opposite direction
   ball.goto(0, 0)
   ball.dx *= -1
   ball.dy *= -1
  #Updating score in the scoreboard
  score.clear()
  score.write("Player1 : {} Player2: {}".format(player1, player2), align="center", font=("Courier", 20, "bold"))
  #Checking if the left player hit the ball
  if (ball.xcor() < -360 and ball.xcor() > -370) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
   #Increasing score of left player and updating score board
   player1 += 1
   score.clear()
   score.write("Player A: {} Player B: {}".format(player1, player2), align="center", font=("Courier", 20, "bold"))
   ball.setx(-360)
  #Increasing speed of the ball with the limit 7
  if(ball.dy>0 and ball.dy<5): #If dy is positive increasing dy
    ball.dy+=0.5
  elif(ball.dy<0 and ball.dy>-5): #else if dy is negative decreasing dy
    ball.dy-=0.5
  if(ball.dx>0 and ball.dx<5):#If dx is positive increasing dx
    ball.dx+=0.5
  elif(ball.dx<0 and ball.dx>-5): #else if dx is negative decreasing dx
    ball.dx-=0.5

  #Changing the direction of ball towards the right player
  ball.dx *=-1

  #Checking if the right player hit the ball
  if (ball.xcor() > 360 and ball.xcor() < 370) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
      #Increasing score of right player and updating scoreboard
      player2 += 1
      score.clear()
      score.write("Player A: {} Player B: {}".format(player1, player2), align="center", font=("Courier", 20, "bold"))
      ball.setx(360)

  #Increasing speed of the ball with the limit 7
  if(ball.dy>0 and ball.dy<7):#If dy is positive increasing dy
    ball.dy+=1
  elif(ball.dy<0 and ball.dy>-7):#else if dy is negative decreasing dy
   ball.dy-=1
  if(ball.dx>0 and ball.dx<7):#If dx is positive increasing dx
   ball.dx+=1
  elif(ball.dx<0 and ball.dx>-7): #else if dx is negative decreasing dx
   ball.dx-=1
  #Changing the direction of ball towards the left player
   ball.dx*=-1
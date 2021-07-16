# def addnumbers (number1, number2):
#  output = int(number1) + int(number2)
#  return int(output)

# number1 = input("first number here:")
# number2 = input("second number here:")

# print(addnumbers(number1, number2))


# def addnumbers (number1 , number2):
#   output = int(number1) - int(number2)
#   return int(output)


# number1 = input("first number here:")
# number2= input("second number here:")

# print(addnumbers(number1, number2))


# change the turtles shape
# change the  drawing window dimesions(unit of measurments: pixels)
# change drawing pen size
#change the shape of the turtle
#change the background color
# event: something happening
# even (programming): code that is run when something happens on the computer



# window = turtle.Screen(500, 500, -1000)# width, height, startx
# # change background color
# window.bgcolor("blue")

# turtle = turtle.Turtle()
# turtle.pensize(5)
# turtle.forward(100)
# # print("the height of the window is: " + str(window.window_height()))
# # print("the height of the window is: " + str(window.window_width())
# # change color of turtle
# turtle.color("orange")



# #change of the shape of the turtle

# turtle.shape("turtle")
#arrow
#square
#turtle
#triangle
#circle
#classic

#practice turtle events 
# create a turtle program that has a customized background color draw any shape to screen
import turtle



window = turtle.Screen()
window.setup(500,500)

turtle = turtle.Turtle()



def drawcircle():
  turtle.circle(100)

x = 0
while x < 26:
  turtle.speed(15)
  turtle.circle(100)
  turtle.right(50)
  x += 1
  
#incrementing a variable
# x = x + 1 # x += 1 
#decremetinga variable


x = 0
while x < 36:
 turtle.forward(50)
 turtle.left(50)
 turtle.left(100)
 x += 1









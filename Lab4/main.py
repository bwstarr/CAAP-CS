# Branson Starr
# Assignemnt 4
# 8-4-20019

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
turtle.screensize(200, 200, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#000000")
myPen.speed(10)
# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
#turtle.delay(100)

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
def goto_origin(myPen):
	myPen.home()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
	# Can also be done with a for loop - Can you rewrite thise function as such?
	myPen.begin_fill()
	
	for i in range(4):
		myPen.forward(intDim)
		myPen.left(90)
	myPen.end_fill()
	# 90 deg.
# Here is an example of how to draw a box using the box function      
# Comment these two lines out when you draw your own images

 
# Challenge functions (2 bonus pts each) 
# def save_image(): # saves the screen to an image/vector file
# You have a function for boxes, can you make functions for circles and triangles?
# def circle(intRadius):
# def triangle(intLength): #This can be an equilateral triangle, or not


# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the 
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):
	pic = open(path, "r")
	data = pic.read().splitlines()
	colors = data[0].split(",")
	data = data[1:]




	grid=[]
	for line in data:
		grid.append(line.split(","))
	print(colors)
	print(grid)
	return colors, grid



# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
	turtle.tracer(50)
	for line in pixels:
		for pos in line:
			myPen.color(pallet[int(pos)])
			box(boxSize)
			myPen.penup()
			myPen.setheading(0)
			myPen.forward(boxSize)
			myPen.pendown()
		myPen.setheading(270)
		myPen.penup()
		myPen.forward(boxSize)
		myPen.setheading(180)
		myPen.forward(len(line)*boxSize)
		myPen.setheading(0)
		myPen.pendown()
choice = ""
while choice != ":q":
	print("Hello! Which Image do you desire? (type ':q' to quit and exit out of image to select another")
	print("TRIANGLEART | GROWTH | banana | GHOST | mario | SHROOM | ALIENS")
	name = str(input("Enter Here: "))
	col_tst, gd_tst = load_art('art/' + name + '.txt')
	draw(col_tst, gd_tst)
	
turtle.done()
# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask the if they would like to draw a different piece until they quit the program.
if __name__ == '__main__':
	# sample for loading art and calling draw
	pallet_1, pixels_1 = load_art('art/banana.txt')
	draw(pallet_1, pixels_1)
	# You need this to prevent the window from closing after drawing
	turtle.done()
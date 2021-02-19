# January 11 to February 18, 2021
# Kenn Lui <luik3@student.douglascollege.ca>
# Assignment One
# Version 4 / Procedural with Windows and Doors
# Dream House / A flowchart accompanies this program
# which describes the overall schematic / Screenshots
# accompany this program to illustrate the program output

import turtle

        # colour, height, title and reset angle settings

title = "Dream House"
message = "Make Yourself at Home - " + title
height = turtle.numinput(
    'Welcome to Dream House',
    'Please enter the height of your display window (min 100 and max 625)',
    minval=100,
    maxval=625
    )
wNum = int(turtle.numinput(
    'Customize Your Dream House',
    'How many windows will your house have? (min 0 and max 4)',
    minval=0,
    maxval=4
    ))
turtle.color("black")
standardAngle = -90         # the standard angle points the turtle down
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(0.0000035*(height**2))

        # establish a build queue

"""
Comment -- for additional details please see accompanying
flowchart; note that the queue contains a list of strings
that match functions that will be called sequentially
"""

# BACKGROUND AND WELCOME

queue = []                  # wipe the queue just in case
queue = ["p100"]            # draw red frame
if height > 300:
    queue.append("p200")    # add a title if there is space

# HOUSE - LEFT SIDE UNDER THE ROOF

queue.append("p300")        # build plain left wall 12 rows
if wNum == 1 or wNum == 2:
    queue.append("p410")    # add a single left window
elif wNum == 3 or wNum == 4:
    queue.append("p420")    # add two left windows
else:
    print("no left windows added")

# HOUSE - RIGHT SIDE UNDER THE ROOF

queue.append("p500")        # add plain right wall 12 rows
if wNum == 2 or wNum == 3:
    queue.append("p610")    # add a single right window
elif wNum == 4:
    queue.append("p620")    # add two right windows
else:
    print("no right windows added")
queue.append("p700")        # add a door

# ROOF

queue.append("p800")        # build the roof

        # establish basic parameters

#def calculateTitleX(title):
        # perform calculations to centre a greeting at the top of the GUI
        # x-coordinate
#    titleLength = 2 * len(message)
#    x_title = -0.5 * titleLength
#    return x_title
#def calculateTitleY(height):
        # perform calculations to centre a title at the top of the GUI
        # y-coordinate
#    y_title = calculateY(height) - 50
#    return y_title
def calculateWidth(height):
        # calculate width of workspace that is framed by red frame
    width = height * 1.0833
    return width
def calculateX(height):
        # calculate x_value of workspace or maximum x coordinate
    width = calculateWidth(height)
    x_value = width / 2
    return x_value
def calculateY(height):
        # calculate y_value of workspace or maximum y coordinate
    y_value = height / 2
    return y_value

        # establish side, span, window and door dimensions

def side(height, scale):
    "calculate the distance of a 'side' path along the vertical side of a diamond or brick"
    oneSide = (height * 0.3) / scale
    return oneSide
def span(height, scale):
    "calculate the distance of a 'span' path along the diagonal edge of a brick"
    oneSide = side(height, scale)
    oneSpan = oneSide * 1.14
    return oneSpan
def windowSide(height):
    "calculate the distance of a path along the vertical edge of a regular window"
    oneSide = side(height, 14)
    wSide = oneSide * 6
    return wSide
def windowSpan(height):
    "calculate the distance of a path along the diagonal edge of a regular window"
    oneSpan = span(height, 14)
    wSpan = oneSpan * 2.5
    return wSpan
def smallWindowSide(height):
    "calculate the distance of a path along the vertical edge of a small window"
    wSide = windowSide(height)
    swSide = wSide * 0.5
    return swSide
def smallWindowSpan(height):
    "calculate the distance of a path along the diagonal edge of a small window"
    wSpan = windowSpan(height)
    swSpan = wSpan * 0.4
    return swSpan
def doorSide(height):
    "calculate the distance of a path along the vertical edge of the door"
    oneSide = side(height, 14)
    dSide = oneSide * 10
    return dSide
def doorSpan(height):
    "calculate the distance of a path along the diagonal edge of the door"
    oneSpan = span(height, 14)
    dSpan = oneSpan * 5.4
    return dSpan

        # basic function to read from queue
        # note: the build queue is a list of strings

def readFromQueue(num):
    "takes index as input and returns build queue item at index"
    return queue[num]

        # functions to initialize and navigate the turtle

def initialize():
    "reset the turtle to face down and go to one side above the house bottom corner"
    turtle.setheading(standardAngle)
    turtle.goto(0, 0)
    turtle.penup()
    turtle.forward(2 * side(height, 2))
#def left(pix):
#    "move left a particular number of pixels"
#    turtle.setheading(standardAngle)
#    turtle.left(70)
#    turtle.penup()
#    turtle.forward(-pix)
#    turtle.right(70)
#    turtle.pendown()
#def right(pix):
#    "move right a particular number of pixels"
#    turtle.setheading(standardAngle)
#    turtle.right(70)
#    turtle.penup()
#    turtle.forward(-pix)
#    turtle.left(70)
#    turtle.pendown()
def offsetLeft(num):
    "move left half span of standard brick"
    halfSide = side(height, 28)
    turtle.left(70)
    turtle.penup()
    turtle.forward(-num * halfSide)
    turtle.right(70)
    turtle.pendown()
def offsetRight(num):
    "move right half span of standard brick"
    halfSide = side(height, 28)
    turtle.right(70)
    turtle.penup()
    turtle.forward(-num * halfSide)
    turtle.left(70)
    turtle.pendown()
def climb(num):
    "move up one/ten sides of standard brick"
    turtle.penup()
    turtle.forward(-num * side(height, 14))
    turtle.pendown()

        # functions to draw basic elements with the turtle

def procedureB01(height):
    "B01 - standard left brick"
    oneSide = side(height, 14)
    oneSpan = span(height, 14)
    turtle.pendown()
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.forward(oneSide)
    turtle.left(70)
    turtle.forward(-oneSpan)
    turtle.right(70)
    turtle.forward(-oneSide)
    turtle.left(70)
    turtle.forward(oneSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-oneSpan)
    turtle.right(70)

def procedureB02(height):
    "B02 - standard right brick"
    oneSide = side(height, 14)
    oneSpan = span(height, 14)
    turtle.pendown()
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.forward(oneSide)
    turtle.right(70)
    turtle.forward(-oneSpan)
    turtle.left(70)
    turtle.forward(-oneSide)
    turtle.right(70)
    turtle.forward(oneSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-oneSpan)
    turtle.left(70)

def procedureB03(height):
    "B03 - short left brick"
    oneSide = side(height, 14)
    oneSpan = span(height, 14)
    turtle.pendown()
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.forward(oneSide)
    turtle.left(70)
    turtle.forward(-0.5 * oneSpan)
    turtle.right(70)
    turtle.forward(-oneSide)
    turtle.left(70)
    turtle.forward(0.5 * oneSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-0.5 * oneSpan)
    turtle.right(70)

def procedureB04(height):
    "B04 - short right brick"
    oneSide = side(height, 14)
    oneSpan = span(height, 14)
    turtle.pendown()
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.forward(oneSide)
    turtle.right(70)
    turtle.forward(-0.5 * oneSpan)
    turtle.left(70)
    turtle.forward(-oneSide)
    turtle.right(70)
    turtle.forward(0.5 * oneSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-0.5 * oneSpan)
    turtle.left(70)

def procedureB05(height):
    "B05 - corner left brick"
    oneSide = side(height, 14)
    oneSpan = span(height, 14)
    turtle.pendown()
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.right(70)
    turtle.forward(-0.5 * oneSpan)
    turtle.left(70)
    turtle.forward(oneSide)
    turtle.right(70)
    turtle.forward(0.5 * oneSpan)
    turtle.left(140)
    turtle.forward(-oneSpan)
    turtle.right(70)
    turtle.forward(-oneSide)
    turtle.left(70)
    turtle.forward(oneSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-oneSpan)
    turtle.right(70)

def procedureB06(height):
    "B06 - corner right brick"
    oneSide = side(height, 14)
    oneSpan = span(height, 14)
    turtle.pendown()
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.left(70)
    turtle.forward(-0.5 * oneSpan)
    turtle.right(70)
    turtle.forward(oneSide)
    turtle.left(70)
    turtle.forward(0.5 * oneSpan)
    turtle.right(140)
    turtle.forward(-oneSpan)
    turtle.left(70)
    turtle.forward(-oneSide)
    turtle.right(70)
    turtle.forward(oneSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-oneSpan)
    turtle.left(70)

def procedureB07(height):
    "B07 - left regular window"
    wSide = windowSide(height)
    wSpan = windowSpan(height)
    turtle.pendown()
    turtle.color("white", "light blue")
    turtle.begin_fill()
    turtle.forward(wSide)
    turtle.left(70)
    turtle.forward(-wSpan)
    turtle.right(70)
    turtle.forward(-wSide)
    turtle.left(70)
    turtle.forward(wSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-wSpan)
    turtle.right(70)

def procedureB08(height):
    "B08 - right small window"
    wSide = smallWindowSide(height)
    wSpan = smallWindowSpan(height)
    turtle.pendown()
    turtle.color("white", "light blue")
    turtle.begin_fill()
    turtle.forward(wSide)
    turtle.right(70)
    turtle.forward(-wSpan)
    turtle.left(70)
    turtle.forward(-wSide)
    turtle.right(70)
    turtle.forward(wSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-wSpan)
    turtle.left(70)

def procedureB09(height):
    "B09 - right door frame"
    dSide = doorSide(height)
    dSpan = doorSpan(height)
    turtle.pendown()
    turtle.color("white", "white")
    turtle.begin_fill()
    turtle.forward(dSide)
    turtle.right(70)
    turtle.forward(-dSpan)
    turtle.left(70)
    turtle.forward(-dSide)
    turtle.right(70)
    turtle.forward(dSpan)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-dSpan)
    turtle.left(70)

def procedureB10(height):
    "B10 - right door"
    dSide = doorSide(height)
    dSpan = doorSpan(height)
    turtle.pendown()
    turtle.color("white", "burlywood")
    turtle.begin_fill()
    turtle.forward(dSide*0.94)
    turtle.right(70)
    turtle.forward(-dSpan*0.84)
    turtle.left(70)
    turtle.forward(-dSide*0.94)
    turtle.right(70)
    turtle.forward(dSpan*0.84)
    turtle.end_fill()
    turtle.penup()

        # functions to draw rows of bricks

def procedureB11(height):
    "B11 - even left row of 14 bricks"
    turtle.pendown()
    turtle.color("white", "red")
    procedureB05(height)
    for count in range(14):
        procedureB01(height)

def procedureB12(height):
    "B12 - odd right row of 14 bricks"
    offsetRight(1)
    turtle.pendown()
    turtle.color("white", "red")
    for count in range(14):
        procedureB02(height)
    procedureB04(height)

def procedureB13(height):
    "B13 - odd left row of 14 bricks"
    offsetLeft(1)
    turtle.pendown()
    turtle.color("white", "red")
    for count in range(14):
        procedureB01(height)
    procedureB03(height)

def procedureB14(height):
    "B14 - even right row of 14 bricks"
    turtle.pendown()
    turtle.color("white", "red")
    procedureB06(height)
    for count in range(14):
        procedureB02(height)

def procedureB15(height):
    "B15 - 12 left rows of 14 bricks"
    c = 0
    for count in range(6):
        climb(c)
        procedureB11(height)
        initialize()
        c += 1
        climb(c)
        procedureB13(height)
        initialize()
        c += 1

def procedureB16(height):
    "B16 - 12 right rows of 14 bricks"
    c = 0
    for count in range(6):
        climb(c)
        procedureB12(height)
        initialize()
        c += 1
        climb(c)
        procedureB14(height)
        initialize()
        c += 1

        # functions to draw windows

def procedureB31(height):
    "B31 - draw single window on left wall"
    turtle.penup()
    offsetLeft(7)
    climb(7.5)
    procedureB07(height)
    initialize()
    turtle.penup()

def procedureB32(height):
    "B32 - draw two windows on left wall"
    turtle.penup()
    offsetLeft(7)
    climb(7.5)
    procedureB07(height)
    initialize()
    turtle.penup()
    offsetLeft(23)
    climb(7.5)
    procedureB07(height)
    turtle.penup()

def procedureB33(height):
    "B33 - draw window on right side of the door"
    turtle.penup()
    offsetRight(27)
    climb(6)
    procedureB08(height)
    initialize()
    turtle.penup()

def procedureB34(height):
    "B34 - draw windows on either side of the door"
    turtle.penup()
    offsetRight(5)
    climb(6)
    procedureB08(height)
    initialize()
    turtle.penup()
    offsetRight(27)
    climb(6)
    procedureB08(height)
    turtle.penup()

        # functions to add door and door elements on right wall

def procedureB41(height):
    "B41 - add a door frame"
    turtle.penup()
    offsetRight(11)
    climb(9)
    turtle.pendown()
    procedureB09(height)

def procedureB42(height):
    "B42 - add a door"
    turtle.penup()
    offsetRight(12)
    climb(8.33)
    turtle.pendown()
    procedureB10(height)
    turtle.penup()

def procedureB43(height):
    "B43 - add a doorknob"
    turtle.penup()
    offsetRight(20.6)
    climb(3.5)
    turtle.pendown()
    turtle.color("black")
    turtle.dot()
    turtle.penup()

        # functions to draw build queue items

def procedure100(height):
    "100 - draw a red border"
    maxTopLeftX = calculateX(height)
    maxTopLeftY = calculateY(height)
    turtle.title(title)
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(-maxTopLeftX, maxTopLeftY)
    turtle.pendown()
    width = calculateWidth(height)
    for count in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.penup()
    initialize()

def procedure200(title, height):
    "200 - write a welcome message centred at the top of the drawing"
    turtle.pencolor("black")
#    x_valueTitle = calculateTitleX(title)
#    y_valueTitle = calculateTitleY(height)
    position = .7*calculateY(height)
    fontSize = int(height/30)
    turtle.goto(0,position)
    turtle.pendown()
    turtle.write(message, align="center", font=("Helvetica", fontSize, "normal"))
    turtle.penup()
    initialize()

def procedure300():
    "300 - build a plain left wall"
    procedureB15(height)
    initialize()

def procedure410():
    "410 - add a single window to left wall"
    procedureB31(height)
    initialize()

def procedure420():
    "420 - add two windows to left wall"
    procedureB32(height)
    initialize()

def procedure500():
    "500 - build a plain right wall"
    procedureB16(height)
    initialize()

def procedure610():
    "610 - add a single window to right wall"
    procedureB33(height)
    initialize()

def procedure620():
    "620 - add a single window to right wall"
    procedureB34(height)
    initialize()

def procedure700():
    "700 - add a door to right wall"
    procedureB41(height)
    initialize()
    procedureB42(height)
    initialize()
    procedureB43(height)
    initialize()

def procedure800():
    "800 - build roof"
    turtle.penup()
    oneSide = side(height, 14)
    sideLength = -20 * oneSide
    roofHeight = 11 * oneSide
    climbHeight = 11 * oneSide
    climb(11)
    position = turtle.pos()
    frontCornerY = position[1]
    turtle.pendown()
    turtle.color("black", "slate gray")
    turtle.begin_fill()
    turtle.left(70)
    turtle.forward(sideLength)
    turtle.right(70)
    position = turtle.pos()
    otherCornerX = -position[0]
    otherCornerY = position[1]
    turtle.goto(0, roofHeight)
    turtle.goto(otherCornerX, otherCornerY)
    turtle.goto(0, frontCornerY)
    turtle.goto(0, roofHeight)
    turtle.end_fill()
    turtle.color("black")

        # build the house according to queue instructions

for step in range(len(queue)):
    if readFromQueue(step) == "p100":
        procedure100(height)
    elif readFromQueue(step) == "p200":
        procedure200(title, height)
    elif readFromQueue(step) == "p300":
        procedure300()
    elif readFromQueue(step) == "p410":
        procedure410()
    elif readFromQueue(step) == "p420":
        procedure420()
    elif readFromQueue(step) == "p500":
        procedure500()
    elif readFromQueue(step) == "p610":
        procedure610()
    elif readFromQueue(step) == "p620":
        procedure620()
    elif readFromQueue(step) == "p700":
        procedure700()
    elif readFromQueue(step) == "p800":
        procedure800()
    else:
        print("build code error")

turtle.done()

import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.title("Simple Drawing with Shapes")
screen.bgcolor("white")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed (1 is slow, 10 is fast)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        pen.color('blue')
        pen.forward(side_length)
        pen.right(90)

# Function to draw a circle
def draw_circle(radius):
    pen.color('red')
    pen.circle(radius)
    

# Function to draw an equilateral triangle
def draw_triangle(side_length):
    for _ in range(3):
        pen.color('green')
        pen.forward(side_length)
        pen.left(120)

# Draw shapes
pen.penup()
pen.goto(-50, 50)  # Position the Turtle
pen.pendown()

# You can change the shape, size, and color of the drawing here
draw_square(100)
draw_circle(50)
draw_triangle(100)

# Close the Turtle Graphics window on click
screen.exitonclick()

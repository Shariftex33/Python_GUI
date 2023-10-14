import turtle
import math

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
spiro = turtle.Turtle()
spiro.shape("turtle")
spiro.color("Red")
spiro.speed(0)  # Adjust the speed for faster or slower drawing

# Function to draw a Spirograph
def draw_spirograph(R, r, d):
    # Calculate the initial position
    x = (R - r) * math.cos(0) + d * math.cos(((R - r) / r) * 0)
    y = (R - r) * math.sin(0) - d * math.sin(((R - r) / r) * 0)
    spiro.penup()
    spiro.goto(x, y)
    spiro.pendown()
    theta = 0

    while theta <= 360:
        # Parametric equations for a Spirograph
        x = (R - r) * math.cos(math.radians(theta)) + d * math.cos(((R - r) / r) * math.radians(theta))
        y = (R - r) * math.sin(math.radians(theta)) - d * math.sin(((R - r) / r) * math.radians(theta))
        spiro.goto(x, y)
        theta += 1

# Customize your Spirograph here
R = 100  # Radius of the large circle
r = 20   # Radius of the small circle
d = 50   # Distance from the center of the small circle to the pen

# Draw the Spirograph
draw_spirograph(R, r, d)

# Close the drawing window when clicked
screen.exitonclick()

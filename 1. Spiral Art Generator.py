import turtle

# Set up the Turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a Turtle object
artist = turtle.Turtle()
artist.shape("turtle")
artist.color("blue")
artist.speed(10)  # Adjust the speed as needed (1-10)

# Function to draw a spiral
def draw_spiral(sides, length, angle):
    for _ in range(sides):
        artist.forward(length)
        artist.right(angle)

# Number of sides in the spiral (change this to vary the pattern)
num_sides = 36

# Length of each side (change this for a larger or smaller spiral)
side_length = 300

# Angle by which the Turtle turns (change this to alter the spiral shape)
turn_angle = 170

# Drawing the spiral
draw_spiral(num_sides, side_length, turn_angle)

# Close the Turtle graphics window on click
window.exitonclick()

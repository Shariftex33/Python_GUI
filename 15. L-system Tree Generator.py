import turtle

# Set up the Turtle screen
window = turtle.Screen()
window.bgcolor("white")
window.title("L-system Tree Generator")

# Create a Turtle object
tree = turtle.Turtle()
tree.speed(0)  # Set the drawing speed (0 is the fastest)
tree.color('green')

# Define the L-system rules
rules = {
    "F": "FF+[+F-F-F]-[-F+F+F]",
    "+": "+",
    "-": "-"
}

# Initial axiom
axiom = "F"

# Generate the L-system string
iterations = 7  # Change this value for different tree sizes
lsystem = axiom
for _ in range(iterations):
    lsystem = "".join([rules.get(c, c) for c in lsystem])

# Length of each forward step
step_length = 20

# Angle for left and right turns (in degrees)
angle = 22.5

# Stack to store position and heading
stack = []

# Drawing the L-system
for char in lsystem:
    if char == "F":
        tree.backward(step_length)
    elif char == "+":
        tree.right(angle)
    elif char == "-":
        tree.left(angle)
    elif char == "[":
        stack.append((tree.pos(), tree.heading()))
    elif char == "]":
        position, heading = stack.pop()
        tree.penup()
        tree.goto(position)
        tree.setheading(heading)
        tree.pendown()

# Close the Turtle graphics window on click
window.exitonclick()

import turtle as t

# Function to draw a single letter
def draw_letter(letter, pen_color):
    t.pendown()
    t.pencolor(pen_color)
    t.write(letter, font=("Arial", 20, "normal"))
    t.penup()
    t.forward(30)  # Adjust the spacing between letters

# Set up the Turtle screen
t.bgcolor("black")  # Background color
t.speed(1)  # Drawing speed (1 is slow, 10 is fast)
t.penup()
t.goto(-100, 0)  # Starting position

# Your name or word to animate
name = "Python"

# Customization: Change the colors as desired
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Animation loop
for color in colors:
    
    for letter in name:
        draw_letter(letter, color)
    
    t.goto(-100, -30)  # Return to the starting position
    t.goto(-100, -30)
    #t.clear()

# Close the Turtle graphics window on click
t.exitonclick()

import turtle as t

# Function to draw a Koch snowflake of a given order and length
def koch_snowflake(order, length):
    if order == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(order - 1, length)
        t.left(60)
        koch_snowflake(order - 1, length)
        t.right(120)
        koch_snowflake(order - 1, length)
        t.left(60)
        koch_snowflake(order - 1, length)

# Initialize the Turtle
t.speed(0)  # Set the drawing speed (0 is the fastest)
t.penup()
t.goto(-150, 90)  # Set starting position
t.pendown()

# Customize the snowflake by changing these values
order = 4  # The order of the snowflake (higher values for more complexity)
length = 300  # The length of each side

# Draw the snowflake
for _ in range(3):
    t.color('Red')
    koch_snowflake(order, length)
    t.right(120)
    

# Close the drawing window on click
t.exitonclick()

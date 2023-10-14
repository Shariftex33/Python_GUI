# Import necessary libraries
import turtle
from datetime import datetime

# Set up the Turtle screen
wn = turtle.Screen()
wn.title("Animated Clock")
wn.bgcolor("White")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create the clock face
clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.color("black")
clock_face.penup()
clock_face.goto(0, -210)
clock_face.pendown()
clock_face.circle(210)

# Create clock hands
hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.shape("arrow")
hour_hand.color("blue")
hour_hand.shapesize(stretch_wid=0.05, stretch_len=7)

minute_hand = turtle.Turtle()
minute_hand.speed(0)
minute_hand.shape("arrow")
minute_hand.color("green")
minute_hand.shapesize(stretch_wid=0.05, stretch_len=13)

second_hand = turtle.Turtle()
second_hand.speed(0)
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(stretch_wid=0.02, stretch_len=15)

# Update the clock
def update_clock():
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12

    # Move the clock hands
    second_angle = -90 - second * 6
    minute_angle = -90 + (minute + second / 60) * 6
    hour_angle = -90 + (hour + minute / 60) * 30

    second_hand.setheading(second_angle)
    minute_hand.setheading(minute_angle)
    hour_hand.setheading(hour_angle)

    wn.update()
    wn.ontimer(update_clock, 1000)

update_clock()

# Close the window on click
wn.exitonclick()

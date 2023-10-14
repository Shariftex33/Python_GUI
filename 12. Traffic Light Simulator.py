import turtle
import time

# Function to draw a single traffic light
def draw_traffic_light(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

# Set up the Turtle Screen
screen = turtle.Screen()
screen.title("Traffic Light Simulator")

# Initial state of the traffic light
state = "red"

while True:
    if state == "red":
        draw_traffic_light("red")
        time.sleep(2)  # Red light for 2 seconds
        state = "green"
        turtle.forward(80)
        #turtle.clear()
    elif state == "green":
        draw_traffic_light("green")
        time.sleep(2)  # Green light for 2 seconds
        state = "yellow"
        turtle.forward(80)
        #turtle.clear()
    else:
        draw_traffic_light("yellow")
        time.sleep(1)  # Yellow light for 1 second
        state = "red"
        turtle.clear()

turtle.done()

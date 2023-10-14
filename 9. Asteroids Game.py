import turtle
import random
import math

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Asteroids Game")

# Create the player's spaceship
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)

# Set the player's speed
playerspeed = 15

# Create the asteroids
asteroids = []
num_asteroids = 5

for _ in range(num_asteroids):
    asteroid = turtle.Turtle()
    asteroid.color("red")
    asteroid.shape("circle")
    asteroid.penup()
    asteroid.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    asteroid.setposition(x, y)
    asteroids.append(asteroid)

# Set the asteroid speed
asteroid_speed = 2

# Define the player's movement functions
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -250:
        x = -250
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 250:
        x = 250
    player.setx(x)

# Set up keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
while True:
    for asteroid in asteroids:
        # Move the asteroid
        y = asteroid.ycor()
        y -= asteroid_speed
        asteroid.sety(y)

        # Check for collision with the player
        if player.distance(asteroid) < 20:
            player.hideturtle()
            asteroid.hideturtle()
            print("Game Over")
            wn.bye()
    
    # Check for win condition
    if all(asteroid.ycor() < -250 for asteroid in asteroids):
        print("You Win!")
        wn.bye()

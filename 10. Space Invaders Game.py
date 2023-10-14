import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Simple Space Invaders")
wn.bgcolor("blue")
wn.setup(width=600, height=600)

# Create the player
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("green")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Create the enemies
enemies = []

for _ in range(10):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
while True:
    for enemy in enemies:
        y = enemy.ycor()
        y -= 2
        enemy.sety(y)

        # Check for collision with player
        if player.distance(enemy) < 20:
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            wn.bye()

        # Respawn the enemy
        if y < -300:
            x = random.randint(-290, 290)
            y = random.randint(100, 250)
            enemy.goto(x, y)

wn.mainloop()

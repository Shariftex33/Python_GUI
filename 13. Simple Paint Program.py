import turtle as t

# Set up the screen
t.bgcolor("white")
t.title("Simple Paint Program")
t.setup(width=800, height=600)

# Define functions for drawing shapes
def draw_line(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('green')
    t.circle(60)

def draw_square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('red')
    for _ in range(4):
        t.forward(100)
        t.right(90)

def clear_screen():
    t.clear()

# Set up event handlers
t.onscreenclick(draw_line)
t.onkeypress(lambda: draw_circle(t.xcor(), t.ycor()), "c")
t.onkeypress(lambda: draw_square(t.xcor(), t.ycor()), "s")
t.onkeypress(clear_screen, "x")

# Listen for events
t.listen()
t.mainloop()

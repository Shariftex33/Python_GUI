import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        # Draw the main branch
        t.forward(branch_length)

        # Right subtree (recursive call)
        t.right(20)
        draw_branch(branch_length - 15, t)

        # Left subtree (recursive call)
        t.left(40)
        draw_branch(branch_length - 15, t)

        # Return to the original position
        t.right(20)
        t.backward(branch_length)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    fractal_tree = turtle.Turtle()
    fractal_tree.speed(0)  # Set the drawing speed (0 is the fastest)
    fractal_tree.color("green")
    
    fractal_tree.left(90)  # Start by pointing the turtle upward
    fractal_tree.penup()
    fractal_tree.setpos(0, -200)  # Set the starting position
    fractal_tree.pendown()
    
    draw_branch(100, fractal_tree)  # Change the first argument for different tree sizes
    
    window.exitonclick()

if __name__ == "__main__":
    main()

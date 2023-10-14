import turtle as t

# Create a 2D maze as a list of lists
maze = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

# Function to draw a square at (x, y)
def draw_square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(40)
        t.right(90)
    t.end_fill()

# Function to draw the maze
def draw_maze():
    t.speed(0)
    t.color("black")
    t.penup()
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw_square(x * 40, -y * 40)

# Function to solve the maze using recursion
def solve_maze(x, y):
    if 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] == 1:
        maze[y][x] = 2  # Mark the current cell as visited
        if x == len(maze[0]) - 1 and y == 0:
            t.color("green")
            draw_square(x * 40, -y * 40)
            t.color("black")
            return True  # Maze solved
        if (
            solve_maze(x + 1, y)
            or solve_maze(x - 1, y)
            or solve_maze(x, y + 1)
            or solve_maze(x, y - 1)
        ):
            t.color("green")
            draw_square(x * 40, -y * 40)
            t.color("black")
            return True  # Maze solved
    return False

# Main function
if __name__ == "__main__":
    draw_maze()
    t.speed(1)
    t.delay(0)
    if not solve_maze(0, len(maze) - 1):
        print("No solution found.")
    t.exitonclick()

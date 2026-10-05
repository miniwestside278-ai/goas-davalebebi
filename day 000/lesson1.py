import turtle


def draw_rectangle(t, width, height, fill_color):
    """Utility function to draw a filled rectangle."""
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        
    t.end_fill()


def draw_triangle(t, side_length, fill_color):
    """Utility function to draw a filled equilateral triangle."""
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()


def main():
    screen = turtle.Screen()
    screen.title("Colorful House")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)
    t.pensize(2)

    # --- 1. Main House Body (Blue) ---
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    draw_rectangle(t, 200, 150, "blue")

    # --- 2. Roof (Green) ---
    t.penup()
    t.goto(-110, 50)  # Slightly wider than the house for overhang
    t.pendown()
    draw_triangle(t, 220, "green")

    # --- 3. Door (Yellow) ---
    t.penup()
    t.goto(-25, -100)
    t.pendown()
    draw_rectangle(t, 50, 80, "yellow")

    # Door Knob
    t.penup()
    t.goto(15, -60)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    # --- 4. Left Window (Red) ---
    t.penup()
    t.goto(-80, -10)
    t.pendown()
    draw_rectangle(t, 40, 40, "red")

    # --- 5. Right Window (Red) ---
    t.penup()
    t.goto(40, -10)
    t.pendown()
    draw_rectangle(t, 40, 40, "red")

    # Finish drawing
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
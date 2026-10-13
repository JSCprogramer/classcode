import turtle 

t = turtle.Turtle()
t.speed(0)
def draw_spirograph(R, r, d):
    for _ in range(100):
        t.pencolor("black")
        t.circle(R)
        t.pencolor("gray")
        t.circle(r)
        t.left(d)
draw_spirograph(100, 30, 25)
turtle.done()

import turtle

t = turtle.Screen()
t.title("Двигающаяся черепаха")
t.bgcolor("black")
t.setup(400, 400)
t.tracer(0)

krug = turtle.Turtle()
krug.speed(0)
krug.shape("circle")
krug.color("white")
krug.penup()
krug.goto(0, 0)
#krug.dx = 2
#krug.dy = 2


def move_up():
    y = krug.ycor()
    y += 3
    krug.sety(y)

def move_down():
    y = krug.ycor()
    y -= 3
    krug.sety(y)

def move_left():
    x = krug.xcor()
    x -= 3
    krug.setx(x)

def move_right():
    x = krug.xcor()
    x += 3
    krug.setx(x)

t.listen()
t.onkeypress(move_up, "w")
t.onkeypress(move_down, "s")
t.onkeypress(move_left, "a")
t.onkeypress(move_right, "d")

while True:
    t.update()

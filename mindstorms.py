import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    sides = 0
    while sides < 4:
        brad.forward(100)
        brad.right(90)
        sides += 1
    
    window.exitonclick()

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("red")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    window.exitonclick()

def draw_triangle():
    window = turtle.Screen()

    leonard = turtle.Turtle()

    sides = 0
    while sides < 3:
        leonard.forward(100)
        leonard.right(120)
        sides += 1

    window.exitonclick()

draw_square()    
draw_circle()
draw_triangle()

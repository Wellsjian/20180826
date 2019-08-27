import turtle

def draw_size(size):
    for i in range(5):
        turtle.fd(size)
        turtle.right(144)

def main():
    turtle.penup()
    turtle.back(600)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("red")
    size = 50
    turtle.exitonclick()
    while True:
        draw_size(50)
if __name__ == "__main__":
    main()
    # turtle.exitonclick()
from turtle import *
import random

# ///////// Hollow Pentagon /////////
# colors = ['red', 'blue', 'orange', 'green', 'yellow']

# t = Turtle()

# for i in colors:
#     t.color(i)
#     t.forward(100)
#     t.left(72)

# done()


# ///////// Solid Square /////////
# c_pos = [
#     ((100, 100), "red"),
#     ((-100, 100), "blue"),
#     ((-100, -100), "orange"),
#     ((100, -100), "green"),
# ]

# t = Turtle()

# for i in c_pos:
#     t.penup()
#     t.goto(*i[0])
#     t.pendown()
#     t.color(i[1])
#     t.begin_fill()
#     for i in range(4):
#         t.forward(50)
#         t.left(90)
#     t.end_fill()

# done()


# ///////// Shape based on function /////////
# t = Turtle()


# def square() -> None:
#     for i in range(4):
#         t.forward(100)
#         t.left(90)


# def pentagon() -> None:
#     for i in range(5):
#         t.forward(100)
#         t.left(72)


# def triangle() -> None:
#     for i in range(3):
#         t.forward(100)
#         t.left(120)


# ask = input("Enter a shape [square, pentagon, triangle]: ")

# if ask == "square":
#     square()
# elif ask == "pentagon":
#     pentagon()
# elif ask == "triangle":
#     triangle()
# else:
#     print("No shape entered")

# done()


# ///////// Shape based on function /////////
# t = Turtle()

# for i in range(10):
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     radius = random.randint(1, 100)

#     t.penup()
#     t.goto(x, y)
#     t.pendown()

#     t.circle(radius)

# done()


# ///////// 3 Objects in a column with triangle /////////
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.color("red")
t2.color("blue")
t3.color("green")


def triangle(t: Turtle, y: int, x: int=-50) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()


triangle(t1, 100)
triangle(t2, 0)
triangle(t3, -100)

done()


import random
import turtle


def tree(branch_len, t):
    if branch_len > 5:
        xlen = random.randrange(5, 20)
        xdeg = random.randrange(15, 45)
        t.pensize(width=branch_len//3)
        t.forward(branch_len)
        t.color(random.choice(['green','red','yellow']))
        t.right(xdeg)
        t.color(random.choice(['green','red','yellow']))
        tree(branch_len - xlen, t)
        t.left(xdeg*2)
        tree(branch_len - xlen, t)
        t.right(xdeg)
        t.color(random.choice(['green','red','yellow']))
        t.backward(branch_len)
        t.color(random.choice(['green','red','yellow']))

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()

main()

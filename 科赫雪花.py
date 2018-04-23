import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
def main(level):
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    koch(400,level)    # 线条长度600,3阶
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
main(3)


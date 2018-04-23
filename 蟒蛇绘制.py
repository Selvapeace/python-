import turtle
turtle.setup(650,350,0,0)
turtle.penup        # 海龟在飞，轨迹不显示
turtle.fd(-250)   # forward
turtle.pendown
turtle.pensize(25)     # pensize = width
turtle.pencolor('purple')    # 3种方式：颜色名、RGB小数值、RGB元组值
turtle.seth(-40)         # set heading 海龟方向控制（绝对视角）； turtle.left()turtle.right()海龟视角
for i in range(4):
    turtle.circle(40,80)     # 默认圆心在海龟左侧40距离处，走80度
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.down       # 程序运行完毕后不会自动退出


from turtle import*
setup(650,350,0,0)
penup()
fd(-250)
pendown()
pensize(25)
pencolor('purple')
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40 * 2/3)
down()


import turtle as t
t.setup(650,350,0,0)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor('purple')
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40 * 2/3)
t.down()

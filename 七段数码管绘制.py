import turtle as t
import time

def drawgap():
    t.penup()
    t.fd(5)
def drawline(draw):
    drawgap()
    t.pendown() if draw == True else t.penup()
    t.fd(40)
    drawgap()
    t.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawdate(date):
    t.pencolor('red')
    for each in date:      
        if each == '年':
            t.write('年',font = ('Arial',18,'normal'))
            t.pencolor('yellow')
            t.fd(40)
        elif each == '月':
            t.write('月',font = ('Arial',18,'normal'))
            t.pencolor('RosyBrown2')
            t.fd(40)
        elif each == '日':
            t.write('日',font = ('Arial',18,'normal'))
            t.pencolor(95/255,158/255,160/255)
            t.fd(40)
        else:
            drawdigit(eval(each))
def main(time):
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawdate(time)
    t.hideturtle()
    t.done()


time2 = time.strftime('%Y年%m月%d日',time.gmtime())
main(time2)

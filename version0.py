import turtle,time,math,easygui

#画3种线
def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(20)

def drawLongline(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)

def drawSmallline(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(math.sqrt((40**2+80**2))/2)

def NextPic():
    turtle.penup()
    turtle.fd(10)
    drawLongline(False)
    turtle.left(90)
    drawLongline(False)
    turtle.left(90)

#画单个字符
def draw(pic):
# line1
    drawLongline(True) if pic in ['*', 2, 3, 5, 6, 7, 8, 9, 0, 'E', 'A', 'R', 'O', 'T','D','C','I'] else drawLongline(False)
    turtle.left(math.degrees(math.atan(0.5))+90)
# line2
    drawSmallline(True) if pic in ['*', 'Y','M','N'] else drawSmallline(False)
# line3
    drawSmallline(True) if pic in ['*', 'R','N'] else drawSmallline(False)
    turtle.left(180-math.degrees(math.atan(0.5)))
# line4
    drawLongline(True) if pic in ['*', 1, 7, 3, 4, 5, 6, 8, 9, 0, 'A', 'U', 'M', 'O', 'N', 'H', 'D'] else drawLongline(False)
# line5
    drawLongline(True) if pic in ['*', 1, 7, 2, 3, 4, 8, 9, 0, 'A', 'R', 'U', 'M', 'O', 'N', 'H', 'D'] else drawLongline(False)
    turtle.left(180-math.degrees(math.atan(0.5)))
# line6
    drawSmallline(True) if pic in ['*', 0, 1, 'Y', 'M'] else drawSmallline(False)
# line7
    drawSmallline(True) if pic in ['*', 0] else drawSmallline(False)
    turtle.left(math.degrees(math.atan(0.5))+90)
# line8
    drawLongline(True) if pic in ['*', 2, 3, 5, 6, 8, 9, 0, 'E', 'O', 'D','U','C','I'] else drawLongline(False)
    turtle.left(180)
    drawLongline(False)
    turtle.right(90)
# line9
    drawLongline(True) if pic in ['*', 2, 6, 8, 0, 'E', 'A', 'R', 'M', 'O', 'N','H','U','C'] else drawLongline(False)
# line10
    drawLongline(True) if pic in ['*', 4, 5, 6, 8, 9, 0, 'E', 'A', 'R', 'M', 'O', 'N', 'H','U','C'] else drawLongline(False)
    turtle.right(90)
    drawLine(False)
    turtle.right(90)
# line11
    drawLongline(True) if pic in ['*', 'T','D','I'] else drawLongline(False)
# line12
    drawLongline(True) if pic in ['*', 'Y', 'T', 'D','I'] else drawLongline(False)
    turtle.right(90)
    drawLine(False)
    turtle.right(90)
    drawLongline(False)
    turtle.right(90)
# line13
    drawLine(True) if pic in ['*', 2, 4, 5, 6, 8, 9, 'E', 'A', 'R', 'H'] else drawLine(False)
# line14
    drawLine(True) if pic in ['*', 2, 4, 3, 5, 6, 8, 9, 'A', 'R', 'H'] else drawLine(False)
    NextPic()

def drawDate(date,s):
    turtle.pencolor('red')
    for i in date:
        if i == 'S': #S的符号和5一样
            draw(5)
        elif i == '*' or i.isalpha():
            draw(i)
        else:
            draw(int(i))
        if s=='date':
            if i == 'R':
                turtle.pencolor('green')
                turtle.fd(10)
            elif i == 'H':
                turtle.pencolor('blue')
                turtle.fd(10)
#时分秒之间变色
        elif s=='time':
            if i == 'R':
                turtle.pencolor('green')
                turtle.fd(-20)
            elif i == 'E':
                turtle.pencolor('blue')
                turtle.fd(-20)

def main():
    s = easygui.buttonbox('What you want to post?', 'B21032211', ('date', 'time', 'test'))
    turtle.speed(100)#让乌龟动的快一点
    turtle.setup(3000, 500, 50, 50)
    if s=='time':
        while (1):
            
            turtle.goto(-700,10)
            turtle.penup()
            turtle.clear()
            turtle.pensize(5)
            turtle.right(180)
            drawDate(time.strftime('%HHOUR%MMINUTE%SSECOND',time.gmtime()),s)
            time.sleep(1)
            turtle.hideturtle()
            NextPic()
            turtle.penup()
            #turtle.done()
    else :
        turtle.goto(-700,10)
        turtle.penup()
        turtle.clear()
        turtle.pensize(5)
        turtle.right(180)
        if s=='test':
            drawDate('*0123456789YEARMONTHDUIC',s)
        elif s=='date':
            drawDate(time.strftime('%YYEAR%mMONTH%dDAY',time.gmtime()),s)
        time.sleep(1)
        turtle.hideturtle()
        NextPic()
        turtle.penup()
        turtle.done()

main()

'''turtle正方形绘制
使用turtle库，绘制一个正方形。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬

注意：这不是自动评阅题目，仅用于练习，没有评阅。'''

import turtle as t
t.setup(250,250)
t.penup()
t.fd(100)
t.pendown()
t.pensize(10)
t.pencolor('black')
t.goto(100,-100)
t.goto(-100,-100)
t.goto(-100,100)
t.goto(100,100)
t.goto(100,0)
t.done()

'''参考答案：
import turtle as t
t.pensize(2)
for i in range(4):
    t.fd(150)
    t.left(90)'''
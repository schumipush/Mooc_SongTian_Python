'''来自：https://docs.python.org/zh-cn/3/library/turtle.html#turtle.position'''

from turtle import *
color('red', 'yellow')
'''color(colorstring1, colorstring2), color((r1,g1,b1), (r2,g2,b2))
相当于 pencolor(colorstring1) 加 fillcolor(colorstring2)，使用其他输入格式的方法也与之类似。'''
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1: #求坐标向量的模
        break
end_fill()
done()
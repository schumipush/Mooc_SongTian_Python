'''turtle六边形绘制
使用turtle库，绘制一个六边形。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬'''

import turtle as t
for ii in range(6):
    t.right(60)
    t.fd(100)
t.done()

'''参考答案：
#HexagonDraw.py
import turtle as t
t.pensize(2)
for i in range(6):
    t.fd(150)
    t.left(60)'''
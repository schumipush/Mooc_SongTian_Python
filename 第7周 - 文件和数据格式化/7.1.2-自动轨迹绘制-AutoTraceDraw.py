#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensicze(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    # 使用了内置函数map,实现的功能是：将map的第二个参数（split后的列表）中每个元素作为eval的参数执行一次；
    datals.append(list(map(eval,line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

'''数据接口定义：
300，1，144，0，1，0
行进距离，转向判断（0左转，1右转），转向角度，pencolor
'''
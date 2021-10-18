'''星号三角形
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬
第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬'''

odd = eval(input())
if odd%2 == 0:
    print('你输入的这是奇数？？')
else:
    for i in range(odd+1):
        if i%2 == 1:
            #print('{:-^)}'.format('*'*i))
            print(('*'*i).center(odd,' '))

'''【参考答案】
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
关键是对.format()中槽机制的理解，槽中可以嵌套槽，用来表示宽度、填充等含义。'''
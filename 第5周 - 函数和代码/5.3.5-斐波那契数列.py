#斐波那契数列：F(n)=F(n-1)+F(n-2)
#递归的程序的要素：1)函数+分支结构；2)递归链条；3)递归基例;

def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1) + f(n-2)
for i in range(1,20):
    print('{: >2d} | {:3d}'.format(i,f(i)))
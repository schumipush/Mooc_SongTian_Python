count = 0
def hanoi(n, src, dst, mid):
    global count
    if n==1:
        print('{}:{}-->{}'.format(1,src,dst)) #移动最小的圆盘，每次调用时，src、dst表示的柱子会不同
        count += 1
    else:
        hanoi(n-1, src, mid, dst) #先把n-1个圆盘移到过渡位置
        print('{}:{}-->{}'.format(n,src,dst)) #把第n个圆盘移到目标位置
        count += 1
        hanoi(n-1, mid, dst, src) #最后再把n-1个圆盘也移到目标位置
hanoi(3,'A','C','B')
print(count)

'''
说明：
n表示汉诺塔问题中圆盘的数量，圆盘的编号按从小到大为（1,2,...,n）
mid表示3根柱子中的过渡柱子
'''
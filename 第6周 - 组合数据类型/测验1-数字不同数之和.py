'''数字不同数之和
描述
获得用户输入的一个整数N，输出N中所出现不同数字的和。
例如：用户输入 123123123，其中所出现的不同数字为：1、2、3，这几个数字和为6。
'''

s = input()
ss = set(s)
sum = 0
for sss in ss:
    sum += eval(sss)
print(sum)

'''与参考代码思路一致'''

'''【参考代码】

n = input()
ss = set(n)
s = 0
for i in ss:
    s += eval(i)
print(s)
注意，字符串可以通过list()直接变成列表，或通过set()直接变成集合。
'''
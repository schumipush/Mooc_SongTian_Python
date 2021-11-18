'''
CSV格式列变换
附件是一个CSV文件，请将每行按照列逆序排列后输出，不改变各元素格式（如周围空格布局等）。
'''

f = open('data.csv')
for ff in f:
    ff = ff.strip('\n')
    ls = ff.split(',')
    ls.reverse()
    print(','.join(ls))
f.close()

'''
参考答案使用切片实现了列表逆序方法'''

'''【参考代码】

f = open("data.csv")
for line in f:
    line = line.strip("\n")
    ls = line.split(",")
    ls = ls[::-1]
    print(",".join(ls))
f.close()'''
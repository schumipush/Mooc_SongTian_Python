'''
文件行数
打印输出附件文件的有效行数，注意：空行不计算为有效行数。
'''
f = open("latex.log","r").readlines()
count = 0
for line in f:
    if line !='\n':
        count+=1
print("共{}行".format(count))

'''
参考代码中可取的地方是：使用for line in f: 这样不需要调用read()方法'''

'''【参考代码】

f = open("latex.log")
s = 0
for line in f:
    line = line.strip('\n')
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))
需要注意：for line in f方式获得的每行内容（在变量line中）包含换行符，
所以，要通过strip()函数去掉换行符后再进行统计。这里，空行指没有字符的行。'''
'''描述
关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬

统计附件文件中与关键行的数量。'''


f = open('latex.log')
lines = f.readlines()

# 共有a种行
lines_set = set(lines)
a = len(lines_set)

# 把所有的行都剔除一次，b是重复的行的种类
for line in lines_set:
    lines.remove(line)
lines_set2 = set(lines)
b = len(lines_set2)

print('共{}关键行'.format(a-b))


'''这道题做错了，主要是因为没有搞清关键行、独特行这两个东西（之前的练习中统计的是独特行数，就像我的答案这样）'''

'''
【参考代码】

f = open("latex.log")
ls = f.readlines()
s = set(ls)
print("共{}关键行".format(len(s)))
记住：如果需要"去重"功能，请使用集合类型。'''
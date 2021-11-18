'''
文件独特行数
统计附件文件中与其他任何其他行都不同的行的数量，即独特行的数量。
输出示例：
共99独特行
'''

f = open("latex.log","r").readlines()
ff = set(f)
print("共{}独特行".format(len(ff)))

'''
错误原因：
思考得太简单了，我的答案给出的其实是：共有几种不同内容的行；
而统计独特行，要的是只出现过一次的行的数量'''


'''【参考代码】

f = open("latex.log")
ls = f.readlines()
s = set(ls)
for i in s:
    ls.remove(i)
t = set(ls)
print("共{}独特行".format(len(s)-len(t)))
记住：如果需要"去重"功能，请使用集合类型。

ls.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现。'''
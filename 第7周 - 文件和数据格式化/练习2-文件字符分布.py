'''
文件字符分布
统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果。
同时请输出文件一共包含的字符数量。
注意输出格式，各元素之间用英文逗号（,）分隔。
答案可能包含a-z共26个字符的分布，如果某个字符没有出现，则不显示，输出顺序a-z顺序。

输出示例
共999字符,a:11,b:22,c:33,d:44,e:55
'''

f = open("latex.log","r").read().lower()
counts = {}
exclude = '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~ \n0123456789'
for s in exclude:
    f = f.replace(s,'')
for ff in f:
    counts[ff] = counts.get(ff,0) + 1

s="共{}字符".format(len(f))
for a in range(ord('a'),ord('z')+1):
    if chr(a) in counts:
        s += ",{}:{}".format(chr(a),counts.get(chr(a),0))
print(s)

'''
我的答案增加了功能，包括：统一大小写、去掉字母以外其他字符，所以结果与参考答案不同；
没有找到正确答案的原因：
    1. for a in range(ord('a'),ord('z')+1) 这句没有写+1，导致只输出a~y的结果；
    2. 在只做了基本功能，且答案不正确的时候，我并没有检查问题，而是开始增加题目没有要求的功能，导致离正确答案越来越远；
'''


'''【参考代码】

f = open("latex.log")
cc = 0
d = {}
for i in range(26):
    d[chr(ord('a')+i)] = 0
for line in f:
    for c in line:
        d[c] = d.get(c, 0) + 1
        cc += 1
print("共{}字符".format(cc), end="")
for i in range(26):
    if d[chr(ord('a')+i)] != 0:
        print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")
使用 ord('a')+i 配合 range()函数 可以遍历一个连续的字符表。'''
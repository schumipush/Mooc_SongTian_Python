'''
英文字符的鲁棒输入
描述
获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
'''

s = input()
out = ''
for ss in s:
    if ord(ss) in range(ord('a'),ord('z')+1):
        out += ss
    elif ord(ss) in range(ord('A'),ord('Z')+1):
        out += ss
print(out)

'''【参考答案】

alpha = []
for i in range(26):
    alpha.append(chr(ord('a') + i))
    alpha.append(chr(ord('A') + i))
s = input()
for c in s:
    if c in alpha:
        print(c, end="")
注意：这里采用遍历字符的方式实现，通过约束字母表达到鲁棒效果。'''
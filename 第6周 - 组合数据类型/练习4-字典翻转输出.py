'''字典翻转输出
描述
读入一个字典类型的字符串，反转其中键值对输出。即，读入字典key:value模式，输出value:key模式。
输入格式：用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。
输出格式：给定字典d，按照print(d)方式输出

输入输出示例：
输入：{"a": 1, "b": 2}
输出：{1: 'a', 2: 'b'}
'''

s=eval(input())
try:
    s.get('aaa',0)
    keys = list(s.keys())
    values = list(s.values())
    s_reverse = {}
    i = 0
    for value in values:
        s_reverse[value] = keys[i]
        i+=1
    print(s_reverse)

except:
    print('输入错误')

'''【参考代码】

s = input()
try:
    d = eval(s)
    e = {}
    for k in d:
        e[d[k]] = k
    print(e)
except:
    print("输入错误")
'''

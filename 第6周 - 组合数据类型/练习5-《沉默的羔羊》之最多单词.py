'''《沉默的羔羊》之最多单词
附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于等于2且出现频率最多的单词。
如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。
输入格式：文件
输出格式：字符串
输出示例'''
import jieba
with open('沉默的羔羊.txt', 'r', encoding='utf-8') as f:
    s = f.read()
words = jieba.lcut(s)
counts = {}
for word in words:
    if len(word) < 2:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse=True)

print(list(items[0])[0])

'''本答案的不足之处：
我的答案虽然给出正确结果，但没有实现“如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词”这一点。
参考答案中使用了一个表达式“k > maxw”实现这一点。
'''



'''【参考代码】

import jieba
f = open("沉默的羔羊.txt", encoding='utf-8')
ls = jieba.lcut(f.read())
d = {}
for w in ls:
        if len(w) >= 2:
            d[w] = d.get(w, 0) + 1
maxc = 0
maxw = ""
for k in d:
    if d[k] > maxc :
        maxc = d[k]
        maxw = k
    elif d[k] == maxc and k > maxw:
        maxw = k
print(maxw)
f.close()
'''
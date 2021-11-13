'''38003200360032003500321636815146973
实例10：文本词频统计 -- Hamlet
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
文本词频统计：：一篇文章，出现了哪些词？哪些词出现的最多？ 
英文文本：hamlet
请统计hamlet.txt文件中出现的英文单词情况，统计并输出出现最多的10个单词，注意：
(1) 单词不区分大小写，即单词的大小写或组合形式一样；
(2) 请在文本中剔除如下特殊符号：!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~
(3) 输出10个单词，每个单词一行；
(4) 输出单词为小写形式。'''

#请在...处补充代码

def getText():
    txt = open("hamlet.txt", "r").read()
    txt=txt.lower()
    # 出错点1：没有将题目中的 “\”改为“\\”。python中，使用双斜杆表求"\"，其中第一个斜杆作用是转义符。
    # 文本中的单个斜杆读入后，会存为双斜杆
    exclude = '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~'
    for s in exclude:
        # 出错点2：txt.replace()前面没有写"txt="
        # 没有赋值，就不会改变txt中的元素，这一步的操作就没有意义了
        txt=txt.replace(s,' ')
    txt=txt.split()
    return txt
    
txt = getText()
counts = {} #32013
for word in txt:
    counts[word]=counts.get(word,0)+1
items=[]
items=list(counts.items())
items.sort(key= lambda x:x[1], reverse=True)
for ii in range(10):
    a,b=items[ii]
    print(a)

'''【参考代码】

def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt

hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    # print ("{0:<10}{1:>5}".format(word, count))  输出出现最多的10个单词和其出现次数
    print (word)  #输出出现最多的10个单词
'''
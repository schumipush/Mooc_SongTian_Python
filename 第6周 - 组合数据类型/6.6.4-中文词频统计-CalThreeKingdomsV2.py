'''本程序在词频统计基本功能的基础上，进行面向问题的改造升级
需要解决的问题是：统计《三国演义》中人物出场次数
解决这个问题需要实现两点：1是删除结果中的非人名词语，2是合并同一人物的不同名称（如：孔明、诸葛亮对应着同一个人物）'''
#CalThreeKingdomsV1.py
import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
# 加入一个excludes集合，其中存放不属于人名的词语；
# 构造这个集合的方法是根据每次程序运行结果，不断的从词频前10的词语中提取出非人名的词
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word =="诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word =="关公" or word == "云长":
        rword = "关羽"
    elif word =="玄德" or word == "玄德曰":
        rword = "刘备"
    elif word =="孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

'''程序运行结果：
曹操         1451
孔明         1383
刘备         1252
关羽          784
张飞          358
商议          344
如何          338
主公          331
军士          317
吕布          300
'''

'''这个程序仍然需要继续优化，即将输出中的“商议”、“如何”等加入excludes集合中，继续进行优化'''

'''举一反三：
这个问题可以拓展到词频分析、人物统计分析、政府工作报告关键词统计、绘制文本的词云'''
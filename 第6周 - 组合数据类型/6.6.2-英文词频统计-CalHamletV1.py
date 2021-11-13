#CalHamletV1.py
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '|"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
# 经过下面的操作，counts中的第一个键值对，将成为列表items中的一个元素
# items是 [('the', 1138), ('tragedy', 3), ('of', 668),..., ('peal', 1)]
items = list(counts.items())
# 下面以键值对中的值进行排序，从大到小；
# items现在变成了[('the', 1138), ('and', 965), ('to', 754), ...
items.sort(key=lambda x:x[1], reverse=True)
# 打印出出现次数最多的10个单词
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

'''hamlet.txt下载地址：https://python123.io/resources/pye/hamlet.txt'''

'''运行结果如下：
the        1138
and         965
to          754
of          668
you         549
a           542
i           540
my          514
hamlet      456
in          436
'''
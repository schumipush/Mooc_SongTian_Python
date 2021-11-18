#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
ii = 0
# 使用一个循环去掉单个字符
while 1:
    if ii == len(ls):
        break 
    if len(ls[ii]) < 2:
        del ls[ii]
    else:
        ii+=1

txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttc",\
    width = 1000, height = 700, background_color = "white", \
    #增加stopwords参数，剔除不重要的词语（需要不断优化）
    stopwords = set(["以","和","的","是","在","从","更","在","成为"]), \
    max_words = 200 )
w.generate(txt)
w.to_file("grwordcloud_modify.png")
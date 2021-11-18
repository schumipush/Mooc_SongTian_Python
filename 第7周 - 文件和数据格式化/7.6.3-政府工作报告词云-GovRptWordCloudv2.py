#GovRptWordCloudv2.py
'''增加了mask参数，生成一个有形状的词云
在这个例子中，需要提供一个背景是白色的五角星图片 fivestart.png'''
import jieba
import wordcloud
'''
这里从视频中抄写的代码有问题，根据（https://blog.csdn.net/weixin_43938093/article/details/102632520），问题解决办法有两个：
1). pip install scipy==1.2.0 #将scipy库的版本还原至1.2.0版本
2). from imageio import imread #使用imageio库同样能够完成此功能
'''
#from scipy.misc import imread
from scipy.misc import imread
mask = imread("fivestart.png")
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttc", mask = mask, \
    width = 1000, height = 700, background_color = "white", \
    )
w.generate(txt)
w.to_file("grwordcloud.png")
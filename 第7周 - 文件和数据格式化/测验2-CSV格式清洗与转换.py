'''CSV格式清洗与转换
描述
附件是一个CSV格式文件，提取数据进行如下格式转换：
（1）按行进行倒序排列；
（2）每行数据倒序排列；
（3）使用分号（;）代替逗号（,）分割数据，无空格；
按照上述要求转换后将数据输出。 '''

f = open("data.csv")
ss = list()
ii = 0
ls = list()
for ff in f:
    ff = ff.strip("\n")
    ff = ff.replace(" ","")
    ls = ff.split(',')
    ls.reverse()
    str = ';'.join(ls)
    #str += '\n'
    ss.append(str)
ss.reverse()
for sss in ss:
    print(sss)

'''
参考答案的思路是一次读入，行逆序，再依次处理
我的思路是依次读入，依次列逆序，一次性输出
'''


'''【参考代码】

f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()
注意：使用strip()方法去掉每行最后的回车，使用replace()去掉每行元素两侧的空格。'''
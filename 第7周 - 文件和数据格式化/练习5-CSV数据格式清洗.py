f = open("data.csv")
for ff in f:
    ff = ff.replace(' ','')
    ff = ff.strip('\n')
    print(ff)
f.close()

'''
参考答案，没有按行读取、按行打印，更简单'''


'''【参考代码】

f = open("data.csv")
s = f.read()
s = s.replace(" ","")
print(s)
f.close()

该CSV文件的每个数据中不包含空格，因此，可以通过替换空格方式来清洗。如果数据中包含空格，该方法则不适用。'''

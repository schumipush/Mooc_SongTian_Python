'''实例9：基本统计值计算
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
获取以逗号分隔的多个数据输入（输入为一行），计算基本统计值（平均值、标准差、中位数）
除中位数外，其他输出保留小数点后两位。
请补充编程模板中代码完成'''

#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    strin = []
    s=input()
    s=s.split(',')
    for ss in s:
        strin.append(eval(ss))
    return strin

def mean(numbers):  #计算平均值
    sum = 0
    for n in numbers:
        sum += n
    return sum/len(numbers)
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    l = len(numbers)
    numbers.sort()
    if l%2==0:
        return (numbers[l//2] + numbers[l//2-1])/2
    else:
        return numbers[l//2]
    
n =  getNum() #主体函数
m =  mean(n)
sdev = dev(n,m)
median = median(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,sdev,median))

'''【参考代码】

#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    s = input()
    ls = list(eval(s))
    return ls

def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n,m),median(n)))
这是本课程的实例9：

(1) 获取多个数据：从控制台获取逗号分隔的多个数据

(2) 多函数编写方法：模块化设计方法，每部分功能比较清晰

(3) 排序：列表ls的默认排序方法是ls.sort()，如果从大到小排序，用ls.sort(reverse=True)
'''
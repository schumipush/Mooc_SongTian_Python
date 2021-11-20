'''
数字的鲁棒输入
描述
获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进制形式，且只能是数字。对输入数字进行平方运算，输出结果。
要求：
（1）无论用户输入何种内容，程序无错误；
（2）如果输入有误，请输出"输入有误"。
'''

s=input()
try:
    char = s
    for ss in '0123457869+-.j':
        char = char.replace(ss,'')
    if len(char)>0:
        print("输入有误")
    elif 'j' in s:
        print(eval(s)**2)
    elif '+' in s or '-' in s:
        print("输入有误")
    else:
        print(eval(s)**2)
except:
    print("输入有误")

'''【思考】

参考答案使用了complex()函数，很巧妙、简便地实现了判断字符串是否是以正确格式表示的一个数字：
complex([real[, imag]]) 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
如果第一个参数为字符串，则不需要指定第二个参数。

以下实例展示了 complex 的使用方法：

>>> complex(1, 2)
(1 + 2j)

>>> complex(1+2)
(3 + 0j)

>>> complex(1)    # 数字
(1 + 0j)
 
>>> complex("1")  # 当做字符串处理
(1 + 0j)
 
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
'''


'''【参考代码】

s = input()
try:
    if complex(s) == complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")

complex()和complex(eval())之间的比较将能够排除非数字类型的输入。

注意：不能直接使用eval()，否则，用户可以通过输入表达式（如100**2）输入数字，与要求不同（在实际应用中带来安全隐患）。
'''
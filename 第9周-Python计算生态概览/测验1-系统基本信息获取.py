'''系统基本信息获取
描述
获取系统的递归深度、当前执行文件路径、系统最大UNICODE编码值等3个信息，并打印输出。
输出格式如下：
RECLIMIT:<深度>, EXEPATH:<文件路径>, UNICODE:<最大编码值>
提示：请在sys标准库中寻找上述功能。

输入输出示例
这里仅是格式参考，非正确答案，请注意，输出中每个逗号（,）后面都有一个空格。
RECLIMIT:500, EXEPATH:/bin/python, UNICODE:1411
'''

import sys
print('RECLIMIT:{}, EXEPATH:{}, UNICODE:{}'.format(sys.getrecursionlimit(),sys.executable,sys.maxunicode))

'''
sys标准库的文档：https://docs.python.org/zh-cn/3/library/sys.html?highlight=sys#module-sys'''


'''【参考代码】

import sys
print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(sys.getrecursionlimit(), sys.executable, sys.maxunicode))
基本信息获取'''
'''二维数据表格输出
描述
tabulate能够对二维数据进行表格输出，是Python优秀的第三方计算生态。
参考编程模板中给定的数据和代码，编写程序，能够输出如下风格效果的表格数据。'''

from tabulate import tabulate

data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data,tablefmt='grid'))

'''python-tabulate库的文档：https://pypi.org/project/tabulate/'''


'''【参考代码】

from tabulate import tabulate
data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data, tablefmt="grid"))
tabulate库更多使用请参考该库的文档。'''
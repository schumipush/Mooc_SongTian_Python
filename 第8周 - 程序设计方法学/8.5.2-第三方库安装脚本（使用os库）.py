'''8.5.1 推荐的一些库：
NumPy N维数据表示和运算
Matplotlib 二维数据可视化
PIL 图像处理
Scikit-Learn 机器学习和数据挖掘
Requests HTTP协议访问及网络爬虫
Pyinstaller 打包Python源文件为可执行文件
WeRoBot 微信机器人开发框架
SymPy 数学符号计算工具
Pandas 高效数据分析和计算
PyQt5 基于Qt的专业级GUI开发框架
PyPDF2 PDF文件内容提取及处理
docopt Python命令行解析
'''


#BatchInstall.py
import os
libs = {"numpy","matplotlib","wordcloud","pyinstaller","jieba","requests"}

try:
    for lib in libs:
        os.system("pip install "+ lib)
    print("Successful")
except:
    print("Failed Somehow")
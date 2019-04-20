#! usr/bin/env python3
# -*- coding:utf-8 -*-
# _author_ ='Lishunli'
# Email:17801063098@163.com
"""利用jieba模块实现中文分词、词频统计"""

###导入模块
import jieba
import jieba.analyse

###读入数据
with open('/Users/lishunli/Desktop/中央财经大学/研一下/应用案例选讲/课堂作业/第五次/zhongwen.txt', 'r') as file:
    zhongwen = file.read()

zhongwen = zhongwen.lower()  ###将所有字母小写
print(zhongwen)

jieba.load_userdict('/anaconda3/lib/python3.7/site-packages/jieba/dict.txt') #打开本地用户词典

###jieba模块分词
zhongwen_fenci = jieba.cut(zhongwen, cut_all=False)  #精确模式 #True为
print(list(zhongwen_fenci))

###Jieba基于TF-IDF算法的关键词抽取
jieba.analyse.extract_tags(zhongwen, topK = 7, withWeight = True, allowPOS = ('n', 'vn', 'v', 'ns'), withFlag = True)

###Jieba基于TextRank算法的关键词抽取
jieba.analyse.textrank(zhongwen, topK = 7, withWeight = True, allowPOS = ('ns', 'n', 'v', 'vn'), withFlag = True)

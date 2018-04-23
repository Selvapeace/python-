import jieba

'''
精确模式：把文本精确切分开，不存在冗余单词
全模式：把文本中所有可能的词语都扫描出来，有冗余
搜索引擎模式：在精确模式的基础上，对长词再次切分，从而可对短词语搜索
'''

s = '我家猪宝宝要不要学机器学习要学python和r中国是哈哈哈哈'
a =jieba.lcut(s)  # 精确模式，返回一个列表类型的分词结果
b = jieba.lcut(s,cut_all = True)    # 全模式
c = jieba.lcut_for_search('中华人民共和国中央人民政府')   # 搜索引擎模式
jieba.add_word('是哈哈哈哈')     # 向词库增加新词语
d =jieba.lcut(s)

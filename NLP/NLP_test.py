#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   NLP_test.py
@Time    :   2019/11/12 15:17:15
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''
#jieba.analyse.extract_tags(sentence , topK=5,withWeight=False)
''''
sentence：待提取的文本语料；
topK：返回 TF/IDF 权重最大的关键词个数，默认值为 20；
withWeight：是否需要返回关键词权重值，默认值为 False；
'''
# here put the import code
import jieba
import jieba.analyse

def demo1():
    sentence  = "人工智能（Artificial Intelligence），英文缩写为AI。它是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器，该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大，可以设想，未来人工智能带来的科技产品，将会是人类智慧的“容器”。人工智能可以对人的意识、思维的信息过程的模拟。人工智能不是人的智能，但能像人那样思考、也可能超过人的智能。人工智能是一门极富挑战性的科学，从事这项工作的人必须懂得计算机知识，心理学和哲学。人工智能是包括十分广泛的科学，它由不同的领域组成，如机器学习，计算机视觉等等，总的说来，人工智能研究的一个主要目标是使机器能够胜任一些通常需要人类智能才能完成的复杂工作。但不同的时代、不同的人对这种“复杂工作”的理解是不同的。2017年12月，人工智能入选“2017年度中国媒体十大流行语”。"
    keywords = "  ".join(jieba.analyse.extract_tags(sentence , topK=5,withWeight=False))
    print("文章关键词TOP5:")
    print(keywords)
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
    keywords =(jieba.analyse.extract_tags(sentence , topK=5, withWeight=True))
    for item in keywords:
        # 分别为关键词和相应的权重
        print(item[0], item[1])



    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

    txt='那些你很冒险的梦，我陪你去疯，折纸飞机碰到雨天终究会坠落，伤人的话我直说，因为你会懂，冒险不冒险你不清楚，折纸飞机也不会回来，做梦的人睡不醒！'
    Key=jieba.analyse.extract_tags(txt,topK=3)
    print(Key)
    #-----------------------------------------------------------------------------------
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

    # 字符串前面加u表示使用unicode编码
    content = u'中国特色社会主义是我们党领导的伟大事业，全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'
    # 第一个参数：待提取关键词的文本
    # 第二个参数：返回关键词的数量，重要性从高到低排序
    # 第三个参数：是否同时返回每个关键词的权重
    keywords = jieba.analyse.extract_tags(content, topK=5, withWeight=True)
    # 访问提取结果
    for item in keywords:
        # 分别为关键词和相应的权重
        print(item[0], item[1])


key_word = "你叫什么名字"  # 定义一句话,基于这句话进行分词
cut_word = jieba.cut(key_word)  # 使用结巴分词中的cut方法对"你叫什么名字" 进行分词
print(cut_word)  # <generator object Tokenizer.cut at 0x03676390> 不懂生成器的话,就忽略这里
cut_word_list = list(cut_word)  # 如果不明白生成器的话,这里要记得把生成器对象做成列表
print(cut_word_list)  # ['你', '叫', '什么', '名字']


import jieba
import gensim
from gensim import corpora
from gensim import models
from gensim import similarities

l1 = ["你的名字是什么", "你今年几岁了", "你有多高你胸多大", "你胸多大"]
a = "你今年多大了"

all_doc_list = []
for doc in l1:
    doc_list = [word for word in jieba.cut(doc)]
    all_doc_list.append(doc_list)

print(all_doc_list)
doc_test_list = [word for word in jieba.cut(a)]

# 制作语料库
dictionary = corpora.Dictionary(all_doc_list)  # 制作词袋
# 词袋的理解
# 词袋就是将很多很多的词,进行排列形成一个 词(key) 与一个 标志位(value) 的字典
# 例如: {'什么': 0, '你': 1, '名字': 2, '是': 3, '的': 4, '了': 5, '今年': 6, '几岁': 7, '多': 8, '有': 9, '胸多大': 10, '高': 11}
# 至于它是做什么用的,带着问题往下看

print("token2id", dictionary.token2id)
print("dictionary", dictionary, type(dictionary))

corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
# 语料库:
# 这里是将all_doc_list 中的每一个列表中的词语 与 dictionary 中的Key进行匹配
# 得到一个匹配后的结果,例如['你', '今年', '几岁', '了']
# 就可以得到 [(1, 1), (5, 1), (6, 1), (7, 1)]
# 1代表的的是 你 1代表出现一次, 5代表的是 了  1代表出现了一次, 以此类推 6 = 今年 , 7 = 几岁
print("corpus", corpus, type(corpus))

# 将需要寻找相似度的分词列表 做成 语料库 doc_test_vec
doc_test_vec = dictionary.doc2bow(doc_test_list)
print("doc_test_vec", doc_test_vec, type(doc_test_vec))

# 将corpus语料库(初识语料库) 使用Lsi模型进行训练
lsi = models.LsiModel(corpus)
# 这里的只是需要学习Lsi模型来了解的,这里不做阐述
print("lsi", lsi, type(lsi))
# 语料库corpus的训练结果
print("lsi[corpus]", lsi[corpus])
# 获得语料库doc_test_vec 在 语料库corpus的训练结果 中的 向量表示
print("lsi[doc_test_vec]", lsi[doc_test_vec])

# 文本相似度
# 稀疏矩阵相似度 将 主 语料库corpus的训练结果 作为初始值
index = similarities.SparseMatrixSimilarity(lsi[corpus], num_features=len(dictionary.keys()))
print("index", index, type(index))

# 将 语料库doc_test_vec 在 语料库corpus的训练结果 中的 向量表示 与 语料库corpus的 向量表示 做矩阵相似度计算
sim = index[lsi[doc_test_vec]]

print("sim", sim, type(sim))

# 对下标和相似度结果进行一个排序,拿出相似度最高的结果
# cc = sorted(enumerate(sim), key=lambda item: item[1],reverse=True)
cc = sorted(enumerate(sim), key=lambda item: -item[1])
print(cc)

text = l1[cc[0][0]]

print(a,text)

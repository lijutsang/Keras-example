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

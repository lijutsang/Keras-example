#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/12/10 17:14:24
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''
from chatterbot import ChatBot
#创建一个新的聊天机器人
chatbot = ChatBot("Test")
#用语料数据训练机器人
from chatterbot.trainers import ListTrainer
#语料库
conversation = [
    "你叫什么名字？",
    "我叫Chelsea。",
    "今天天气真好",
    "是啊，这种天气出去玩再好不过了。",
    "那你有没有想去玩的地方？",
    "我想去有山有水的地方。你呢？",
    "还有好多作业没做呢",
    "哈哈，这就比较尴尬了",
    "你喜欢什么运动",
    "我喜欢游泳",
    "Good morning!",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
#选择训练器
#trainer = ListTrainer(chatbot)
#开始训练
#trainer.train(conversation)
#获得响应
s ='你喜欢什么运动!'
response = chatbot.get_response(s)
print('问:{}\n答:{}'.format(s,response))


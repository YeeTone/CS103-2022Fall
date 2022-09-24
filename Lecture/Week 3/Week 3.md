# CS103 Week 3

## AI的三大主义

符号主义，连接主义和行为主义。先做一个简要的个人理解：

符号主义集中于思维和数据的抽象；连接主义集中于思维的形象化；行为主义集中于思维的感知、

![image](https://user-images.githubusercontent.com/64548919/192088653-393ef399-406c-4f05-828d-7c43516f42a8.png)

- Symbolicism（符号主义）
  
又称为Logicism（逻辑主义），Psychologism（心理学派）或者Computerism（计算机学派）。

主要组成部分：
1. 数学逻辑
2. 专家系统
3. 知识工程

此时的智能是由人类赋予的，是一种基于逻辑推理的智能模拟方法。

这个是早期的人工智能研究，他们的主要观点有以下几点：
1. 人类认知和思维的基本单元是符号
2. 计算机是物理符号系统
3. 认知过程就是在符号表示上的一种运算

- Connectionism（连接主义）

又称为Bionicsism（仿生学派）或者Physiologism（生理学派）。

主要组成部分：
- 人工神经元
- 感知器
- BP神经网络
- DNN（全连接神经网络）

此处的智能是机器学习而来的。

他们的主要原理是神经网络和神经网络之间的连接机制和学习算法，他们的研究方法是利用数学模型来研究人来认知的方法，通常以高度互联、类似神经元的处理单元出现。

他们的主要观点有：
1. 人类智能归结为人脑的高层活动
2. 智能的产生是由大量简单的单元通过复杂的连接和并行运行的结果。

- Actionism（行为主义）

又称为Evolutionism（进化主义）和Cyberneticism（控制论学派）

主要组成部分：
- 强化学习
- 智能机器人

此处的智能是机器从环境的反馈学习而来的。

他们的主要观点是人工智能来源于控制论。

## Intelligent Agent

定义要抓住两个方面：
- perceives its environment（感知周围的环境）
- takes actions that maximize its chance of success（最大化胜利的可能性）

上面是IA的定义，Agent的定义就更加广泛一点：

- perceive its environment through sensors（通过感知器感知环境）
- act upon that environment through effector（通过效应器作用域环境）

强化学习和智能体的5大关键要素
- agent（智能体）
- action（动作）
- environment（环境）
- state（状态）
- reward（奖励）

![image](https://user-images.githubusercontent.com/64548919/192088915-b1d99212-fc4c-41e2-9389-2c50659b6f05.png)

Example:

对于自动驾驶智能体来说：
- agent就是采取驾驶行为的智能体
- action是智能体发出的驾驶行为
- environment是车辆行驶时周围的环境
- state是智能体从环境获得或者观测得到的信息
- reward是环境对于智能体行为所做出的反馈，这个反馈正面和负面都有可能

接下来介绍下AI的几个组成部分：
- 观测环境
  - 观测并理解环境
  - 模式识别，机器学习，深度学习
  - 事实抽象，如知识表示，数据挖掘，搜索等等
- 采取行动
  - 决策（搜索，推理，机器学习，不确定性检验，演化计算）
- 最大化胜利概率
  - 优化
  - 演化计算
# Jittor 第三届计图挑战热身赛

![主要结果](https://img.ziuch.top/i/2023/07/18/93000_64b569a9394f6.png)

## 简介

本项目包含了第三届计图挑战赛热身赛的代码实现。本项目的特点是：利用jittor框架实现Conditional GAN（Conditional Generative Adversarial Nets）对一个随机向量 z 和额外辅助信息 y 进行处理，生成特定数字的图像。

## 安装
本项目可在 1 张 3090 上运行，训练时间约为 0.5 小时。

#### 运行环境
- ubuntu 20.04 LTS
- python >= 3.7
- jittor >= 1.3.0

#### 安装依赖
执行以下命令安装 python 依赖
```
pip install -r requirements.txt
```

## 训练
｜ 介绍模型训练的方法

单卡训练可运行以下命令：
```
python CGAN.py
```

## 推理

生成结果可以运行以下命令：

```
python test.py --number 1234567890
```

## 致谢

此项目基于论文 *Conditional Generative Adversarial Nets* 实现，部分代码参考了 [jittor-gan](https://github.com/Jittor/gan-jittor)。

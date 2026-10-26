# CICIDS2017 | Adversarial Intrusion Detection

**个人项目** · Python · PyTorch · CNN · DQN · Robustness Evaluation

[首页](../README.md) · [公开源码](https://github.com/ck458/CICIDS2017)

## 项目背景

围绕网络流量异常识别，搭建 CNN 入侵检测系统并结合强化学习生成对抗流量样本，用于检测器鲁棒性分析。

## 我的职责

**CNN 检测：** 建立数据预处理、输入特征构造、模型训练和验证流程，管理训练权重和推理输出。

**DQN Agent：** 设计与检测器交互的扰动环境，训练强化学习策略构造对抗样本。

**评测与系统化：** 串联基础检测、对抗生成、对抗训练与最终指标计算，并将代码划分为 preprocessing、models、rl、attack 和 evaluation 模块。

**公开源码：** [ck458/CICIDS2017](https://github.com/ck458/CICIDS2017)

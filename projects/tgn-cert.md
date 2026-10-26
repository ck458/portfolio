# TGN × CERT | Temporal Event Anomaly Detection

**机器学习工程** · PyTorch · Temporal Graphs · Sentence-Transformer

[首页](../README.md)

## 项目背景

将连续行为日志表示为时序交互图，结合用户、设备、事件内容和时间信息开展异常识别。

## 核心实现

**事件预处理：** 将 CERT 宽表转化为全局按时间排序的事件序列，提取用户、设备、文件、邮件和 HTTP 等行为字段。

**多源特征融合：** 使用 Sentence-Transformer 生成 **384维归一化文本向量**，结合结构化事件统计，并采用训练时段拟合的标准化变换。

**TGN 适配：** 利用 temporal memory、time encoding、temporal attention 和 message aggregation，实现事件级评分头与训练入口。

**评测设计：** 保持事件时间顺序，结合验证集阈值选择，对 AUROC、AUPRC、Precision、Recall 和 F1 进行统计。

~~~mermaid
flowchart LR
 A[Event Logs] --> B[Chronological Features]
 B --> C[Text + Structured Embeddings]
 C --> D[TGN Temporal Memory]
 D --> E[Event Scoring]
 E --> F[Evaluation]
~~~

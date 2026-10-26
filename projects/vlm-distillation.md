# Qwen3-VL 8B → 2B | Multimodal Training & Evaluation

**角色：研究设计、模型实验与工程实现** · PyTorch · LoRA · Slurm · ScienceQA · MMStar

[首页](../README.md) · [技术架构](../docs/system-architecture.md) · [配对评测代码](../samples/evaluation/paired_bootstrap.py)

## 研究背景

围绕轻量多模态模型的直接答案任务，研究教师答案、推理文本和视觉证据如何影响 Student 的学习表现与跨数据集泛化。

## 职责与技术实现

**01 · 教师数据审计：** 构建 ScienceQA 固定子集 5,000/500/500，审核 Teacher 输出的完整性与答案可解析性，建立样本映射、配置和 SHA-256 数据清单。

**02 · 模型微调与实验组织：** 搭建 Qwen3-VL-8B Teacher / Qwen3-VL-2B Student 的 LoRA 训练链路；通过 Slurm 编排 GPU 作业与评估依赖，管理种子、训练视图、模型参数及运行记录。

**03 · 视觉评测与泛化：** 实现 image / no-image / mismatch 评测条件，记录逐样本预测与解析状态，并对 MMStar clean 的 1,431 条样本进行外部验证。

**04 · 统计与机制分析：** 开展配对 Bootstrap、matched-random、训练权重与阶段对照，汇总准确率、答案变化和区间估计，支撑可重复的技术判断。

## Pipeline

~~~mermaid
flowchart LR
 A[Source Data] --> B[Teacher Audit + Versioned Views]
 B --> C[Student LoRA Training]
 C --> D[ScienceQA + MMStar]
 D --> E[Paired Statistics]
 E --> F[Experiment Evidence]
~~~

## Selected results

| 项目 | 结果 |
| --- | ---: |
| Student · ScienceQA test | **95.6%** |
| Student · MMStar clean | **57.79%** |
| Base 2B · MMStar clean | 49.76% |
| Teacher 输出审计规模 | **5,000 条** |
| Clean 外部评测样本 | **1,431 条** |

学生模型指标对应匹配协议下的 answer-only 训练条件。[查看配对评测工具](../samples/evaluation/paired_bootstrap.py)。

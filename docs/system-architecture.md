# System Architecture | 架构总览

[首页](../README.md) · [代码](code-gallery.md)

## Novel Engine · Agent Orchestration

~~~mermaid
flowchart TD
 A[Canonical State] --> B[Context Retrieval]
 B --> C[Agency & Planning]
 C --> D[Model Execution]
 D --> E[Evidence + Checks]
 E --> F[Review & Approval]
 F --> G[(Durable Commit)]
 C -.-> H[Versioned RunJournal]
 D -.-> H
 E -.-> H
~~~

关键模块：状态机、步骤检查点、模型适配、持久化事务、审阅与恢复。

## Multimodal Distillation · Evaluation

~~~mermaid
flowchart LR
 A[Teacher Audit] --> B[Versioned Training Data]
 B --> C[Student LoRA]
 C --> D[ScienceQA / MMStar]
 D --> E[Paired Bootstrap]
 E --> F[Evidence Report]
~~~

关键模块：教师数据质量、训练/评测一致性、逐样本比较、可信统计。

## Study Logs · Application

~~~mermaid
flowchart LR
 A[Typed UI] --> B[API Routes]
 B --> C[Business Services]
 C --> D[Data Storage]
 D --> E[History]
 B --> F[AI Context]
~~~

关键模块：前后端协作、查询与写入职责、结构化业务数据及时间线聚合。

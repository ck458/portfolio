<p align="center"><img src="assets/portfolio-banner.svg" width="100%" alt="ck458 · AI Research and Engineering"></p>
<p align="center"><strong>Multimodal Learning · Research Engineering · Agent Systems · Full-Stack Products</strong></p>
<p align="center"><a href="README.en.md">English</a> · <a href="docs/project-index.md">按岗位浏览</a> · <a href="docs/code-gallery.md">精选代码</a> · <a href="docs/engineering-evidence.md">研究与工程成果</a></p>

# ck458 | AI Research & Engineering

南京理工大学 · 数据科学与大数据技术 · 2027届 · 已保研

从真实研究问题出发，设计有说服力的实验，再将模型能力转化为可运行、可维护的 AI 系统。重点方向：**多模态训练与评测、LLM Agent、研究工程、全栈应用开发**。

## Selected achievements

| 成果 | 技术与指标 |
| :--- | :--- |
| **ICONIP 2026 · Oral** | 第一作者研究 REVEAL，连续时间动态图异常检测 |
| **4/4 real datasets** | REVEAL 在四个真实数据集取得最佳 AUPRC |
| **+61.7% relative AUPRC** | REVEAL 在 BitcoinOTC 上相对官方 SLADE |
| **95.6% / 57.79%** | Qwen3-VL-2B · ScienceQA test / MMStar clean，匹配协议的 answer-only 模型 |
| **544 automated tests** | Novel Engine 最新分支，Windows / Ubuntu 双平台 CI |
| **24 API routes** | Study Logs 全栈产品，涵盖计划、计时、复盘和 AI 数据整理 |

## Featured projects

### 01 · [Novel Engine | Reliable Agent Workflow](projects/novel-engine.md)
**个人项目负责人 · Python / LLM Workflows / SQLite / Testing**

- **项目背景：** 将 AI 长任务中的规划、模型执行、知识状态、审核与结果保存组织为可靠工作流。
- **职责与技术：** 从0到1设计多阶段 Agent 工作流、模型适配层、RunJournal 检查点、原子提交、任务恢复、成本追踪和自动化测试。
- **量化成果：** 10章隔离场景端到端运行验证；**544项自动化测试通过**，Windows / Ubuntu 双平台 CI 成功。

[查看项目详情](projects/novel-engine.md) · [工作区校验代码](samples/novel-engine/workspace_paths.py)

### 02 · [Qwen3-VL 8B→2B | Multimodal Post-Training](projects/vlm-distillation.md)
**研究设计与工程实现 · PyTorch / LoRA / Slurm / Evaluation**

- **研究背景：** 探究教师答案、推理文本及视觉证据对小型视觉语言模型的学习效果。
- **职责与技术：** 建立 Teacher 输出审计、数据版本、LoRA 训练、Slurm 作业编排、视觉输入干预、跨数据集评测及配对统计。
- **量化成果：** ScienceQA test **95.6%**，MMStar clean **57.79%**；对1,431条外部样本完成评测。

[查看研究详情](projects/vlm-distillation.md) · [统计评测代码](samples/evaluation/paired_bootstrap.py)

### 03 · [REVEAL | Dynamic Graph Anomaly Detection](projects/reveal.md)
**ICONIP 2026 · 第一作者 Oral · Method Design / Benchmarking**

- **研究背景：** 增强连续时间动态图中局部异常证据的可见性。
- **职责与技术：** 设计 evidence-conditioned residual scoring，负责核心方法实现、异常注入、基线复现、5次独立实验及统计分析。
- **量化成果：** 四个真实数据集最佳 AUPRC；BitcoinOTC 相对官方 SLADE **+61.7%**。

[查看研究成果](projects/reveal.md)

### 04 · [Study Logs | Full-Stack AI Productivity](projects/study-logs.md)
**独立产品设计与研发 · Next.js / React / TypeScript / API Engineering**

- **项目背景：** 将个人任务、专注时间、日常记录和长期成长档案整合为连续工作流。
- **职责与技术：** 负责页面交互、数据模型、业务接口、服务与查询层分离、AI 上下文汇总、数据导出和会话管理。
- **工程成果：** **24个API路由模块、13个页面入口**，支持完整的记录、检索与复盘流程。

[查看产品详情](projects/study-logs.md) · [日期业务代码](samples/study-logs/period.ts)

### Additional machine learning projects

- [TGN × CERT | Temporal Event Anomaly Detection](projects/tgn-cert.md)：时序图记忆、文本语义嵌入、结构化特征融合。
- [CICIDS2017 | Adversarial Intrusion Detection](projects/cicids2017.md)：CNN 检测、DQN 对抗样本生成、鲁棒性评测。[公开完整源码](https://github.com/ck458/CICIDS2017)。

## Technical toolkit

**ML / Research:** Python, PyTorch, LoRA/SFT, temporal graphs, VLM evaluation, paired statistics, Slurm  
**System Engineering:** ModelAdapter, Agent workflows, SQLite, transactional persistence, checkpointing, Git, CI  
**Application Engineering:** TypeScript, React, Next.js, typed APIs, domain models, service-layer design

## Selected code and evidence

| 示例 | 展示的技术能力 |
| --- | --- |
| [WorkspacePaths](samples/novel-engine/workspace_paths.py) | 工作区目录边界与路径约束 |
| [Atomic I/O](samples/novel-engine/io_utils.py) | 原子写入与持久化 |
| [Paired Bootstrap](samples/evaluation/paired_bootstrap.py) | 配对评测、答案翻转和置信区间 |
| [Period Utilities](samples/study-logs/period.ts) | 时区与日期区间业务逻辑 |

[![Portfolio sample checks](https://github.com/ck458/portfolio/actions/workflows/samples.yml/badge.svg)](https://github.com/ck458/portfolio/actions/workflows/samples.yml)

[项目导览](docs/project-index.md) · [技术架构](docs/system-architecture.md) · [工程验证](docs/engineering-evidence.md) · [面试与技术证据导览](docs/portfolio-readiness.md) · [静态作品展示](docs/static-site.md)

**联系：** [GitHub @ck458](https://github.com/ck458)

<sub>© 2026 ck458 · All rights reserved.</sub>

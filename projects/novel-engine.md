# Novel Engine | Reliable Agent Workflow

**角色：个人项目负责人** · Python · Agent Orchestration · SQLite · Model Adapters · CI

[首页](../README.md) · [架构](../docs/system-architecture.md) · [代码](../docs/code-gallery.md)

## 项目背景

以长流程 AI 创作作为真实应用场景，将模型规划、上下文检索、内容生成、结构化状态更新、人工审核和持久化组织为端到端可执行的生产工作流。

## 职责与技术实现

**01 · Agent 系统架构：** 主导 Agency、Planner、Composer、Evidence Extractor 与 Review 的职责划分，设计结构化执行契约与多阶段状态演进。

**02 · 任务恢复与数据一致性：** 实现 RunJournal，记录输入指纹、步骤产物、运行时间与 SHA-256；结合 SQLite 原子事务、幂等恢复、检查点与操作锁维护长流程一致性。

**03 · 模型服务集成：** 设计模型适配接口，接入远程推理服务和 Codex CLI；实现结构化输出校验、调用记录、token 归因与成本管理。

**04 · 工程可靠性：** 实现路径边界校验、原子文件落盘、审阅候选指纹绑定、修订范围约束和多平台自动化测试。

**05 · 创作工作流质量：** 将人物行为候选、场景目标、检查意见与局部修订接入同一执行链，形成可追踪、可审核的编辑流程。

## Architecture

~~~mermaid
flowchart TD
 A[Author Plan + Canonical State] --> B[Context Retrieval]
 B --> C[Agency + Planning]
 C --> D[Model Execution]
 D --> E[Evidence Extraction + Checks]
 E --> F[Review Package]
 F --> G[Explicit Approval]
 G --> H[(Durable State)]
 C -.-> J[Versioned RunJournal]
 D -.-> J
 E -.-> J
 G -.-> K[Usage Ledger]
~~~

## Quantified results

| 验证项目 | 成果 |
| --- | --- |
| 回归测试 | **544 tests passed** |
| 系统平台 | **Windows / Ubuntu CI 成功** |
| 完整流程 | **10章节 / 10次状态提交** 的隔离端到端运行 |
| 测试覆盖 | 状态持久化、步骤恢复、事务一致性、模型适配、路径校验和审核权限 |

[精选代码：安全工作区](../samples/novel-engine/workspace_paths.py) · [原子写入](../samples/novel-engine/io_utils.py)

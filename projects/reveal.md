# REVEAL | Dynamic Graph Anomaly Detection

**ICONIP 2026 · First Author · Oral**

[首页](../README.md) · [科研工程](vlm-distillation.md)

## 背景

连续时间动态图中的异常行为常表现为短时结构变化、端点支持关系漂移与局部分布变化。REVEAL 围绕局部异常证据的可见性提出增强评分框架。

## 我的贡献

**问题分析：** 对 SLADE、F-FADE、MIDAS-F 等异常检测器开展复现与异常注入分析，形成短时变化和局部支持异常的实验诊断。

**方法设计：** 提出 evidence-conditioned residual scoring，结合分数秩变换、条件正残差、可靠性路由与上下文证据融合。

**实验实施：** 在 BitcoinAlpha、BitcoinOTC、Reddit、Wikipedia 和 EmailEU 合成数据上实施对照、消融、5次独立运行及统计分析。

**论文与研究表达：** 作为第一作者负责方法实现、研究设计、主要实验、结果分析和论文写作，成果被 ICONIP 2026 录用并安排 Oral。

## Quantified results

| 研究指标 | 结果 |
| --- | --- |
| 真实数据 AUPRC | **4/4 最佳** |
| BitcoinOTC AUPRC | 相对官方 SLADE **+61.7%** |
| EmailEU 合成数据 AUROC | **8/8 最佳** |
| 实验重复 | **5 independent runs** |

**Technical keywords:** Temporal graphs, anomaly scoring, residual evidence, controlled evaluation, statistical testing.

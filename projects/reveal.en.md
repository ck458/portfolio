# REVEAL · Residual Evidence Enhancement for Dynamic Graph Anomaly Detection

**First author · ICONIP 2026 Oral Presentation**  
**Field:** Continuous-time dynamic graph anomaly detection

[Portfolio](../README.en.md) · [中文版](reveal.md)

## Research motivation

In social and financial interaction streams, anomalous activity may appear as short-window structural changes, changes in the supporting endpoint or localized behavioral distribution shifts. Strong memory-based detectors benefit from additional local context when ranking individual events.

## My contributions

**Problem diagnosis.** Studied representative methods including SLADE, F-FADE and MIDAS-F. Designed synthetic anomalies representing burst-like interactions, microclusters, bridges and gradual drift.

**Method design.** Proposed an evidence-conditioned residual scoring framework. The method transforms the backbone and contextual signals into empirical ranks, introduces conditional positive residuals, and combines evidence channels with reliability-aware gating.

**Implementation and benchmarking.** Conducted baseline replication, anomaly injection, experiments on four real-world interaction datasets and synthetic settings, repeated evaluation, statistical testing and ablation analysis.

**Scientific communication.** Led the research framing, core method design and experimental implementation, and prepared the first-author paper accepted at ICONIP 2026 with an oral presentation assignment.

## Selected results

| Benchmark | Reported outcome |
| --- | --- |
| BitcoinAlpha, BitcoinOTC, Reddit, Wikipedia | **Best AUPRC on 4/4 datasets** |
| BitcoinOTC compared with official SLADE | **+61.7% relative AUPRC** |
| EmailEU synthetic anomaly configurations | **Best AUROC in 8/8 cases** |
| Experiment repetitions | **5 independent runs** |

The project demonstrates problem-driven algorithm development, careful benchmark design and statistical evaluation of temporal machine learning methods.

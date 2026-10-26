# Portfolio Readiness | Project Evidence & Interview Guide

[Portfolio](../README.md) · [English](../README.en.md) · [Code gallery](code-gallery.md)

## Agent systems

**Novel Engine** demonstrates an agent system integrating planning, model execution, versioned checkpoints, validation, review and durable state commits.

When discussing the project, walk through one request's lifecycle: state retrieval → plan creation → model output → artifact checkpoint → evidence extraction → review → transaction commit. Reference the public [WorkspacePaths](../samples/novel-engine/workspace_paths.py) and [atomic I/O](../samples/novel-engine/io_utils.py) samples for implementation details.

Key outcome: **544 automated tests** on the source project with cross-platform verification, plus a ten-chapter isolated end-to-end engineering sequence.

## Multimodal model research

**Qwen3-VL 8B→2B** demonstrates an experimental system spanning training-data audits, controlled supervision, LoRA training, GPU batch orchestration and external evaluation.

Describe the benchmark comparison precisely:

- ScienceQA test: **95.6%**, matched answer-only student.
- MMStar clean: **57.79%**, 1,431 evaluation samples.
- MMStar clean 2B zero-shot: **49.76%**.

The public [paired-bootstrap module](../samples/evaluation/paired_bootstrap.py) illustrates per-example statistical comparisons.

## Temporal anomaly detection

**REVEAL** combines an explicit diagnosis with a scoring mechanism, multiple baselines and repeated measurement. The paper is accepted as an **ICONIP 2026 Oral**.

Explain empirical rankings using the correct metric: **AUPRC best on four real datasets**, and **+61.7% relative AUPRC on BitcoinOTC compared with official SLADE**.

## Full-stack engineering

**Study Logs** showcases a typed front-end/API application, 24 API route modules, data services, dated activity records and AI-oriented context composition.

The [date utilities](../samples/study-logs/period.ts) include calendar and timezone edge cases, now covered by automated Node-based regression tests.

## Code quality verification

Public selected examples are verified on Windows and Ubuntu using GitHub Actions with Python 3.12 and Node.js 22. The workflow exercises path and atomic-write behavior, paired prediction evaluation, actual TypeScript date operations, documentation links and publication safety rules.

[Run the checks](https://github.com/ck458/portfolio/actions/workflows/samples.yml).

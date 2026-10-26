# Qwen3-VL 8B → 2B · Multimodal Training & Evaluation

**Role:** Research design, model experimentation and infrastructure implementation  
**Stack:** PyTorch · LoRA · Slurm · ScienceQA · MMStar · Paired Bootstrap

[Portfolio](../README.en.md) · [Statistics code](../samples/evaluation/paired_bootstrap.py) · [中文版](vlm-distillation.md)

## Research question

How do a teacher model's final answers, reasoning explanations and visual evidence influence the effectiveness of post-training for a compact vision-language model? The experimental system uses Qwen3-VL-8B-Instruct as teacher and Qwen3-VL-2B-Instruct as student.

## My responsibilities

**Data engineering.** Defined fixed ScienceQA image splits of 5,000 training, 500 validation and 500 test items. Implemented teacher-output parsing, answer audits, sample identity checks, content manifests and training-view construction.

**Model training and orchestration.** Built a LoRA training pipeline for answer-only, teacher-answer and rationale-based supervision. Managed Slurm batch execution, dependent jobs, configuration snapshots and checkpoint metadata.

**Evaluation design.** Implemented paired evaluation for image, no-image and mismatched-image conditions, with per-sample outputs and interpretation of answer changes. Applied an external MMStar clean evaluation containing 1,431 examples.

**Statistical analysis.** Used paired bootstrap intervals, matched-random comparisons, and supervision-weight / training-phase controls to compare experimental conditions under matched budgets.

## Training and evaluation flow

~~~mermaid
flowchart LR
  A[Fixed Input Splits] --> B[Teacher Audit]
  B --> C[Student LoRA Training]
  C --> D[ScienceQA Test]
  C --> E[MMStar Clean]
  D --> F[Paired Comparison]
  E --> F
~~~

## Selected results

| Experiment | Measured outcome |
| --- | ---: |
| Qwen3-VL-2B · ScienceQA test | **95.6% accuracy** |
| Qwen3-VL-2B · MMStar clean | **57.79% accuracy** |
| Original 2B zero-shot · MMStar clean | 49.76% accuracy |
| Audited teacher outputs | 5,000 |
| Clean external evaluation set | 1,431 |

Student results here refer to the **matched-protocol answer-only training condition**, preserving the exact experimental context of the reported measurements.

[Inspect paired prediction comparison implementation](../samples/evaluation/paired_bootstrap.py).

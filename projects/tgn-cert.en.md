# TGN × CERT · Temporal Event Anomaly Detection

**Role:** Machine learning engineering  
**Stack:** PyTorch · Temporal Graph Networks · Sentence-Transformer · Structured Event Features

[Portfolio](../README.en.md) · [中文版](tgn-cert.md)

## Problem

Model behavior logs as continuous-time interaction events and combine text semantics with structured event features for temporal anomaly classification.

## Implementation

**Chronological preprocessing.** Converted event logs into ordered interactions, preserving user, device, file, email and HTTP activity fields and explicit event identifiers.

**Text and structured representation.** Used a Sentence-Transformer to compute 384-dimensional normalized event embeddings and complemented them with numerical and categorical event statistics. Structured feature normalization was fitted on training-time data.

**Temporal model adaptation.** Extended a TGN-based architecture, retaining temporal memory, time encodings, message aggregation and temporal attention, with an event-level anomaly head and task-specific training entry point.

**Evaluation design.** Used chronological splits, validation-time decision thresholds and AUROC, AUPRC, precision, recall and F1 for event-level evaluation.

## Pipeline

~~~mermaid
flowchart LR
  A[Event Logs] --> B[Chronological Samples]
  B --> C[Text + Structured Features]
  C --> D[TGN Temporal Memory]
  D --> E[Anomaly Scores]
  E --> F[Evaluation]
~~~

Demonstrates event data engineering, multimodal feature fusion and temporal graph model adaptation.

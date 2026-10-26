# Novel Engine · Recoverable Agent Workflow

**Role:** Independent project lead, architecture and engineering  
**Stack:** Python · Model Adapters · SQLite · pytest · GitHub Actions

[Portfolio](../README.en.md) · [Architecture](../docs/system-architecture.md) · [Selected code](../docs/code-gallery.md) · [中文版](novel-engine.md)

## The problem

Long-running agent workflows must coordinate several model tasks while maintaining consistent application state. Novel Engine uses long-form creative production as a demanding application: the system retrieves context, plans actions, generates drafts, extracts structured state changes, runs checks, and presents a review package for approval.

## My responsibilities

**Architecture and domain contracts.** Designed components for character agency, scene planning, generation, evidence extraction, consistency review and canonical story state. Typed contracts manage plan versions, character knowledge and the evidence associated with persistent changes.

**Checkpointed execution.** Built a versioned RunJournal with SHA-256 hashes over input definitions and step artifacts. Execution records preserve completed outputs and support recovery from interrupted stages without repeating already accepted model work.

**Durable state transitions.** Implemented frozen review candidates, approval binding, SQLite transactions, operation locks and commit integrity validation. The architecture keeps the canonical state and exported artifacts consistent across process lifecycles.

**Model interfaces.** Integrated remote model adapters and a local CLI-backed adapter, including structured-output validation, execution records and token/usage accounting.

**Reliability verification.** Developed tests for interruptions, resumed jobs, idempotent commits, file boundary enforcement and review-state consistency.

## Execution pipeline

~~~mermaid
flowchart TD
  A[Author Plan + Canonical State] --> B[Context Retrieval]
  B --> C[Agent Planning]
  C --> D[Model Execution]
  D --> E[Extraction & Validation]
  E --> F[Review Package]
  F --> G[Approved Commit]
  G --> H[(Persistent State)]
  C -.-> J[RunJournal]
  D -.-> J
  E -.-> J
~~~

## Engineering evidence

| Result | Verification |
| --- | --- |
| **544 automated tests passed** | Latest project suite |
| **Windows and Ubuntu** | Cross-platform continuous integration |
| **10-chapter isolated workflow** | End-to-end checkpoint, review and state-commit scenario |

Representative implementations: [workspace boundary validation](../samples/novel-engine/workspace_paths.py) and [durable file I/O](../samples/novel-engine/io_utils.py).

**Core strengths:** agent orchestration, long-task reliability, state management, artifact integrity and software testing.

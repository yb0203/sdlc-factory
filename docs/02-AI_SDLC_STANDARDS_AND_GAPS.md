# 📜 Book 2: AI-SDLC Standards, Manifestos & Gap Audit (`02-AI_SDLC_STANDARDS_AND_GAPS.md`)

## Executive Summary
This document compiles the global industry standards, N-Factor manifestos, regulatory compliance mandates, and gap remediation blueprints governing the **AI-Native Software Development Lifecycle (AI-SDLC)**.

---

## 1. N-Factor Methodologies Matrix

### 1.1 The 12-Factor Agent Methodology (12FA)
*Authored by HumanLayer / Dexter Horthy for production-grade agent reliability:*

1. **JSON Extraction as Foundation**: Treat LLMs primarily as structured data translators.
2. **Own Your Prompts**: Keep prompts explicitly in application code; avoid black-box prompt abstractions.
3. **Manage Context Windows Explicitly**: Actively prune, summarize, and curate context packs.
4. **Tools Are Just JSON & Code**: Treat tool calls as typed outputs validated via deterministic switch/case logic.
5. **Own Your Control Flow**: Keep execution loops (ReAct, OODA) in native application code.
6. **Stateless Agent Design**: Build execution steps to be idempotent and restartable.
7. **Separate Business State from Execution State**: Isolate transactional DB state from agent step history.
8. **Contact Humans as First-Class Operations**: Treat human-in-the-loop routing as a standard tool call.
9. **Small, Focused Agents**: Keep agents bounded to 3–10 steps max; compose small specialized agents.
10. **Explicit Error Handling**: Compact execution errors into the next prompt for closed self-healing loops.

### 1.2 The 16-Factor App for AI (Google Cloud)
- **Factor XIII (Prompts as Code & Specs)**: Version-control prompts, context logic, and golden datasets.
- **Factor XIV (State as a Service)**: Externalize memory and vector state into managed stores.
- **Factor XV (Observability for Non-Determinism)**: Measure semantic drift, token efficiency, and tool accuracy.
- **Factor XVI (Evaluation-Driven CI/CD)**: Enforce automated evaluation regressions against golden datasets.

### 1.3 The 12-Factor AgentOps Framework
- **Phase 1: Prepare**: Context Is Everything (I), Track Everything in Git (II), One Agent One Job (III).
- **Phase 2: Bound**: Enforce Least Privilege (IV), Research Before You Build (V), Isolate Workers (VI).
- **Phase 3: Select**: Validate Externally (VII), Lock Progress Forward (VIII), Extract Learnings (IX).
- **Phase 4: Govern**: Compound Knowledge (X), Supervise Hierarchically (XI), Measure Outcomes (XII).

---

## 2. Regulatory, Compliance & Standards Catalog

### 2.1 ISO/IEC 5338:2023 Compliance
International standard for AI system lifecycle processes. Establishes data readiness checkpoints, role mapping across cross-functional teams (Product Owner, Data Scientist, ML Engineer, DevOps), and traceable deployment decisions.

### 2.2 NIST SP 800-218A & NIST AI 600-1 (Generative AI Profile)
- **Content Provenance**: Track history, origin, modifications, and synthetic outputs via digital watermarking and metadata recording.
- **IP Governance**: Document training data origins and verify code generation against public license registries to mitigate copyright infringement.

### 2.3 EU AI Act Compliance (Annex III & Article 12)
Imposes legally binding obligations on AI software pipelines, including mandatory automatic logging of prompt inputs, model endpoint parameters, and token transaction audit trails.

---

## 3. Gap Analysis & 5 Enterprise Enhancement Modules

Our gap analysis audit identified 5 critical missing capabilities in baseline agent harnesses, remediated via 5 dedicated factory modules:

```
┌────────────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE ENHANCEMENT MODULES                      │
├──────────────────────────┬─────────────────────────────────────────────┤
│ @factory/governance      │ AIBOM generation, EU AI Act audit logger    │
│ @factory/observability   │ OpenTelemetry GenAI spans & drift metrics   │
│ @factory/sre             │ Post-deploy self-healing hotfix triggers    │
│ @factory/wip-control     │ Human review velocity WIP throttling        │
│ @factory/evals           │ Golden benchmark eval dataset CI/CD gate    │
└──────────────────────────┴─────────────────────────────────────────────┘
```

1. **`@factory/governance` (AIBOM & Regulatory Logging)**:
   - Generates cryptographic **AI Bill of Materials (AIBOM)** tracking model version checkpoints, system prompt versions, and tool dependencies per PR.
   - Encrypts EU AI Act compliant audit logs with DSSE cryptographic seals.

2. **`@factory/observability` (OpenTelemetry GenAI Spans)**:
   - Exports OpenTelemetry GenAI semantic conventions (tracing parent agent $\rightarrow$ subagent $\rightarrow$ tool calls).
   - Monitors token efficiency ratios, tool selection accuracy, and semantic drift.

3. **`@factory/sre` (Post-Deploy Self-Healing)**:
   - Monitors production OpenTelemetry alerts and error spikes.
   - Auto-triggers an **Amendment Pipeline (P6)** to generate and test hotfixes autonomously.

4. **`@factory/wip-control` (Human Velocity WIP Throttle & Recursion Guard)**:
   - Throttles agent job queues when open unmerged PR backlogs exceed human review capacity.
   - Enforces strict recursion limits (max 10 steps) and token budgets (max $5.00 per task run).

5. **`@factory/evals` (Golden Benchmark Evaluation CI/CD)**:
   - Runs prompt/agent updates against golden benchmark eval datasets (Braintrust / SWE-bench style) before merging factory configuration changes.

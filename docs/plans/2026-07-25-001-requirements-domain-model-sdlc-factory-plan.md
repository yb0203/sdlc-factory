---
artifact_contract: ce-unified-plan/v1
artifact_readiness: requirements-only
product_contract_source: ce-brainstorm
date: 2026-07-25
---

# Domain-Model Centric SDLC Factory (agy SDK) - Plan

## Executive Summary
The **Domain-Model Centric SDLC Factory** is a **100% domain-agnostic**, AI-native software factory built using the **Google Antigravity (`google-antigravity`) Python SDK**.

The engine operates on a generic **5-Primitive Core Taxonomy**:
1. **Entity**: Structural domain model object (Attributes, State, Schema).
2. **Template**: Parameterized blueprint with `inputSchema`.
3. **Task**: Unit of execution work (code gen, DB migration, test, build, deploy).
4. **Spec**: Declarative system rules/policies AND proposal dual-state (`liveContent` vs `proposedContent`).
5. **Link**: Provably MECE directional relationship edge (Space, Time, Contract, Lifecycle).
*(Plus `Activity` as the immutable event / audit trail log).*

---

## 1. Core Architecture & Design Principles

### 1.1 Templatized Domain Entities
- **Domain Entity Schema**: Entities are defined as abstract templates possessing `inputSchema` (JSON Schema) and `{{placeholder}}` substitution syntax.
- **Nullable Template Foreign Keys**: `templateId = NULL` for ad-hoc items, allowing organic promotion via "Save as Template".

### 1.2 Unified `Spec` Primitive
- Folded `Policy` and `Proposal` into **`Spec`**:
  - `Spec.type`: `BEHAVIOR` | `POLICY` | `SLA` | `CONTRACT` | `SCHEMA`.
  - `Spec.liveContent` vs `Spec.proposedContent`: Dual-state tracking current active rule vs proposed PR/diff.
  - Proposal Actions (`PROPOSE`, `COUNTER`, `ACCEPT`, `REJECT`, `LOCK`) update `proposedContent` without mutating live state until acceptance.

### 1.3 Provably MECE Link Engine
All relationships are governed by a **MECE Link Taxonomy** partitioned across 4 orthogonal dimensions (see [MECE_LINK_ENGINE_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/MECE_LINK_ENGINE_SPEC.md)):
1. **Space ($E_{\text{Space}}$)**: Structural topology (`REQUIRES`, `CONFLICTS`, `COMPOSES`).
2. **Time ($E_{\text{Time}}$)**: Execution scheduling (`SEQUENCE`, `BLOCKS`, `PARALLEL_WITH`).
3. **Contract ($E_{\text{Contract}}$)**: Behavior & Value (`GOVERNS`, `DERIVES_FROM`).
4. **Lifecycle ($E_{\text{Lifecycle}}$)**: Revision evolution (`AMENDS`, `SUPERSEDES`).

### 1.4 Universal Taste Ergonomics (`@factory/ergonomics`)
- 3-tier progressive disclosure UI (Executive Strip $\rightarrow$ Primary Entity Tree $\rightarrow$ Visual Spec Diff View).
- Instant scenario DB seeding (`pnpm db:use <scenario>`) and local auth bypass (`DEV_DISABLE_AUTH_BYPASS`).

### 1.5 agy SDK Multi-Agent Orchestration
- Built directly on `google.antigravity` Python SDK (`Agent`, `LocalAgentConfig`, `CapabilitiesConfig`).
- Multi-agent roles: **Architect / Navigator** $\rightarrow$ **Developer / Transformer** $\rightarrow$ **Verifier / Reviewer**.

---

## 2. Product Boundaries & Non-Goals

### In-Scope
- 100% Domain-Agnostic 5-Primitive SDLC Factory Core powered by `google-antigravity` SDK.
- CLI & GitHub Actions CI/CD runner interface.
- Declarative Domain Entity & Template Compiler (`@factory/core`).
- Provably MECE Polymorphic Link Engine.
- Unified `Spec` & Proposal Engine.
- Universal Ergonomics Engine (`@factory/ergonomics`).
- Universal Activity Audit Logging system.
- DoR / DoD YAML Policy Engine.
- AIBOM & OpenTelemetry GenAI Observability exporters.

### Out-of-Scope (Phase 1)
- Custom Web UI Console (focused exclusively on CLI & CI/CD automation first).

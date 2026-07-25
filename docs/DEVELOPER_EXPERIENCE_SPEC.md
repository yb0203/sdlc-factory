# ⚡ Minimal Universal CLI & Developer Experience (`DEVELOPER_EXPERIENCE_SPEC.md`)

## Executive Summary
The **SDLC Factory CLI** has been collapsed into a **Single Universal Command: `af`** (alias `agy-factory`).

`af` auto-detects context, intent, and project state without requiring developers to remember subcommands:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      MINIMAL UNIVERSAL CLI (`af`)                      │
├───────────────────┬────────────────────────────────────────────────────┤
│ Command           │ Context-Aware Auto-Detected Action                 │
├───────────────────┼────────────────────────────────────────────────────┤
│ 1. `af`           │ Auto-detects directory state:                      │
│                   │ • Empty directory -> Initiates fresh project       │
│                   │ • Codebase exists -> Auto-onboards existing repo   │
├───────────────────┼────────────────────────────────────────────────────┤
│ 2. `af "intent"`  │ Compiles prompt intent directly into:              │
│                   │ `{Delta, Contract, Edge, Proof}` primitives        │
├───────────────────┼────────────────────────────────────────────────────┤
│ 3. `af --prove X` │ Runs Z3 SMT Theorem Prover invariant verification  │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 1. Zero-Subcommand DX Workflows

### Scenario 1: Onboarding an Existing Codebase
```bash
cd /path/to/existing-project
af
```
*Output*: Detects existing stack (Python / Node.js / Docker) and creates `.factory/domain/onboarded_domain.yaml` and `.githooks/pre-commit`.

---

### Scenario 2: Compiling New Feature Intent
```bash
af "Implement payment gateway retry logic with exponential backoff"
```
*Output*: Compiles intent into 2 Deltas, 2 Contracts, 2 Edges, 1 Proof.

---

### Scenario 3: Running Formal Invariant Verification
```bash
af --prove Loan
```
*Output*: Runs Z3 SMT Solver and certifies invariant safety (`fine_cents >= 0`).

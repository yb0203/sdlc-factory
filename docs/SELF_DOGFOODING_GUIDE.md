# 🐕 Self-Dogfooding Guide: Developing sdlc-factory with sdlc-factory (`SELF_DOGFOODING_GUIDE.md`)

## Executive Summary
**Self-Dogfooding** means using the **Domain-Model Centric SDLC Factory** to compile, develop, formally prove, test, and maintain `sdlc-factory` itself.

The `sdlc-factory` repository is its own first domain instance, using its own 5 Core Primitives (`Entity`, `Delta`, `Contract`, `Edge`, `Proof`), `google-antigravity` (`agy`) SDK agents, Git-Native worktrees, Git Notes, and Z3 SMT formal solver gates.

---

## 1. The 5-Step Self-Dogfooding Loop

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SELF-DOGFOODING EXECUTION LOOP                       │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Self-Domain Model (.factory/domain/sdlc_factory.yaml)              │
│    - The factory repository self-describes its own entities in YAML.   │
├────────────────────────────────────────────────────────────────────────┤
│ 2. agy-factory Compile                                                 │
│    - agy Architect Agent compiles new features into Deltas & Contracts.│
├────────────────────────────────────────────────────────────────────────┤
│ 3. Git-Native Worktree Execution (.worktrees/delta-<id>)               │
│    - agy Developer Agent writes Python code in isolated worktrees.     │
│    - Reasoning thoughts logged into Git Notes (refs/notes/activity).   │
├────────────────────────────────────────────────────────────────────────┤
│ 4. Formal Z3 SMT Proof & DoD Gates                                     │
│    - DoR pre-commit hook runs Z3 SMT solver invariant checks.          │
│    - DoD gate runs pytest + Semgrep and seals commit with DSSE tag.    │
├────────────────────────────────────────────────────────────────────────┤
│ 5. Epistemic Compounding (learnings.md)                                │
│    - Failures auto-extract into learnings.md for future prompt packs.  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Step 1: Self-Domain Model (`.factory/domain/sdlc_factory.yaml`)

The factory self-describes its own architecture in `.factory/domain/sdlc_factory.yaml`:

```yaml
apiVersion: factory.domain/v1
kind: EntitySpecification
metadata:
  name: SDLCFactoryEngine
  domain: SDLCFactory
spec:
  attributes:
    version: "0.1.0"
    primitives: ["Entity", "Delta", "Contract", "Edge", "Proof"]
    gitNative: true

  # SELF-REFERENTIAL MECE EDGES
  links:
    - dimension: SPACE
      type: REQUIRES
      target: MECEEdgeEngine
      invariant: "SDLCFactoryEngine requires MECEEdgeEngine for DAG checks."

    - dimension: SPACE
      type: REQUIRES
      target: FormalProofVerifier
      invariant: "SDLCFactoryEngine requires FormalProofVerifier for Z3 SMT math."

    - dimension: CONTRACT
      type: GOVERNS
      target: DefinitionOfDonePolicy
      invariant: "DoD policy governs all PR releases."
```

---

## 3. Step 2: Developing a New Feature via `agy-factory`

When adding a new feature (e.g. "Add OpenTelemetry GenAI Span Exporter"):

```bash
# 1. Compile intent into Deltas, Contracts, Edges, Proofs
agy-factory compile \
  --name "OpenTelemetryExporter" \
  --domain "SDLCFactory" \
  --intent "Export GenAI spans to Datadog/Jaeger"

# 2. Run Z3 SMT Theorem Prover invariant check
agy-factory prove --name "OpenTelemetryExporter"
```

---

## 4. Step 3: Git-Native Agent Worktree Execution

The `google-antigravity` Python SDK agent runner spawns an isolated Git Worktree:

```bash
# Spawn isolated worktree for agent task
agy-factory git spawn-worktree --delta-id "delta-otelp" --branch "delta/otelp-exporter"
```

Inside the worktree, the `agy` agent writes Python code, runs `pytest`, and appends reasoning thoughts into **Git Notes**:

```bash
# Git Notes activity logging
git notes --ref=activity add -m '{"actor": "architect-agent", "thought": "Verifying OpenTelemetry span exporter...", "status": "PASSED"}' HEAD
```

---

## 5. Step 4: DoR Pre-Commit & DoD Verification Gates

### DoR Pre-Commit Hook (`.githooks/pre-commit`)
Before any commit is accepted, the Git pre-commit hook runs:
1. `python3 -m pytest` (100% passing test suite).
2. Z3 SMT Theorem Prover invariant verification.
3. MECE Edge DAG acyclicity check.

```bash
# Setup git hooks
git config core.hooksPath .githooks
```

### DoD Release Gate & DSSE Seal
When opening a PR, independent reviewer agents analyze the diff and attach a signed cryptographic DSSE tag:
```bash
git tag -a v0.2.0-proof-dsse-seal -m "DoD Gates PASSED: Pytest 100% green, Z3 SMT proved, DSSE signed."
```

---

## 6. Step 5: Epistemic Memory Compounding (`learnings.md`)

If any test or Z3 SMT proof fails during development:
1. The `agy` agent extracts the failure root cause.
2. Appends the problem and resolution to `learnings.md`.
3. Subsequent `agy` agent runs automatically ingest `learnings.md` into their system prompt context packs!

# 🐙 Git-Native SDLC Specification (`GIT_NATIVE_SDLC_SPEC.md`)

## Executive Summary
In a **Git-Native SDLC Factory**, Git is not merely a Version Control System for code files. **Git IS the primary database, state engine, multi-agent sandbox, audit log, and cryptographic release ledger.**

Every primitive in our 5-Primitive Core Taxonomy (`Entity`, `Delta`, `Contract`, `Edge`, `Proof`) and `Activity` stream maps directly onto native Git constructs.

---

## 1. Mapping Core Primitives to Native Git Constructs

```
┌────────────────────────────────────────────────────────────────────────┐
│                   GIT-NATIVE SDLC PRIMITIVE MAPPING                    │
├───────────────────┬────────────────────────────────────────────────────┤
│ SDLC Primitive    │ Native Git Construct                               │
├───────────────────┼────────────────────────────────────────────────────┤
│ Entity & Contract │ Tracked `.yaml` / `.json` files in `.zuzu/domain/`  │
│ Delta             │ Isolated Git Worktree (`.worktrees/delta-<id>`)     │
│ Edge              │ DAG relationships declared in YAML / Commit Graph  │
│ Proof             │ Signed Git Tag (`git tag -s`) & DSSE Attestation  │
│ Proposal          │ Git Ref (`refs/proposals/`) & Pull Request Diffs   │
│ Activity Log      │ Git Notes (`git notes --ref=activity`)             │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 2. The 6 Pillars of Git-Native Architecture

### 1. Files & Trees as Domain Entities (`.zuzu/domain/`)
- Domain entities, contracts, and policies live in version-controlled `.yaml` files.
- Any change to an entity or rule is captured as a `git diff`.
- Git commits provide monotonic, cryptographically signed state history out of the box.

### 2. Worktrees as Ephemeral Agent Sandboxes (`.worktrees/delta-<id>`)
- Parallel `agy` SDK agents operate in isolated **Git Worktrees**:
  ```bash
  git worktree add .worktrees/delta-10-fine-calculator -b delta/10-fine-calculator
  ```
- Multiple specialized agents (Architect, Developer, Reviewer) execute concurrently on separate worktrees with **zero file collisions** and zero dirty working directory contamination.

### 3. Git Notes as Immutable Activity Audit Stream (`git notes`)
- Agent reasoning thoughts (`response.thoughts`), tool execution logs, and DoR/DoD check results are appended directly to commits using **Git Notes**:
  ```bash
  git notes --ref=activity add -m '{"actor": "architect-agent", "thought": "Verifying Z3 SMT invariant..."}' HEAD
  ```
- Activity logs travel automatically with `git push` and `git fetch`, eliminating the need for an external logging database.

### 4. Custom Git Refs for Decision & Proposal Dual-State (`refs/proposals/`)
- Proposal state transitions (`PROPOSE` $\rightarrow$ `COUNTER` $\rightarrow$ `ACCEPT` $\rightarrow$ `LOCK`) use light-weight Git Refs:
  ```bash
  # Create a proposal ref
  git update-ref refs/proposals/loan-fine-cap HEAD
  ```
- Un-accepted proposals live cleanly in custom git ref trees without polluting the `main` branch until accepted.

### 5. Git Hooks as Definition of Ready (DoR) Gates
- **Pre-commit / Pre-push Hooks** (`.githooks/pre-commit`): Automatically run Z3 SMT Theorem Provers, Tarjan DAG cycle checks, and JSON Schema validations before allowing commits.

### 6. Signed Git Tags & DSSE Seals as Proof Certificates (`Proof`)
- Release attestations and formal verification proofs are sealed using GPG/SSH signed Git Tags or DSSE attestation blobs stored in `refs/notes/proofs`:
  ```bash
  git tag -s v1.0.0-proof-smt-pass -m "Z3 SMT Invariant Proved & DSSE Signed"
  ```

---

## 3. Git-Native CLI Workflow

```bash
# 1. Initialize Git-Native SDLC Environment
agy-factory git init-hooks

# 2. Spawn Isolated Agent Worktree for a Delta
agy-factory git spawn-worktree --delta-id "delta-10" --branch "delta/fine-calculator"

# 3. Append Agent Reasoning to Git Notes
agy-factory git log-thought --message "Z3 SMT Invariant Proved" --commit HEAD

# 4. Seal DoD Gate with Signed Git Tag
agy-factory git seal-proof --target-id "Loan" --type "DSSE_ECDSA"
```

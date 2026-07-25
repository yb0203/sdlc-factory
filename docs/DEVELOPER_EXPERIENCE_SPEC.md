# 💻 Developer Experience (DX) Specification (`DEVELOPER_EXPERIENCE_SPEC.md`)

## Executive Summary
This document specifies the **Developer Experience (DX)** for both **New Project Initiation** (`agy-factory init`) and **Existing Project Onboarding** (`agy-factory onboard`) within the **Domain-Model Centric SDLC Factory**.

The DX is designed for **zero friction**, **instant feedback**, and **continuous automated verification**.

---

## 1. Scenario 1: Initiating a Brand New Project (`agy-factory init`)

### Developer Workflow

```bash
# 1. Create project directory and run init
mkdir payment-gateway && cd payment-gateway
agy-factory init --name "PaymentGateway" --domain "Fintech" --prompt "Build a Stripe-compatible payment microservice"
```

```
┌────────────────────────────────────────────────────────────────────────┐
│                   NEW PROJECT INITIATION DX PIPELINE                   │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Prompt Ingestion & Domain Synthesis                                 │
│    - agy Architect Agent synthesizes .factory/domain/payment_gateway.yaml│
├────────────────────────────────────────────────────────────────────────┤
│ 2. Universal Entity Compilation                                        │
│    - Compiles initial Deltas, Contracts, Edges, and Z3 SMT Proofs.   │
├────────────────────────────────────────────────────────────────────────┤
│ 3. Git-Native Initialization                                           │
│    - Initializes git repo, creates initial commit, installs .githooks. │
└────────────────────────────────────────────────────────────────────────┘
```

### Generated File Hierarchy
```
payment-gateway/
├── .factory/
│   └── domain/
│       └── payment_gateway.yaml      # Synthesized Domain Specification
├── .githooks/
│   └── pre-commit                    # DoR Z3 SMT & Test verification gate
├── .worktrees/                       # Isolated agent execution sandboxes
├── schemas/
│   └── v1/                           # Non-markdown JSON Schemas & Pydantic models
├── pyproject.toml / package.json
└── README.md
```

---

## 2. Scenario 2: Onboarding an Existing Codebase (`agy-factory onboard`)

### Developer Workflow

```bash
# 1. Navigate to existing repository root
cd /path/to/existing-codebase

# 2. Run automated onboarding scanner
agy-factory onboard
```

```
┌────────────────────────────────────────────────────────────────────────┐
│               EXISTING PROJECT ONBOARDING DX PIPELINE                  │
├────────────────────────────────────────────────────────────────────────┤
│ 1. AST & Schema Scanner (agy Researcher Agent)                         │
│    - Scans package.json, pyproject.toml, Prisma/SQL schemas, OpenAPI.  │
├────────────────────────────────────────────────────────────────────────┤
│ 2. Domain Model Extraction                                             │
│    - Reconstructs existing domain entities into .factory/domain/*.yaml. │
├────────────────────────────────────────────────────────────────────────┤
│ 3. Baseline Contract & Proof Generation                                │
│    - Generates Contracts (API specs, SLAs) and Z3 SMT invariants.      │
├────────────────────────────────────────────────────────────────────────┤
│ 4. Git-Native Retrofitting                                             │
│    - Installs Git Notes logging (refs/notes/activity) & .githooks.    │
└────────────────────────────────────────────────────────────────────────┘
```

### Onboarding Output Example
```
🔍 Scanning existing codebase at /Users/hkc/projects/existing-app...
✅ Detected Tech Stack: Python 3.12 + FastAPI + PostgreSQL + SQLAlchemy
✅ Extracted 5 Domain Entities -> Generated .factory/domain/onboarded_domain.yaml
✅ Extracted 12 API Routes -> Generated 12 Contract specs
✅ Configured Z3 SMT Invariant Verification for DB schema
✅ Installed DoR pre-commit hook (.githooks/pre-commit)

Your existing project is now 100% SDLC Factory Onboarded!
Run `agy-factory status` to view your project domain matrix.
```

---

## 3. Comparative DX Summary Matrix

| Metric / Dimension | Scenario 1: New Project Initiation (`init`) | Scenario 2: Existing Project Onboarding (`onboard`) |
|:---|:---|:---|
| **Time to Ready** | **< 10 seconds** | **< 30 seconds** |
| **Command** | `agy-factory init --name <name> --prompt <intent>` | `agy-factory onboard` |
| **Domain Spec Source** | Synthesized by `agy` Architect Agent from prompt intent. | Reverse-engineered from AST, DB Schemas, & API code. |
| **Existing Code Risk** | Zero (fresh directory). | Zero (adds `.factory/` metadata without mutating source code). |
| **Git Integration** | Runs `git init` and initial commit. | Retrofits Git Notes (`refs/notes/activity`) into existing history. |
| **Verification Gate** | Fresh DoR/DoD quality gates. | Baseline DoR/DoD quality gates matching current test suite. |

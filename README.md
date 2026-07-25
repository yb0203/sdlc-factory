# 🏛️ SDLC Factory (agy SDK)

> **Domain-Model Centric, AI-Native Software Factory powered by the Google Antigravity (`google-antigravity`) Python SDK.**

---

## 🌟 Overview

The **SDLC Factory** is a 100% domain-agnostic, AI-native software delivery engine. It shifts software development from manual keystroke typing to **Intent-Driven Orchestration**, using **Templatized Domain Entities**, a **Provably MECE Edge Engine**, a **Dual-Faceted Proof Engine**, and **Universal Taste Ergonomics**.

---

## 🔬 Provably Complete 6-Primitive Taxonomy

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PROVABLY COMPLETE 6-PRIMITIVE TAXONOMY               │
├───────────────┬────────────────────────────────────────────────────────┤
│ 1. Entity     │ Structural domain object (Attributes, State, Schema)   │
│ 2. Delta      │ Unit of executable state mutation (work, codegen, test)│
│ 3. Contract   │ Declarative rule/policy AND proposal dual-state        │
│ 4. Edge       │ MECE graph edge (Space, Time, Contract, Lifecycle)     │
│ 5. Proof      │ Mathematical formal verification & Cryptographic seal  │
└───────────────┴────────────────────────────────────────────────────────┘
```
*(Plus `Activity` as the immutable audit event log stream).*

---

## 🚀 Quickstart

### 1. Installation
```bash
# Clone repository
git clone https://github.com/your-org/sdlc-factory.git
cd sdlc-factory

# Install in editable mode
pip install -e .
```

### 2. Compile a Domain Entity
```bash
agy-factory compile --name "Loan" --domain "LibraryManagement" --intent "Overdue fine calculation"
```

### 3. Formal Invariant Proof Verification
```bash
agy-factory prove --name "Loan"
```

### 4. Run Test Suite
```bash
pytest
```

---

## ⚙️ Machine-Readable Schema Registry (`schemas/v1/`)

All core primitives are backed by non-markdown, strongly-typed machine-readable specification files:
- 📄 JSON Schemas in [`schemas/v1/*.schema.json`](schemas/v1/)
- 🐍 Python Pydantic models in [`schemas/v1/models.py`](schemas/v1/models.py)

```python
from schemas.v1 import Entity, Delta, Contract, Edge, Proof

# Used directly for google-antigravity structured outputs
```

---

## 📖 Complete Documentation Suite (`docs/`)

Explore the full documentation hub in [`docs/README.md`](docs/README.md):
- 🏛️ **[Book 1: System Architecture](docs/01-ARCHITECTURE_SPEC.md)**
- 📜 **[Book 2: AI-SDLC Standards & Gap Audit](docs/02-AI_SDLC_STANDARDS_AND_GAPS.md)**
- 💻 **[Book 3: System Walkthrough & agy SDK Guide](docs/03-SYSTEM_WALKTHROUGH.md)**
- 📐 **[MECE Edge Engine Specification](docs/MECE_LINK_ENGINE_SPEC.md)**
- 🔬 **[Proof Primitive Specification](docs/PROOF_PRIMITIVE_SPEC.md)**
- 🎨 **[Opinionated Frameworks Specification](docs/OPINIONATED_FRAMEWORKS_SPEC.md)**
- 🔍 **[Zuzuu Studio Retrospective Analysis](docs/ZUZUU_STUDIO_RETROSPECTIVE_MISSES.md)**
- 🏛️ **[ADR-001: Nullable Template FKs](docs/ADR_001_NULLABLE_TEMPLATE_FKS.md)**
- 🏛️ **[ADR-002: Eliminating Template Primitive](docs/ADR_002_WHY_NO_TEMPLATE_PRIMITIVE.md)**

---

## 📄 License
MIT License

# 📖 Domain-Model Centric SDLC Factory Documentation Hub

Welcome to the **Domain-Model Centric SDLC Factory** documentation suite. The architecture, standards, proofs, retrospective analysis, ADRs, compiler patterns, Git-Native engine, and opinionated human frameworks are compiled into a clean specification set:

---

## 🐙 Git-Native Architecture Specification
📄 **[GIT_NATIVE_SDLC_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/GIT_NATIVE_SDLC_SPEC.md)**
- **Git Trees & Files**: Domain entities & specs in `.zuzu/domain/*.yaml`.
- **Git Worktrees**: Ephemeral agent sandboxes (`.worktrees/delta-<id>`).
- **Git Notes (`git notes`)**: Immutable Activity audit stream (`refs/notes/activity`).
- **Git Custom Refs (`refs/proposals/`)**: Decision & Proposal dual-state (`liveContent` vs `proposedContent`).
- **Git Hooks**: DoR pre-commit validation gates (Z3 SMT solver proofs).
- **Signed Git Tags**: Cryptographic DSSE attestation seals (`Proof`).

---

## ⚙️ Machine-Readable Schema Registry (`schemas/v1/`)

Non-markdown, strongly-typed machine-readable specification files for `google-antigravity` (`agy`) Python SDK structured outputs and tool validations:

| Primitive | JSON Schema File | Python Pydantic Model |
|:---|:---|:---|
| **`Entity`** | 📄 [`entity.schema.json`](file:///Users/hkc/Documents/software-factory/schemas/v1/entity.schema.json) | 🐍 [`models.py:Entity`](file:///Users/hkc/Documents/software-factory/schemas/v1/models.py#L25-L35) |
| **`Delta`** | 📄 [`delta.schema.json`](file:///Users/hkc/Documents/software-factory/schemas/v1/delta.schema.json) | 🐍 [`models.py:Delta`](file:///Users/hkc/Documents/software-factory/schemas/v1/models.py#L52-L65) |
| **`Contract`** | 📄 [`contract.schema.json`](file:///Users/hkc/Documents/software-factory/schemas/v1/contract.schema.json) | 🐍 [`models.py:Contract`](file:///Users/hkc/Documents/software-factory/schemas/v1/models.py#L82-L93) |
| **`Edge`** | 📄 [`edge.schema.json`](file:///Users/hkc/Documents/software-factory/schemas/v1/edge.schema.json) | 🐍 [`models.py:Edge`](file:///Users/hkc/Documents/software-factory/schemas/v1/models.py#L125-L133) |
| **`Proof`** | 📄 [`proof.schema.json`](file:///Users/hkc/Documents/software-factory/schemas/v1/proof.schema.json) | 🐍 [`models.py:Proof`](file:///Users/hkc/Documents/software-factory/schemas/v1/models.py#L156-L167) |
| **`Activity`** | 📄 [`activity.schema.json`](file:///Users/hkc/Documents/software-factory/schemas/v1/activity.schema.json) | 🐍 [`models.py:Activity`](file:///Users/hkc/Documents/software-factory/schemas/v1/models.py#L186-L195) |

---

## 📚 Documentation Core

| Book / Spec | Document | Purpose & Scope |
|:---|:---|:---|
| **Book 1** | 🏛️ **[01-ARCHITECTURE_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/01-ARCHITECTURE_SPEC.md)** | **Complete System Architecture & Specification**<br>Provably Minimal 5-Primitive Core Taxonomy (`Entity`, `Delta`, `Contract`, `Edge`, `Proof`), Prototypal Cloning, MECE Edge Engine, Pure Pipeline Functions (P1–P6), DoR/DoD Quality Gates, and `learnings.md` Memory Flywheel. |
| **Book 2** | 📜 **[02-AI_SDLC_STANDARDS_AND_GAPS.md](file:///Users/hkc/Documents/software-factory/docs/02-AI_SDLC_STANDARDS_AND_GAPS.md)** | **AI-SDLC Standards, Manifestos & Enterprise Gap Audit**<br>12-Factor Agent Methodology (12FA), 16-Factor AI Apps, 12-Factor AgentOps, ISO/IEC 5338:2023, EU AI Act compliance, AIBOM generation, OpenTelemetry GenAI Observability, and Agent WIP Throttling. |
| **Book 3** | 💻 **[03-SYSTEM_WALKTHROUGH.md](file:///Users/hkc/Documents/software-factory/docs/03-SYSTEM_WALKTHROUGH.md)** | **System Walkthrough & agy SDK Integration Guide**<br>Step-by-step concrete execution walkthrough for a Library Management System, `google-antigravity` Python SDK agent runner code, real-time thought/tool streaming, and DSSE signed PR flow. |
| **Git-Native** | 🐙 **[GIT_NATIVE_SDLC_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/GIT_NATIVE_SDLC_SPEC.md)** | **Git-Native SDLC Specification**<br>Mapping SDLC primitives to native Git constructs: Git Trees/Files, Worktrees as Agent Sandboxes, Git Notes as Activity log, Custom Git Refs for proposals, and Signed Git Tags as Proofs. |
| **Nomenclature** | 🔤 **[PROJECTION_UNITS_NOMENCLATURE_COMPARISON.md](file:///Users/hkc/Documents/software-factory/docs/PROJECTION_UNITS_NOMENCLATURE_COMPARISON.md)** | **Compiler Nomenclature Paradigm**<br>Selected Option B: Compiler Theory & Phoenix Math Nomenclature (`Delta`, `Contract`, `Edge`, `Proof`). |
| **Compiler** | 🧬 **[ENTITY_PROJECTION_COMPILER_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/ENTITY_PROJECTION_COMPILER_SPEC.md)** | **Universal Entity Projection Compiler Specification**<br>Formal SDLC terminology for entity-to-entity compilation (Model-to-Model Transformation, Multi-Domain Entity Projection, Intent Projection Engine), and multi-domain projection examples across DevOps, Fintech, Games, and CLM. |
| **MECE Proof** | 📐 **[MECE_PROJECTION_UNITS_PROOF.md](file:///Users/hkc/Documents/software-factory/docs/MECE_PROJECTION_UNITS_PROOF.md)** | **Mathematical Proof of MECE Projection Units**<br>Formal mathematical proof of pairwise disjointness and collective exhaustiveness for compiler projection units (`{Delta, Contract, Edge, Proof}`). |
| **ADR-001** | 🏛️ **[ADR_001_NULLABLE_TEMPLATE_FKS.md](file:///Users/hkc/Documents/software-factory/docs/ADR_001_NULLABLE_TEMPLATE_FKS.md)** | **ADR-001: Nullable Template FKs & Ad-Hoc Entities**<br>Architectural Decision Record explaining why `templateId` is nullable. |
| **ADR-002** | 🏛️ **[ADR_002_WHY_NO_TEMPLATE_PRIMITIVE.md](file:///Users/hkc/Documents/software-factory/docs/ADR_002_WHY_NO_TEMPLATE_PRIMITIVE.md)** | **ADR-002: Eliminating the Template Primitive**<br>Architectural Decision Record for eliminating `Template` as a primitive class in favor of Prototype-Based Cloning & Direct LLM Agent Synthesis (5 Pure Primitives). |
| **Proof Spec** | 🔬 **[PROOF_PRIMITIVE_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/PROOF_PRIMITIVE_SPEC.md)** | **The Proof Primitive Specification**<br>Dual-Faceted Proof Engine: Formal Mathematical Proofs (Z3 SMT Solver Invariants, MECE proofs, Tarjan DAG acyclicity) + Cryptographic Attestation Proofs (DSSE Seals, AIBOM Hashes), and `agy` agent auto-repair resolution loops. |
| **Opinionated** | 🎨 **[OPINIONATED_FRAMEWORKS_SPEC.md](file:///Users/hkc/Documents/software-factory/docs/OPINIONATED_FRAMEWORKS_SPEC.md)** | **Opinionated Decision Protocols & Taste Ergonomics**<br>Generic proposal state machine (`PROPOSE`, `COUNTER`, `ACCEPT`, `LOCK`), soft vs hard guardrails, 3-tier progressive disclosure UI, visual spec diffs, and developer experience (DX) test scenarios. |
| **Retrospective** | 🔍 **[ZUZUU_STUDIO_RETROSPECTIVE_MISSES.md](file:///Users/hkc/Documents/software-factory/docs/ZUZUU_STUDIO_RETROSPECTIVE_MISSES.md)** | **Retrospective: What Would Have Been Missed on Zuzuu Studio**<br>Deep analysis of what domain rules (financial rate cards, margin math), negotiation dynamics (P3 redline loop), human UX taste, tacit knowledge, and API token scoping would be missed without human architectural direction. |

---

## 📂 Source Manifestos & References

Original PDF source material located in [`docs/references/`](file:///Users/hkc/Documents/software-factory/docs/references/):
- 📄 [AI Development Manifestos and Frameworks.pdf](file:///Users/hkc/Documents/software-factory/docs/references/AI%20Development%20Manifestos%20and%20Frameworks.pdf)
- 📄 [AI-Native Development Standards.pdf](file:///Users/hkc/Documents/software-factory/docs/references/AI-Native%20Development%20Standards.pdf)

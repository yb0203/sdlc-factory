# 🏛️ Book 1: Domain-Agnostic System Architecture (`01-ARCHITECTURE_SPEC.md`)

## Executive Overview
The **Domain-Model Centric SDLC Factory** is a **100% domain-agnostic**, AI-native software factory built using the **Google Antigravity (`google-antigravity`) Python SDK**.

The factory operates on a **Single Source of Truth (SSOT)** comprising a **Provably Minimal 5-Primitive Core Taxonomy**:
1. **Entity**: Structural domain model object (Attributes, State, Schema, Prototypal Cloning via `isPrototype`).
2. **Delta**: Unit of executable state mutation (code gen, DB migration, test, build, deploy).
3. **Contract**: Declarative system rules/policies AND proposal dual-state (`liveContent` vs `proposedContent`) across 4 provably MECE facets (`BEHAVIOR`, `CONTRACT`, `POLICY`, `OPERATIONAL`).
4. **Edge**: Provably MECE directional relationship graph edge (Space, Time, Contract, Lifecycle).
5. **Proof**: Mathematical formal verification (SMT/DAG/MECE) AND cryptographic attestation seal (DSSE/AIBOM).
*(Plus `Activity` as the immutable audit event log stream).*

---

## 1. Provably Minimal 5-Primitive Core Taxonomy

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PROVABLY MINIMAL 5-PRIMITIVE TAXONOMY                │
├───────────────┬────────────────────────────────────────────────────────┤
│ 1. Entity     │ Structural domain object (Attributes, State, Schema)   │
│ 2. Delta      │ Unit of executable state mutation (work, codegen, test)│
│ 3. Contract   │ Declarative rule/policy AND proposal dual-state        │
│ 4. Edge       │ MECE graph edge (Space, Time, Contract, Lifecycle)     │
│ 5. Proof      │ Mathematical formal verification & Cryptographic seal  │
└───────────────┴────────────────────────────────────────────────────────┘
```

### 1.1 Compiler Theory Nomenclature (Option B)
The 4 Projection Units emitted when compiling an `Entity` use formal Compiler & Phoenix Math nomenclature:
- **`Delta`**: Executable work state mutation ($\text{Desired State} = \text{Current State} + \text{Delta}$).
- **`Contract`**: Declarative boundary rules, API schemas, DoR/DoD policies, and SLAs.
- **`Edge`**: Directional graph relationship edges across Space, Time, Contract, and Lifecycle dimensions.
- **`Proof`**: Mathematical formal verification (Z3 SMT solver invariants) and cryptographic seals (DSSE/AIBOM).

---

## 2. Provably MECE Edge Engine: Domain-Declared, Engine-Enforced

All relationships are governed by a **Mutually Exclusive, Collectively Exhaustive (MECE)** edge taxonomy partitioned across 4 orthogonal dimensions:

$$E = E_{\text{Space}} \cup E_{\text{Time}} \cup E_{\text{Contract}} \cup E_{\text{Lifecycle}}$$

```
                                  ┌──────────────────────────────────┐
                                  │       MECE EDGE ENGINE           │
                                  └────────────────┬─────────────────┘
                                                   │
        ┌──────────────────────┬───────────────────┴───────────────────┬──────────────────────┐
        │                      │                                       │                      │
        ▼                      ▼                                       ▼                      ▼
┌──────────────┐       ┌──────────────┐                        ┌──────────────┐       ┌──────────────┐
│   1. SPACE   │       │   2. TIME    │                        │ 3. CONTRACT  │       │4. LIFECYCLE  │
│ (Structural) │       │ (Temporal)   │                        │   (Value)    │       │ (Mutation)   │
├──────────────┤       ├──────────────┤                        ├──────────────┤       ├──────────────┤
│ REQUIRES     │       │ SEQUENCE     │                        │ GOVERNS      │       │ AMENDS       │
│ CONFLICTS    │       │ BLOCKS       │                        │ DERIVES_FROM │       │ SUPERSEDES   │
│ COMPOSES     │       │ PARALLEL_WITH│                        │              │       │              │
└──────────────┘       └──────────────┘                        └──────────────┘       └──────────────┘
```

1. **Space Dimension ($E_{\text{Space}}$)**: `REQUIRES`, `CONFLICTS`, `COMPOSES`.
2. **Time Dimension ($E_{\text{Time}}$)**: `SEQUENCE`, `BLOCKS`, `PARALLEL_WITH`.
3. **Contract Dimension ($E_{\text{Contract}}$)**: `GOVERNS`, `DERIVES_FROM`.
4. **Lifecycle Dimension ($E_{\text{Lifecycle}}$)**: `AMENDS`, `SUPERSEDES`.

---

## 3. Dual-Faceted `Proof` Primitive Architecture

A `Proof` is a verifiable certificate of system correctness:

```
                                  ┌──────────────────────────────────┐
                                  │         DUAL-FACETED PROOF       │
                                  └────────────────┬─────────────────┘
                                                   │
                        ┌──────────────────────────┴──────────────────────────┐
                        │                                                     │
                        ▼                                                     ▼
        ┌───────────────────────────────┐                     ┌───────────────────────────────┐
        │  1. FORMAL MATHEMATICAL PROOF │                     │ 2. CRYPTOGRAPHIC ATTESTATION  │
        │   (Pre-Execution / Compile)   │                     │    (Post-Execution / Release) │
        ├───────────────────────────────┤                     ├───────────────────────────────┤
        │ - Z3 SMT Solver Invariants    │                     │ - DSSE Cryptographic Seals    │
        │ - MECE Partition Proofs       │                     │ - AIBOM Merkle Lineage Hashes │
        │ - Tarjan DAG Acyclicity       │                     │ - Multi-Agent Review Sign-off │
        └───────────────────────────────┘                     └───────────────────────────────┘
```

---

## 4. Universal Proposal State Machine on `Contract`

```
         ┌─────────────────────────────────────────────────┐
         │  contract.liveContent = "replicas: 2"            │
         │  contract.proposedContent = null                │
         │  contract.proposalStatus = NONE                 │
         └─────────────────────────────────────────────────┘
                           │
              PROPOSE("replicas: 5")
                           │
         ┌─────────────────────────────────────────────────┐
         │  contract.liveContent = "replicas: 2"  (live)   │
         │  contract.proposedContent = "replicas: 5"       │
         │  contract.proposalStatus = PROPOSED             │
         └─────────────────────────────────────────────────┘
          │                   │                    │
        ACCEPT             REJECT             COUNTER("replicas: 3")
          │                   │                    │
    liveContent = proposed proposedContent = null proposedContent = "replicas: 3"
    proposedContent = null proposalStatus = NONE  proposalStatus = COUNTERED
    proposalStatus = NONE     │
          │                 LOCK
          │                   │
          └──────────────────►│ proposalStatus = LOCKED
```

---

## 5. Pure Functional Pipelines & Execution Engine

Macro-workflows are structured as **100% pure functions** emitting typed `Command[]` payloads:
- **P1 `intakePipeline`**: Initializes ownership hierarchy (`Account`, `Project`).
- **P2 `buildProject`**: Compiles parameters and entities into concrete graphs.
- **P3 `proposalPipeline`**: Manages proposal state changes (`PROPOSE`, `COUNTER`, `ACCEPT`, `REJECT`, `LOCK`).
- **P4 `activationPipeline`**: Signs contracts; activates root DAG Delta steps (`SEQUENCE`).
- **P5 `executionPipeline`**: Handles Delta completions and DAG successor activations.
- **P6 `amendmentPipeline`**: Manages post-activation scope changes by creating linked `Draft` projects (`AMENDS`).

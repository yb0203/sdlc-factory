# 🧬 Universal Entity Projection Compilation (`ENTITY_PROJECTION_COMPILER_SPEC.md`)

## Executive Summary
In Zuzuu Studio, a single high-level `Deliverable` entity passes through a compiler (`compiler/space.ts`) to project and generate derived `Task` records (work domain) and `Term` records (legal/spec domain).

This document explores how this **Entity-to-Entity Compiler-Driven Generation Engine** works, its formal names in SDLC software engineering literature, and the **mathematical proof of MECE projection units**.

---

## 1. What Is This Pattern Called in SDLC Literature?

Across software architecture, compiler theory, and Model-Driven Engineering (MDE), this pattern is known by four formal names:

```
┌────────────────────────────────────────────────────────────────────────┐
│               FORMAL SDLC TERMINOLOGY FOR THE PATTERN                  │
├───────────────────────────────────┬────────────────────────────────────┤
│ 1. Model-to-Model (M2M) Transform │ Formal MDE term for compiling a    │
│    (Model-Driven Architecture)    │ Platform-Independent Model (PIM)   │
│                                   │ into Platform-Specific Tasks/Specs.│
├───────────────────────────────────┼────────────────────────────────────┤
│ 2. Multi-Domain Entity Projection │ Compiling a single source entity   │
│    (Aspect-Oriented Architecture) │ across orthogonal domains (Work,   │
│                                   │ Contract, Infrastructure, Proofs). │
├───────────────────────────────────┼────────────────────────────────────┤
│ 3. Intent Projection Engine       │ Modern AI-SDLC term for compiling  │
│    (Spec-Driven Development)      │ declarative intent into execution  │
│                                   │ Work Breakdown Structures (WBS).   │
├───────────────────────────────────┼────────────────────────────────────┤
│ 4. Derivation Graph Compilation   │ Graph theory term for generating   │
│    (Graph Compiler Theory)        │ child nodes and edges from a parent│
│                                   │ root node.                         │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 2. Mathematical Proof of MECE Projection Units

The compiler engine projects any source domain entity $E_{\text{in}}$ across **four provably MECE projection units** (see [MECE_PROJECTION_UNITS_PROOF.md](file:///Users/hkc/Documents/software-factory/docs/MECE_PROJECTION_UNITS_PROOF.md)):

$$P = P_{\text{Task}} \cup P_{\text{Spec}} \cup P_{\text{Link}} \cup P_{\text{Proof}}$$

$$\text{where } \forall i \neq j, P_i \cap P_j = \emptyset$$

```
┌────────────────────────────────────────────────────────────────────────┐
│               UNIVERSAL ENTITY PROJECTION PIPELINE                     │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                           Source Domain Entity
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │ ENTITY PROJECTION COMPILER ENGINE│
                 │      (@factory/compiler)         │
                 └─────────────────┬────────────────┘
                                   │
        ┌──────────────────┬───────┴──────────┬──────────────────┐
        │                  │                  │                  │
        ▼                  ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  Work Tasks  │   │ Behavior Spec│   │ MECE Links   │   │ Formal Proof │
│ (Execution)  │   │  (Contract)  │   │ (Graph Edge) │   │(Verification)│
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

1. **`Task` (Execution Work)**: State mutations, codegen, DB migrations, build/test jobs.
2. **`Spec` (Declarative Constraint)**: DoR/DoD policies, API schemas, SLAs across 4 facets (`BEHAVIOR`, `CONTRACT`, `POLICY`, `OPERATIONAL`).
3. **`Link` (Graph Relationship Edge)**: Directional MECE edges (`Space`, `Time`, `Contract`, `Lifecycle`).
4. **`Proof` (Formal Verification)**: Z3 SMT solver invariant proofs, Tarjan DAG acyclicity proofs, DSSE cryptographic seals.

---

## 3. Universal Applicability Across Domains

This pattern is **100% universal**. Any high-level domain entity in any industry can be compiled into its constituent MECE projection units:

| Industry Domain | Source Entity | Work Projection (`Task`) | Contract Projection (`Spec`) | Graph Edge (`Link`) | Formal Verification (`Proof`) |
|:---|:---|:---|:---|:---|:---|
| **DevOps / IaC** | `Microservice` | 1. Helm Chart<br>2. K8s Pods | 1. RAM $\le 2\text{GB}$<br>2. Healthcheck | `Microservice REQUIRES DB` | SMT Proof: Memory Quota safe |
| **Fintech / Payments** | `PaymentGate` | 1. Stripe Adapter<br>2. Migration | 1. PCI-DSS Rule<br>2. Idempotency | `Gate GOVERNS Transaction` | SMT Proof: No double spend |
| **Library System** | `Loan` | 1. Checkout Task<br>2. Fine Task | 1. $1/day Penalty<br>2. Max $50 Cap | `Loan REQUIRES Member` | SMT Proof: `fineCents >= 0` |
| **Game Engineering** | `PlayerSkill` | 1. Cooldown Task<br>2. Mana Math | 1. Mana $\ge 50$<br>2. Cooldown $10\text{s}$ | `Skill REQUIRES Character` | SMT Proof: Mana non-negative |
| **Legal / CLM (Plugin)**| `Deliverable` | 1. DNS Setup<br>2. SSL Cert | 1. SLA: 24h<br>2. Net 30 Days | `Deliverable SEQUENCE Deploy` | DSSE Seal: Signed SOW diff |

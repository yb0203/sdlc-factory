# 🔬 The `Proof` Primitive Specification (`PROOF_PRIMITIVE_SPEC.md`)

## Executive Summary
In the **Domain-Model Centric SDLC Factory**, correctness is not left to empirical guesswork. **`Proof`** is established as a **first-class core primitive**, elevating software verification to formal mathematical proof and cryptographic attestation.

---

## 1. The 6-Primitive Core Architecture

With `Proof` formalized as a core primitive, the SDLC Factory operates on a **Provably Complete 6-Primitive Core Taxonomy**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PROVABLY COMPLETE 6-PRIMITIVE TAXONOMY               │
├───────────────┬────────────────────────────────────────────────────────┤
│ 1. Entity     │ Structural domain object (Attributes, State, Schema)   │
│ 2. Template   │ Parameterized blueprint with inputSchema               │
│ 3. Task       │ Unit of execution work (code gen, migration, test)     │
│ 4. Spec       │ Declarative rule/policy AND proposal dual-state        │
│ 5. Link       │ MECE directional edge (Space, Time, Contract, Lifecycle)│
│ 6. Proof      │ Mathematical formal verification & Cryptographic seal  │
└───────────────┴────────────────────────────────────────────────────────┘
```
*(Plus `Activity` as the immutable event / audit trail log stream).*

---

## 2. Dual-Faceted Proof Engine Architecture

A `Proof` is a **verifiable certificate of system correctness** possessing two complementary facets:

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

### 2.1 Facet 1: Formal Mathematical Proof (DoR / Compile Time)
Executed before code generation or codebase mutation begins:
1. **MECE Partition Proof**: Validates $S_i \cap S_j = \emptyset$ and $\bigcup S_i = S$ for all domain spec classifications.
2. **DAG Acyclicity Proof**: Executes Tarjan's / Kahn's algorithms on `REQUIRES` and `SEQUENCE` links to certify zero circular dependencies.
3. **SMT Invariant Safety Proof**: Runs a Z3 SMT Theorem Prover to prove that the state transition $\text{Desired State} = \text{Current State} + \text{Delta}$ preserves all domain invariants (e.g., `balance >= 0`, `fineCents >= 0`).

### 2.2 Facet 2: Cryptographic Attestation Proof (DoD / Release Time)
Executed after sandbox execution and testing complete:
1. **DSSE Cryptographic Seal**: ECDSA/Ed25519 digital signature sealing the commit diff, test logs, and reviewer agent approvals.
2. **AIBOM Merkle Provenance Hash**: SHA-256 Merkle root hash linking prompt templates, model checkpoints, context packs, and generated files.

---

## 3. Polymorphic `Proof` Schema

```typescript
export enum ProofFacet {
  FORMAL_MATHEMATICAL = 'FORMAL_MATHEMATICAL', // SMT / DAG / MECE Proofs
  CRYPTOGRAPHIC_SEAL = 'CRYPTOGRAPHIC_SEAL'   // DSSE / AIBOM Signatures
}

export enum ProofStatus {
  PROVING = 'PROVING',
  PROVED = 'PROVED',
  DISPROVED = 'DISPROVED',
  ESCALATED = 'ESCALATED'
}

export interface Proof {
  id: string;
  facet: ProofFacet;
  targetId: string;            // Entity, Spec, Task, or Project ID
  
  // Formal Solver / Seal Metrics
  solverEngine?: 'Z3_SMT' | 'TARJAN_DAG' | 'DSSE_ECDSA' | 'AIBOM_MERKLE';
  theoremExpression?: string;   // Formal logic expression or invariant
  counterExample?: string;     // Counter-example if DISPROVED
  signatureSeal?: string;      // DSSE cryptographic signature string
  
  status: ProofStatus;
  createdAt: Date;
}
```

---

## 4. `agy` SDK Agent Proof Failure Resolution Loop

When a formal mathematical proof is disproved (`DISPROVED`) during compilation:

```
┌─────────────────┐      Disproved      ┌──────────────────┐
│ Compile & Prove │ ──────────────────► │ agy Agent Auto-  │
│ (Z3 SMT Solver) │                     │ Repair Attempt   │
└────────┬────────┘                     └────────┬─────────┘
         │                                       │
      PROVED                                Iteration <= 3
         │                                       │
         ▼                                       ▼
┌─────────────────┐                     ┌──────────────────┐
│ Proceed to Code │                     │ Re-run Solver &  │
│ Generation      │ ◄────────────────── │ Verify Proof     │
└─────────────────┘        PROVED       └────────┬─────────┘
                                                 │
                                           Max Iterations
                                             Exceeded
                                                 │
                                                 ▼
                                        ┌──────────────────┐
                                        │ Extract Counter- │
                                        │ Example into     │
                                        │ learnings.md     │
                                        └────────┬─────────┘
                                                 │
                                                 ▼
                                        ┌──────────────────┐
                                        │ Escalate to      │
                                        │ Human Architect  │
                                        └──────────────────┘
```

1. **Auto-Repair (Max 3 Iterations)**: The `agy` Architect Agent ingests the SMT solver's counter-example, adjusts the `Spec` proposal, and re-submits to the solver.
2. **Epistemic Extraction**: If unresolved after 3 iterations, the counter-example is automatically extracted into `learnings.md` (*"Learning 044: SMT solver disproved fine calculation due to potential integer overflow"*).
3. **Human Escalation**: The task transitions to `ESCALATED`, alerting the human architect with the precise mathematical counter-example.

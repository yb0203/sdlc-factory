# 🎨 Unified Spec & Decision Protocol (`OPINIONATED_FRAMEWORKS_SPEC.md`)

## Executive Summary
By folding `Policy` and `Proposal` into a single core primitive—**`Spec`**—and structuring `Spec.type` across 4 orthogonal facets, the SDLC Factory achieves a **provably MECE specification model**.

---

## 1. Mathematical Proof of MECE for `Spec.type`

Let $S$ be the universe of all possible specifications, rules, constraints, contracts, and policies in any software system.

We define `Spec.type` across **four orthogonal facets**:

$$S = S_{\text{Behavior}} \cup S_{\text{Contract}} \cup S_{\text{Policy}} \cup S_{\text{Operational}}$$

```
                                  ┌──────────────────────────────────┐
                                  │       PROVABLY MECE SPEC         │
                                  └────────────────┬─────────────────┘
                                                   │
        ┌──────────────────────┬───────────────────┴───────────────────┬──────────────────────┐
        │                      │                                       │                      │
        ▼                      ▼                                       ▼                      ▼
┌──────────────┐       ┌──────────────┐                        ┌──────────────┐       ┌──────────────┐
│ 1. BEHAVIOR  │       │ 2. CONTRACT  │                        │  3. POLICY   │       │4.OPERATIONAL │
│ (Functional) │       │ (Interface)  │                        │  (Quality)   │       │(Environment) │
├──────────────┤       ├──────────────┤                        ├──────────────┤       ├──────────────┤
│ Domain Invar.│       │ API Schemas  │                        │ DoR / DoD    │       │ IaC / Scal.  │
│ Scenarios    │       │ DB Schemas   │                        │ Security Gate│       │ Resource RAM │
│ Gherkin      │       │ Event Struct │                        │ Coverage SLA │       │ Cloud Limits │
└──────────────┘       └──────────────┘                        └──────────────┘       └──────────────┘
```

### 1.1 Proof of Mutual Exclusivity (ME)
To prove Mutual Exclusivity, we demonstrate that $\forall i, j \in \{\text{Behavior}, \text{Contract}, \text{Policy}, \text{Operational}\}, i \neq j \implies S_i \cap S_j = \emptyset$:

1. **$S_{\text{Behavior}} \cap S_{\text{Contract}} = \emptyset$**: Functional domain intent (*what user scenarios achieve*) is semantically distinct from interface data schemas (*how typed payloads wire over HTTP/gRPC*).
2. **$S_{\text{Behavior}} \cap S_{\text{Policy}} = \emptyset$**: Functional domain intent is distinct from pass-fail quality/security evaluation criteria (*DoR/DoD gates*).
3. **$S_{\text{Behavior}} \cap S_{\text{Operational}} = \emptyset$**: Functional domain intent is distinct from infrastructure host constraints (*K8s CPU/RAM quotas*).
4. **$S_{\text{Contract}} \cap S_{\text{Policy}} = \emptyset$**: Structural API/DB schemas are distinct from quality gate compliance thresholds (*line coverage $\ge 85\%$*).
5. **$S_{\text{Contract}} \cap S_{\text{Operational}} = \emptyset$**: Interface payload contracts are distinct from physical compute hosting parameters.
6. **$S_{\text{Policy}} \cap S_{\text{Operational}} = \emptyset$**: Quality/security validation gates are distinct from cloud infrastructure resource allocations.

### 1.2 Proof of Collective Exhaustiveness (CE)
To prove Collective Exhaustiveness, we show that any arbitrary specification $s \in S$ in any software system maps to at least one facet:
- If $s$ describes functional business logic or user goals $\implies s \in S_{\text{Behavior}}$.
- If $s$ describes data types, API signatures, or database structures $\implies s \in S_{\text{Contract}}$.
- If $s$ describes security rules, readiness gates, or test quality criteria $\implies s \in S_{\text{Policy}}$.
- If $s$ describes deployment topology, resource limits, or scaling configurations $\implies s \in S_{\text{Operational}}$.

No software specification exists outside these four facets. Thus, $S_{\text{Behavior}} \cup S_{\text{Contract}} \cup S_{\text{Policy}} \cup S_{\text{Operational}} = S$. $\blacksquare$

---

## 2. The Unified `Spec` Schema

```typescript
export enum SpecType {
  BEHAVIOR = 'BEHAVIOR',       // Functional domain intent & Gherkin scenarios
  CONTRACT = 'CONTRACT',       // API schemas, DB schemas, event payloads
  POLICY = 'POLICY',           // DoR/DoD quality gates, security, SLA rules
  OPERATIONAL = 'OPERATIONAL'  // IaC, scaling, K8s resources, cloud parameters
}

export enum ProposalStatus {
  NONE = 'NONE',
  PROPOSED = 'PROPOSED',
  COUNTERED = 'COUNTERED',
  ACCEPTED = 'ACCEPTED',
  REJECTED = 'REJECTED',
  LOCKED = 'LOCKED'
}

export interface Spec {
  id: string;
  type: SpecType;              // Provably MECE Spec Type
  title: string;
  
  // Dual-State Proposal Mechanics
  liveContent: string | Record<string, any>;     // Active Enforced Spec
  proposedContent?: string | Record<string, any>; // Pending Modification / PR Diff
  proposalStatus: ProposalStatus;
  
  updatedAt: Date;
}
```

---

## 3. Universal Proposal State Machine

```
         ┌─────────────────────────────────────────────────┐
         │  spec.liveContent = "replicas: 2"                │
         │  spec.proposedContent = null                    │
         │  spec.proposalStatus = NONE                     │
         └─────────────────────────────────────────────────┘
                           │
              PROPOSE("replicas: 5")
                           │
         ┌─────────────────────────────────────────────────┐
         │  spec.liveContent = "replicas: 2"  (live)       │
         │  spec.proposedContent = "replicas: 5"           │
         │  spec.proposalStatus = PROPOSED                 │
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

## 4. Universal Human Taste Ergonomics (`@factory/ergonomics`)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   TIER 1: EXECUTIVE METRICS STRIP                      │
│   [Status: ACTIVE]   [Metric: 99.9% Uptime]   [Seal: Signed Attestation] │
├────────────────────────────────────────────────────────────────────────┤
│                   TIER 2: INTERACTIVE WORK TREE / MATRIX               │
│   Primary Domain Entity Tree / Execution Task Matrix / Status Filters   │
├────────────────────────────────────────────────────────────────────────┤
│                   TIER 3: VISUAL SPEC DIFF & AUDIT TRAIL               │
│   Unified Visual Diff View (spec.liveContent vs spec.proposedContent)   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Tier 1 (Executive Summary Strip)**: Status badges (`ACTIVE`), key performance indicators, and DSSE cryptographic seals.
2. **Tier 2 (Interactive Primary Matrix)**: Primary entity tree and WBS task execution matrix.
3. **Tier 3 (Visual Spec Diff & Audit View)**: Automated side-by-side or inline visual diff comparing `spec.liveContent` vs `spec.proposedContent` (Green additions / Red deletions) alongside the `Activity` log.

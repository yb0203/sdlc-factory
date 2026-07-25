# 📐 MECE Link Engine Specification (`MECE_LINK_ENGINE_SPEC.md`)

## 1. Architectural Philosophy: Is Linkage a Domain Property or Engine Property?

A fundamental architectural question arises when designing link engines:
> *Should the MECE Link Engine be a property of the Domain Model itself, or an external infrastructure concern?*

### The Architectural Answer: **Domain-Declared, Engine-Enforced**

The Link Engine operates on a **Dual-Faceted Architecture**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THE DUAL-FACETED LINK ARCHITECTURE                   │
├────────────────────────────────────────────────────────────────────────┤
│ 1. DOMAIN LAYER (Domain-Declared Semantics)                            │
│    - The Domain Model OWNS the business relationships.                 │
│    - Declarative schemas express REQUIRES, SEQUENCE, GOVERNS rules.    │
│    - Relationships are intrinsic business rules of the domain domain.  │
├────────────────────────────────────────────────────────────────────────┤
│ 2. ENGINE LAYER (Engine-Enforced Graph Mechanics)                      │
│    - The SDLC Engine OWNS graph algorithms and enforcement.            │
│    - Kahn's DAG cycle detection, CPM scheduling, position sorting.     │
│    - Polymorphic Link table persistence and Activity logging.          │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Link Semantics are INTRINSIC DOMAIN PROPERTIES**:
   - Relationships are not arbitrary external metadata; they represent the core business logic of the domain.
   - Example: In a Library Domain, `Loan REQUIRES Book` and `BorrowingPolicy GOVERNS Loan` are fundamental domain invariants defined directly inside `specs/domain/library.yaml`.

2. **Graph Mechanics are UNIFIED ENGINE CAPABILITIES**:
   - Rather than each domain writing custom code for graph traversal, cycle checking, or scheduling, the SDLC Factory engine provides a single, provably **MECE graph runner**.

---

## 2. Mathematical Proof of MECE

All directed edge types ($E$) connecting domain nodes ($V$) are partitioned across **four orthogonal dimensions**:

$$E = E_{\text{Space}} \cup E_{\text{Time}} \cup E_{\text{Contract}} \cup E_{\text{Lifecycle}}$$

$$\text{where } \forall i, j \in \{\text{Space}, \text{Time}, \text{Contract}, \text{Lifecycle}\}, i \neq j \implies E_i \cap E_j = \emptyset$$

```
                                  ┌──────────────────────────────────┐
                                  │      MECE LINK ENGINE            │
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

---

## 3. Declarative Domain Example vs Engine Execution

### 3.1 Domain-Native Spec Declaration (`specs/domain/library.yaml`)
*The Domain Spec declares relationship invariants natively:*

```yaml
apiVersion: factory.domain/v1
kind: EntitySpecification
metadata:
  name: Loan
domain: LibraryManagement
spec:
  attributes:
    loanId: string
    borrowedAt: timestamp
    dueAt: timestamp

  # DOMAIN-DECLARED MECE LINKS
  links:
    - dimension: SPACE
      type: REQUIRES
      target: Book
      invariant: "A loan cannot exist without an active Book entity."

    - dimension: TIME
      type: SEQUENCE
      target: ReturnBookTask
      invariant: "Checkout must precede Return in the execution WBS."

    - dimension: CONTRACT
      type: GOVERNS
      target: OverdueFinePolicy
      invariant: "OverdueFinePolicy dictates penalty calculation."
```

### 3.2 Engine Graph Execution (`@factory/core`)
*The SDLC Factory Engine parses domain-declared links and enforces graph mechanics:*

```typescript
export interface Link {
  id: string;                  // Unique UUID
  dimension: LinkDimension;    // SPACE | TIME | CONTRACT | LIFECYCLE
  linkType: LinkType;          // REQUIRES | SEQUENCE | GOVERNS | AMENDS | etc.
  sourceId: string;            // Domain Entity Source ID
  targetId: string;            // Domain Entity Target ID
  metadata?: Record<string, any>;
  createdAt: Date;
}

// Engine Graph Execution Runner
export function compileDomainGraph(entities: EntitySpec[], links: Link[]): CompiledGraph {
  // 1. Enforce Space DAG (detect structural cycles via Tarjan's algorithm)
  validateNoCycles(links.filter(l => l.dimension === LinkDimension.SPACE));

  // 2. Resolve Space Conflicts
  validateNoConflicts(entities, links.filter(l => l.linkType === LinkType.CONFLICTS));

  // 3. Run Critical Path Method (CPM) for Time SEQUENCE scheduling
  const executionWaves = scheduleCPM(links.filter(l => l.dimension === LinkDimension.TIME));

  // 4. Compute 2-Level Gapped Position Keys (10, 20, 30...)
  return generatePositionedGraph(entities, executionWaves);
}
```

---

## 4. Summary: Benefits of the Dual-Faceted Model

| Dimension | Domain Responsibility | Engine Responsibility |
|:---|:---|:---|
| **Semantics & Rules** | Declares what business links exist (`REQUIRES`, `SEQUENCE`). | Enforces type safety & link schema validation. |
| **Graph Topology** | Defines entity relationships in `.yaml` domain specs. | Runs cycle detection (Kahn's algorithm / Tarjan's). |
| **Execution** | Specifies task duration & business invariants. | Computes CPM scheduling & 2-level gapped sort keys. |
| **Evolution** | Defines version revision invariants (`AMENDS`). | Manages immutable audit trails & DSSE seals. |

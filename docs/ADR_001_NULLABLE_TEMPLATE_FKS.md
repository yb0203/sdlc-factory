# 🏛️ Architectural Decision Record (ADR-001): Nullable Template FKs & Ad-Hoc Entities

## Status
**ACCEPTED & ENFORCED**

---

## Context
When designing a Domain-Model Centric SDLC Factory, a fundamental architectural choice arises:
> *Should EVERY entity be forced to be a parameterized instance of a Template (`templateId` is mandatory), or should `templateId` be nullable to allow ad-hoc entities?*

---

## Decision
We enforce **Nullable Template Foreign Keys (`templateId: string | null`)**.

An `Entity`, `Task`, or `Spec` can be created either as:
1. **Template-Derived Instance** (`templateId != null`): Compiled from a reusable catalog template via JSON Schema validation and `{{placeholder}}` parameter substitution.
2. **Ad-Hoc Instance** (`templateId == null`): Created directly on-the-fly without a pre-existing catalog template.

Both ad-hoc and template-derived items are **100% first-class equals** across the MECE Link Engine, position key sorting (10, 20, 30...), quality DoR/DoD gates, formal proofs, and activity logging.

---

## Why Nullable `templateId`? (The Rationale)

### 1. Eliminates Friction for Rapid Iteration & Agent Codegen
Forcing an engineer or an `agy` SDK agent to author a formal `Template` record, write a JSON Schema `inputSchema`, and set up `{{placeholder}}` syntax *before* creating a single custom entity (e.g. `CustomAuditRunner` or `TempStagingConfig`) creates excessive ceremony and friction.

### 2. Prevents Catalog Bloat (YAGNI Principle)
Mandatory templates force single-use throwaway items into the global template catalog, cluttering the registry with hundreds of non-reusable entries.

### 3. Enables Organic Registry Growth Loop ("Save as Template")
Real-world software development discovers reusable patterns *after* building a feature, not before:
1. **Ad-Hoc Creation**: Developers/agents build ad-hoc entities (`templateId = null`).
2. **Pattern Discovery**: When an ad-hoc pattern is reused across 2+ projects, the factory triggers **Template Promotion**.
3. **Promotion Extraction**: The factory automatically extracts `inputSchema` parameters (`{{placeholder}}` syntax), creates a formal `Template` record, and updates original ad-hoc instances retroactively to point at the new `templateId`.

---

## Why NOT Mandatory Templates? (Trade-Off Analysis)

| Dimension | Mandatory Templates (`templateId` required) | Nullable Templates (`templateId: null` allowed) |
|:---|:---|:---|
| **Upfront Friction** | 🛑 **High**: Must write JSON Schemas before any work starts. | ✅ **Zero**: Instant ad-hoc creation. |
| **Catalog Cleanliness**| 🛑 **Bloated**: Full of single-use throwaway templates. | ✅ **Clean**: Catalog holds only verified reusable blueprints. |
| **Agent Capability** | 🛑 **Restricted**: Agents blocked if template doesn't exist. | ✅ **Autonomous**: Agents create ad-hoc entities & promote later. |
| **System Uniformity** | ✅ **100%**: Everything has a template link. | ✅ **100%**: Ad-hoc items use identical Link, Status & Proof schemas. |

---

## Consequences & Invariants

1. **Schema Invariant**: `templateId` is nullable on all primitive records (`Entity`, `Task`, `Spec`).
2. **Symmetric Operations**: Graph traversal, Tarjan DAG cycle detection, CPM scheduling, DoR/DoD gates, and formal Z3 SMT proofs treat ad-hoc items and template-derived items identically.
3. **Recompilation Protection**: Recompiling a draft project preserves ad-hoc items at their assigned gapped positions (e.g. position 25 between template positions 20 and 30).

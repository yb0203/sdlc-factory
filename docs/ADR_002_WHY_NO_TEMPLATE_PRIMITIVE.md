# 🏛️ Architectural Decision Record (ADR-002): Eliminating the `Template` Primitive

## Status
**ACCEPTED & ENFORCED**

---

## Context & Decision
In traditional software engineering, catalog systems use explicit `Template` abstractions (e.g. `EntityTemplate`, `TaskTemplate`, `SpecTemplate`) containing JSON Schemas (`inputSchema`) and regex parameter substitution (`{{placeholder}}`).

We have decided to **eliminate `Template` as a separate primitive entity class** in favor of **Prototype-Based Cloning & Direct Agent Synthesis**.

Reusability is achieved through two AI-native mechanisms:
1. **Prototype Cloning**: Any `Entity`, `Task`, or `Spec` can be marked `isPrototype: true` (or referenced via `prototypeId`). Stamping out a copy is simply `entity.clone(overrides)`.
2. **Direct Agent Synthesis**: The `google-antigravity` (agy) SDK LLM agent directly synthesizes customized, typed entity graphs from prompt intent, validating outputs against `Spec` policies.

---

## The 5-Primitive Core Taxonomy

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PROVABLY MINIMAL 5-PRIMITIVE TAXONOMY                │
├───────────────┬────────────────────────────────────────────────────────┤
│ 1. Entity     │ Structural domain object (Attributes, State, Schema)   │
│ 2. Task       │ Unit of execution work (code gen, migration, test)     │
│ 3. Spec       │ Declarative rule/policy AND proposal dual-state        │
│ 4. Link       │ MECE directional edge (Space, Time, Contract, Lifecycle)│
│ 5. Proof      │ Mathematical formal verification & Cryptographic seal  │
└───────────────┴────────────────────────────────────────────────────────┘
```
*(Plus `Activity` as the immutable event / audit trail log stream).*

---

## Comparative Rationale

| Dimension | Model A: Traditional `Template` Primitive | Model B: AI-Native Prototype & Direct Synthesis (No `Template`) — *OUR MODEL* |
|:---|:---|:---|
| **Core Primitives** | 🛑 **Complex (8+ Primitives)**: `Entity`, `EntityTemplate`, `Task`, `TaskTemplate`, `Spec`, `SpecTemplate`... | ✅ **Minimal (5 Pure Primitives)**: `Entity`, `Task`, `Spec`, `Link`, `Proof` |
| **Substitution Model** | 🛑 **Fragile Regex**: String replacement (`{{domain}}`) easily breaks on nested JSON / schema shifts. | ✅ **Structured DeepMerge**: Prototypal attribute merging & typed Pydantic overrides. |
| **AI Agent Alignment** | 🛑 **Low**: Forces LLMs to behave like dumb string macro replacers. | ✅ **High**: Leverages `agy` SDK LLM reasoning to directly synthesize typed instances. |
| **Reusability Engine** | **Catalog Blueprints**: Stamping out instances requires compiling a catalog template. | **Prototypal Cloning**: Any `Entity` with `isPrototype: true` can be cloned (`entity.clone()`). |
| **Upfront Friction** | 🛑 **High**: Must author JSON Schemas and template records before creating items. | ✅ **Zero**: Every object is a live entity; set `isPrototype = true` to share. |
| **Validation Gate** | Isolated `Template.inputSchema` JSON Schema validation. | DoR/DoD `Spec` policy validation & Pydantic entity schema checks. |

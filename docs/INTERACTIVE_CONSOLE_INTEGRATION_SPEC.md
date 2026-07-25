# 🖥️ Interactive Console & Antigravity 2.0 Integration (`INTERACTIVE_CONSOLE_INTEGRATION_SPEC.md`)

## Executive Summary
This document specifies how **SDLC Factory (`af`)** seamlessly integrates when a developer is operating inside the **Antigravity TUI**, **Antigravity 2.0 Console**, or **Antigravity IDE**.

---

## 1. Antigravity TUI Integration (`agy` Interactive Chat)

When operating inside the `agy` TUI terminal console, developers have two instant modes of interaction:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      ANTIGRAVITY TUI INTERACTION                       │
├───────────────────┬────────────────────────────────────────────────────┤
│ Interaction Mode  │ Developer Experience                               │
├───────────────────┼────────────────────────────────────────────────────┤
│ 1. Slash Commands │ • `/factory "intent"` -> Compiles intent into      │
│                   │   Deltas, Contracts, Edges, Proofs.                │
│                   │ • `/prove <entity>`   -> Runs Z3 SMT solver math.  │
│                   │ • `/onboard`          -> Auto-onboards workspace.  │
├───────────────────┼────────────────────────────────────────────────────┤
│ 2. Natural Prompt │ Developer: "Compile Loan into fine calculation"    │
│                   │ Agent: Uses `sdlc_factory` tool with Pydantic      │
│                   │ `response_schema=Delta` to return typed response.  │
└───────────────────┴────────────────────────────────────────────────────┘
```

### Slash Command Handler Definition (`.gemini/commands/factory.toml`)
```toml
[command]
name = "factory"
description = "Universal SDLC Factory Compiler"
alias = ["af"]

[execution]
command = "af \"$1\""
```

---

## 2. Antigravity 2.0 Console & Web Workbench Integration

Inside the **Antigravity 2.0 Web Console**, SDLC Factory exposes its **3-Tier Taste Ergonomics Interface**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ANTIGRAVITY 2.0 CONSOLE PANELS                       │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 1: EXECUTIVE METRICS & PROOF STRIP                                │
│   [Status: ACTIVE]   [Z3 SMT Invariant: PROVED]   [Seal: DSSE-Signed]  │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 2: INTERACTIVE MECE EDGE GRAPH & WBS MATRIX                       │
│   • Visual DAG Graph (Kahn / Tarjan Topological Order)                │
│   • Execution Wave Timelines & Delta Task Lists                        │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 3: VISUAL PROPOSAL REDLINE DIFF VIEW                              │
│   • Side-by-Side Diff: contract.liveContent vs contract.proposedContent│
│   • One-Click Action Buttons: [ ACCEPT ]  [ COUNTER ]  [ REJECT ]      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Antigravity IDE (VS Code / JetBrains / Cursor)

1. **Inline Gutter Badges**: Displays Z3 SMT invariant verification status directly in the editor gutter next to domain entity code (`✓ Z3 Invariant Proved`).
2. **Git Notes Status Bar Widget**: Displays real-time agent reasoning thoughts extracted directly from Git Notes (`refs/notes/activity`).
3. **DoR Pre-Commit Notification**: Prevents bad commits in the IDE Git panel if Z3 SMT solver invariants or unit tests fail.

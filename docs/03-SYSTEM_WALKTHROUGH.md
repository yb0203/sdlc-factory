# 💻 Book 3: System Walkthrough & agy SDK Integration Guide (`03-SYSTEM_WALKTHROUGH.md`)

## Executive Summary
This document provides a complete, hands-on walkthrough demonstrating how the **Domain-Model Centric SDLC Factory** processes a concrete feature request for a **Library Management System** using the **`google-antigravity` (agy) Python SDK**.

---

## 1. Concrete Feature Scenario: Library Management System

### Feature Request
> *"Implement automated overdue fine calculation ($1/day penalty after 14 days, max $50 cap) for returned library books."*

### Initial Domain Graph State
The domain model is defined in `specs/domain/*.yaml` using our **MECE Link Engine**:

```
 ┌──────────────┐   REQUIRES (Space)    ┌──────────────┐   REQUIRES (Space)   ┌──────────────┐
 │    Member    │ ◄──────────────────── │     Loan     │ ───────────────────► │     Book     │
 └──────────────┘                       └──────┬───────┘                      └──────────────┘
                                               │
                                       GOVERNS │ (Contract)
                                               ▼
                                        ┌──────────────┐
                                        │ Borrowing    │
                                        │ RuleSpec     │
                                        └──────────────┘
```

- **Domain Entities**: `Member`, `Book`, `Loan`, `Fine`.
- **MECE Links**:
  - `Space`: `Loan REQUIRES Member`, `Loan REQUIRES Book`, `Loan COMPOSES Fine`.
  - `Time`: `CheckoutBook SEQUENCE ReturnBook SEQUENCE CalculateFine`.
  - `Contract`: `BorrowingRuleSpec GOVERNS Loan`.
  - `Lifecycle`: `AmendedBorrowingRule AMENDS BorrowingRuleSpec`.

---

## 2. Step-by-Step Engine Execution Lifecycle

```
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ STEP 1: DoR Gate │ ───► │ STEP 2: Delta    │ ───► │ STEP 3: Sandbox  │ ───► │ STEP 4: DoD &    │
│    Validation    │      │    Compilation   │      │    Codegen (agy) │      │    DSSE Review   │
└──────────────────┘      └──────────────────┘      └──────────────────┘      └─────────┬────────┘
                                                                                        │
                                                                                        ▼
                                                                               ┌──────────────────┐
                                                                               │ STEP 5: Memory   │
                                                                               │    Compounding   │
                                                                               └──────────────────┘
```

### Step 1: Definition of Ready (DoR) Gate Validation
Developer issues command:
```bash
agy-factory run --feature "Overdue Fines: $1/day penalty after 14 days, capped at $50"
```
- `agy` Architect Agent validates `Loan` entity schema and DoR policy (`DefinitionOfReady`).
- Confirms Gherkin acceptance scenarios and context packs are valid before codegen starts.

### Step 2: Intent Compilation & Delta Calculation ($\text{Desired} = \text{Current} + \text{Delta}$)
The Architect Agent projects intent onto the domain graph and derives the **Delta**:
- **Entity Update**: Extend `Loan` entity with `fineCents: int` and `overdueDays: int`.
- **New Spec/Contract**: Add `OverduePolicy` (`GOVERNS` $\rightarrow$ `FineRecord`).
- **Gapped WBS Task Breakdown**:
  - `Position 10`: DB migration (`add_fine_columns`).
  - `Position 20`: `OverdueFineCalculator` domain service logic.
  - `Position 30`: Unit/Integration test suite (`test_overdue_fine_cap`).
  - `Position 40` (`isGate = true`): Quality & Security Verification Gate.

### Step 3: Ephemeral Sandbox Execution via `google-antigravity` SDK
The Python SDK runner spawns an agent loop inside an isolated git worktree:

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

async def execute_codegen_task():
    # Configure agy agent with write capabilities for sandbox
    config = LocalAgentConfig(
        system_instructions="You are an expert Domain-Driven Design Python developer.",
        capabilities=CapabilitiesConfig()  # enables run_command, edit_file
    )

    async with Agent(config) as agent:
        # Prompt agent with compiled Delta task
        response = await agent.chat(
            "Execute Task 20: Implement OverdueFineCalculator in domain/services/fine_calculator.py "
            "Rule: $1/day after 14 days, max $50. Return typed result."
        )

        # Stream reasoning thoughts in real time
        async for thought in response.thoughts:
            print(f"[Architectural Thought] {thought}")

        # Intercept tool executions
        async for call in response.tool_calls:
            print(f"[Tool Execution] {call.name}({call.args})")

if __name__ == "__main__":
    asyncio.run(execute_codegen_task())
```

### Step 4: Multi-Agent Review & Cryptographic DSSE Sign-off (DoD)
Once local `pytest` suite passes ($\rightarrow$ 100% green):
1. **Security Reviewer Agent**: Scans diff with Semgrep for SQL injection or integer overflow risks ($\rightarrow$ **PASSED**).
2. **Architecture Reviewer Agent**: Confirms domain service purity and SOLID principles ($\rightarrow$ **PASSED**).
3. **DSSE Seal**: Cryptographic attestation seal attached to commit diff, opening a signed Pull Request.

### Step 5: Epistemic Compounding (`learnings.md`) & Audit Logging
If `pytest` initially failed due to timezone drift during date math:
1. Agent extracts failure root cause.
2. Appends rule to `learnings.md`: 
   > *Learning 023: Always evaluate Loan due dates using `datetime.now(timezone.utc)` to prevent negative fines across timezones.*
3. Rule auto-injects into future agent context packs (`AGENTS.md`).
4. Full audit event logged to immutable `Activity` trail.

# 🚀 What is `agy`? (`AGY_SDK_REFERENCE.md`)

## Executive Summary
**`agy`** (pronounced *"ag-y"*) is the short shorthand name for **Google Antigravity**, the next-generation AI agent platform and Python SDK created by the Google DeepMind team.

In this project, `agy` refers to three core components:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AGY ECOSYSTEM COMPONENT MAP                     │
├───────────────────┬────────────────────────────────────────────────────┤
│ Component         │ Purpose & Function                                 │
├───────────────────┼────────────────────────────────────────────────────┤
│ 1. Antigravity CLI│ `agy` command-line binary used to drive agentic   │
│    (`agy`)        │ workflows, slash commands, and sidecars.           │
├───────────────────┼────────────────────────────────────────────────────┤
│ 2. Python SDK     │ `google-antigravity` (`import google.antigravity`) │
│    (`google.agy`) │ Python SDK powering agent runtimes & Pydantic      │
│                   │ structured LLM outputs.                            │
├───────────────────┼────────────────────────────────────────────────────┤
│ 3. SDLC CLI       │ `agy-factory` binary (`agy-factory compile`,       │
│    (`agy-factory`)│ `agy-factory prove`, `init`, `onboard`).           │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 1. The `google-antigravity` Python SDK

Our SDLC Factory is built natively on top of the **`google-antigravity` Python SDK**:

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from schemas.v1 import Entity, Delta, Contract, Edge, Proof

async def run_factory_agent():
    # 1. Configure local agy agent
    config = LocalAgentConfig(
        system_instructions="You are an SDLC Factory Architect Agent.",
        capabilities=CapabilitiesConfig()
    )

    # 2. Launch agy agent runtime
    async with Agent(config) as agent:
        # 3. Stream reasoning & request strongly-typed Pydantic output
        response = await agent.chat(
            "Compile the Loan entity into a Delta mutation...",
            response_schema=Delta  # Pydantic schema validation
        )
        print(f"Validated Delta: {response}")

if __name__ == "__main__":
    asyncio.run(run_factory_agent())
```

---

## 2. The `agy-factory` Command Line Interface

Our project binary is named **`agy-factory`**, providing four primary subcommands:

1. **`agy-factory init`**: Initiates a brand new SDLC Factory project from a prompt intent (< 10s).
2. **`agy-factory onboard`**: Retrofits an existing legacy/active codebase into the SDLC Factory (< 30s).
3. **`agy-factory compile`**: Compiles a domain entity into provably MECE projection units (`{Delta, Contract, Edge, Proof}`).
4. **`agy-factory prove`**: Runs formal Z3 SMT solver invariant verification for a domain entity.

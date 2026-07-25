"""
Universal Entity Projection Compiler Engine (@factory/compiler)
Projects a source Entity into provably MECE projection units: {Delta, Contract, Edge, Proof}
"""

import uuid
from datetime import datetime
from typing import Any, Dict, List, Tuple
from sdlc_factory.primitives import (
    Entity,
    Delta,
    DeltaType,
    Contract,
    SpecType,
    ProposalStatus,
    Edge,
    EdgeDimension,
    EdgeType,
    Proof,
    ProofFacet,
    SolverEngine,
    ProofStatus,
    Activity,
    ActivityType,
    Status,
)


class CompilationResult:
    def __init__(
        self,
        deltas: List[Delta],
        contracts: List[Contract],
        edges: List[Edge],
        proofs: List[Proof],
        activity: Activity,
    ):
        self.deltas = deltas
        self.contracts = contracts
        self.edges = edges
        self.proofs = proofs
        self.activity = activity

    def to_dict(self) -> Dict[str, Any]:
        return {
            "deltas": [d.model_dump() for d in self.deltas],
            "contracts": [c.model_dump() for c in self.contracts],
            "edges": [e.model_dump() for e in self.edges],
            "proofs": [p.model_dump() for p in self.proofs],
            "activity": self.activity.model_dump(),
        }


class EntityProjectionCompiler:
    """
    Universal Entity Projection Compiler Engine
    Projects high-level domain entities into concrete execution Deltas,
    Contract specs, MECE Edges, and Proof targets.
    """

    def compile_entity(
        self,
        entity: Entity,
        intent_description: str,
        actor_id: str = "architect-agent",
    ) -> CompilationResult:
        deltas: List[Delta] = []
        contracts: List[Contract] = []
        edges: List[Edge] = []
        proofs: List[Proof] = []

        # 1. Project Execution Deltas (WBS gapped position keying: 10, 20, 30...)
        d1 = Delta(
            id=str(uuid.uuid4()),
            title=f"Codegen: Implement {entity.name} Domain Logic",
            entityId=entity.id,
            deltaType=DeltaType.CODEGEN,
            status=Status.PENDING,
            position=10,
        )
        d2 = Delta(
            id=str(uuid.uuid4()),
            title=f"Verification Gate: {entity.name} Unit & Security Verification",
            entityId=entity.id,
            deltaType=DeltaType.TEST_EXECUTION,
            isGate=True,
            status=Status.PENDING,
            position=20,
        )
        deltas.extend([d1, d2])

        # 2. Project Declarative Contracts (Policy & Behavior)
        c1 = Contract(
            id=str(uuid.uuid4()),
            type=SpecType.BEHAVIOR,
            title=f"{entity.name} Acceptance Invariants",
            liveContent=f"System MUST enforce invariant bounds on {entity.name} attributes.",
            proposalStatus=ProposalStatus.NONE,
            isHardGuardrail=True,
        )
        c2 = Contract(
            id=str(uuid.uuid4()),
            type=SpecType.POLICY,
            title=f"{entity.name} Definition of Ready Gate",
            liveContent={"requiresSpec": True, "requiresDoRApproval": True},
            proposalStatus=ProposalStatus.NONE,
            isHardGuardrail=True,
        )
        contracts.extend([c1, c2])

        # 3. Project MECE Graph Edges (Space, Time, Contract)
        e1 = Edge(
            id=str(uuid.uuid4()),
            dimension=EdgeDimension.TIME,
            edgeType=EdgeType.SEQUENCE,
            sourceId=d1.id,
            targetId=d2.id,
            metadata={"rule": "Codegen task precedes Verification Gate"},
        )
        e2 = Edge(
            id=str(uuid.uuid4()),
            dimension=EdgeDimension.CONTRACT,
            edgeType=EdgeType.GOVERNS,
            sourceId=c1.id,
            targetId=entity.id,
        )
        edges.extend([e1, e2])

        # 4. Project Proof Targets (Formal Math & DSSE Cryptographic Seal)
        p1 = Proof(
            id=str(uuid.uuid4()),
            facet=ProofFacet.FORMAL_MATHEMATICAL,
            targetId=entity.id,
            solverEngine=SolverEngine.Z3_SMT,
            theoremExpression=f"forall e in {entity.name}, attributes_valid(e) == True",
            status=ProofStatus.PROVING,
        )
        proofs.append(p1)

        # 5. Emit Immutable Activity Log Entry
        act = Activity(
            id=str(uuid.uuid4()),
            entityId=entity.id,
            type=ActivityType.COMPILATION_EVENT,
            actorId=actor_id,
            content=f"Compiled Entity '{entity.name}' ({intent_description}) into 2 Deltas, 2 Contracts, 2 Edges, 1 Proof.",
            payload={"compiledDeltaCount": len(deltas), "compiledContractCount": len(contracts)},
        )

        return CompilationResult(
            deltas=deltas,
            contracts=contracts,
            edges=edges,
            proofs=proofs,
            activity=act,
        )

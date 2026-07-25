"""
Unit tests for SDLC Factory Core
Tests 5 primitives, Entity Projection Compiler, Link Engine, and Z3 Proof Verifier.
"""

import uuid
import pytest
from sdlc_factory.primitives import (
    Entity,
    Delta,
    Contract,
    Edge,
    Proof,
    Status,
    EdgeDimension,
    EdgeType,
    ProofStatus,
    ProofFacet,
    SolverEngine,
)
from sdlc_factory.compiler.projection import EntityProjectionCompiler
from sdlc_factory.graph.link_engine import MECEEdgeEngine, CycleDetectedError
from sdlc_factory.runner.proof_verifier import FormalProofVerifier


def test_entity_creation():
    entity = Entity(
        id=str(uuid.uuid4()),
        name="Loan",
        domain="LibraryManagement",
        attributes={"bookId": "string", "memberId": "string"},
        status=Status.DRAFT,
        position=10,
    )
    assert entity.name == "Loan"
    assert entity.isPrototype is False


def test_entity_projection_compiler():
    entity = Entity(
        id=str(uuid.uuid4()),
        name="Loan",
        domain="LibraryManagement",
        attributes={},
        status=Status.DRAFT,
        position=10,
    )
    compiler = EntityProjectionCompiler()
    res = compiler.compile_entity(entity, "Implement fine calculations")

    assert len(res.deltas) == 2
    assert len(res.contracts) == 2
    assert len(res.edges) == 2
    assert len(res.proofs) == 1
    assert res.activity.entityId == entity.id


def test_mece_link_engine_dag_validation():
    engine = MECEEdgeEngine()
    e1 = Edge(
        id=str(uuid.uuid4()),
        dimension=EdgeDimension.TIME,
        edgeType=EdgeType.SEQUENCE,
        sourceId="node_1",
        targetId="node_2",
    )
    e2 = Edge(
        id=str(uuid.uuid4()),
        dimension=EdgeDimension.TIME,
        edgeType=EdgeType.SEQUENCE,
        sourceId="node_2",
        targetId="node_3",
    )
    assert engine.validate_dag([e1, e2]) is True

    # Add cycle
    e_cycle = Edge(
        id=str(uuid.uuid4()),
        dimension=EdgeDimension.TIME,
        edgeType=EdgeType.SEQUENCE,
        sourceId="node_3",
        targetId="node_1",
    )
    with pytest.raises(CycleDetectedError):
        engine.validate_dag([e1, e2, e_cycle])


def test_proof_verifier_smt():
    proof = Proof(
        id=str(uuid.uuid4()),
        facet=ProofFacet.FORMAL_MATHEMATICAL,
        targetId="Loan",
        solverEngine=SolverEngine.Z3_SMT,
        status=ProofStatus.PROVING,
    )
    verifier = FormalProofVerifier()
    status, msg = verifier.verify_smt_invariant(proof, {})
    assert status == ProofStatus.PROVED
    assert proof.status == ProofStatus.PROVED

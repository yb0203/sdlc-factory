"""
SDLC Factory Core Primitive Pydantic Models (v1)
Generic, strongly-typed Python schemas for google-antigravity (agy) SDK structured agent outputs.
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Status(str, Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    IN_REVIEW = "IN_REVIEW"
    ON_HOLD = "ON_HOLD"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    ARCHIVED = "ARCHIVED"


# ==========================================
# 1. Entity Primitive
# ==========================================
class Entity(BaseModel):
    id: str = Field(..., description="Unique UUID for Entity instance")
    name: str = Field(..., description="Domain entity name (e.g. Member, Book, Loan)")
    domain: str = Field(..., description="Bounded context or domain namespace")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Typed attributes and field definitions")
    isPrototype: bool = Field(default=False, description="Whether this entity is a prototype for cloning (ADR-002)")
    prototypeId: Optional[str] = Field(default=None, description="ID of parent prototype if cloned")
    status: Status = Field(default=Status.DRAFT)
    position: int = Field(..., description="Gapped position key for deterministic sort order (10, 20, 30...)")
    createdAt: datetime = Field(default_factory=utc_now)
    updatedAt: datetime = Field(default_factory=utc_now)


# ==========================================
# 2. Delta Primitive
# ==========================================
class DeltaType(str, Enum):
    CODEGEN = "CODEGEN"
    DB_MIGRATION = "DB_MIGRATION"
    BUILD_JOB = "BUILD_JOB"
    TEST_EXECUTION = "TEST_EXECUTION"
    INFRA_PROVISION = "INFRA_PROVISION"
    REFACTOR = "REFACTOR"


class GateStatus(str, Enum):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    PENDING = "PENDING"
    PASSED = "PASSED"
    FAILED = "FAILED"
    WAIVED = "WAIVED"


class Delta(BaseModel):
    id: str = Field(..., description="Unique UUID for Delta instance")
    title: str = Field(..., description="Title of execution delta task")
    entityId: Optional[str] = Field(default=None, description="Target Entity ID this delta mutates")
    deltaType: DeltaType = Field(..., description="Category of state mutation")
    isGate: bool = Field(default=False, description="Whether this delta represents a mandatory review gate")
    gateStatus: GateStatus = Field(default=GateStatus.NOT_APPLICABLE)
    durationDays: int = Field(default=1)
    costCents: int = Field(default=0)
    status: Status = Field(default=Status.PENDING)
    position: int = Field(..., description="Gapped WBS position key (10, 20, 30...)")
    createdAt: datetime = Field(default_factory=utc_now)


# ==========================================
# 3. Contract Primitive
# ==========================================
class SpecType(str, Enum):
    BEHAVIOR = "BEHAVIOR"       # Functional domain intent & Gherkin scenarios
    CONTRACT = "CONTRACT"       # API schemas, DB schemas, event payloads
    POLICY = "POLICY"           # DoR/DoD quality gates, security thresholds, SLAs
    OPERATIONAL = "OPERATIONAL"  # IaC, scaling, K8s resources, cloud parameters


class ProposalStatus(str, Enum):
    NONE = "NONE"
    PROPOSED = "PROPOSED"
    COUNTERED = "COUNTERED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    LOCKED = "LOCKED"


class Contract(BaseModel):
    id: str = Field(..., description="Unique UUID for Contract/Spec instance")
    type: SpecType = Field(..., description="Provably MECE facet classification")
    title: str
    liveContent: Union[str, Dict[str, Any]] = Field(..., description="Active enforced spec content or rule")
    proposedContent: Optional[Union[str, Dict[str, Any]]] = Field(default=None, description="Pending proposed modification or PR diff")
    proposalStatus: ProposalStatus = Field(default=ProposalStatus.NONE)
    isHardGuardrail: bool = Field(default=False, description="If true, non-negotiable security/test gate")
    status: Status = Field(default=Status.ACTIVE)
    updatedAt: datetime = Field(default_factory=utc_now)


# ==========================================
# 4. Edge Primitive
# ==========================================
class EdgeDimension(str, Enum):
    SPACE = "SPACE"
    TIME = "TIME"
    CONTRACT = "CONTRACT"
    LIFECYCLE = "LIFECYCLE"


class EdgeType(str, Enum):
    # Space
    REQUIRES = "REQUIRES"
    CONFLICTS = "CONFLICTS"
    COMPOSES = "COMPOSES"
    # Time
    SEQUENCE = "SEQUENCE"
    BLOCKS = "BLOCKS"
    PARALLEL_WITH = "PARALLEL_WITH"
    # Contract
    GOVERNS = "GOVERNS"
    DERIVES_FROM = "DERIVES_FROM"
    # Lifecycle
    AMENDS = "AMENDS"
    SUPERSEDES = "SUPERSEDES"


class Edge(BaseModel):
    id: str = Field(..., description="Unique UUID for Edge instance")
    dimension: EdgeDimension = Field(..., description="Orthogonal MECE Edge Dimension")
    edgeType: EdgeType = Field(..., description="Exact MECE Edge Type")
    sourceId: str = Field(..., description="Source Entity/Contract/Delta ID")
    targetId: str = Field(..., description="Target Entity/Contract/Delta ID")
    metadata: Dict[str, Any] = Field(default_factory=dict)
    createdAt: datetime = Field(default_factory=utc_now)


# ==========================================
# 5. Proof Primitive
# ==========================================
class ProofFacet(str, Enum):
    FORMAL_MATHEMATICAL = "FORMAL_MATHEMATICAL"
    CRYPTOGRAPHIC_ATTESTATION = "CRYPTOGRAPHIC_ATTESTATION"


class SolverEngine(str, Enum):
    Z3_SMT = "Z3_SMT"
    TARJAN_DAG = "TARJAN_DAG"
    MECE_PARTITION = "MECE_PARTITION"
    DSSE_ECDSA = "DSSE_ECDSA"
    AIBOM_MERKLE = "AIBOM_MERKLE"


class ProofStatus(str, Enum):
    PROVING = "PROVING"
    PROVED = "PROVED"
    DISPROVED = "DISPROVED"
    ESCALATED = "ESCALATED"


class Proof(BaseModel):
    id: str = Field(..., description="Unique UUID for Proof instance")
    facet: ProofFacet = Field(..., description="Proof facet (DoR formal math vs DoD DSSE seal)")
    targetId: str = Field(..., description="Target Entity, Contract, Delta, or Project ID")
    solverEngine: SolverEngine = Field(...)
    theoremExpression: Optional[str] = Field(default=None, description="Formal logic invariant or expression")
    counterExample: Optional[str] = Field(default=None, description="Solver counter-example if DISPROVED")
    signatureSeal: Optional[str] = Field(default=None, description="DSSE cryptographic seal or AIBOM hash")
    status: ProofStatus = Field(default=ProofStatus.PROVING)
    createdAt: datetime = Field(default_factory=utc_now)


# ==========================================
# 6. Activity Log Primitive
# ==========================================
class ActivityType(str, Enum):
    STATUS_CHANGE = "STATUS_CHANGE"
    PROPOSAL_CHANGE = "PROPOSAL_CHANGE"
    COMPILATION_EVENT = "COMPILATION_EVENT"
    AGENT_THOUGHT = "AGENT_THOUGHT"
    TOOL_EXECUTION = "TOOL_EXECUTION"
    GATE_VERIFICATION = "GATE_VERIFICATION"
    PROOF_VERIFICATION = "PROOF_VERIFICATION"
    LEARNING_EXTRACTED = "LEARNING_EXTRACTED"
    AMENDMENT_INITIATED = "AMENDMENT_INITIATED"


class Activity(BaseModel):
    id: str = Field(..., description="Unique UUID for Activity log entry")
    entityId: str = Field(..., description="Target primitive ID this activity belongs to")
    type: ActivityType = Field(...)
    actorId: str = Field(..., description="User ID or Agent Role (e.g. 'architect-agent')")
    content: str = Field(..., description="Log message or agent thought string")
    payload: Dict[str, Any] = Field(default_factory=dict, description="Structured tool args or command diffs")
    timestamp: datetime = Field(default_factory=utc_now)

"""
Core 5-Primitive Taxonomy
Re-exports generic models from schemas.v1.models
"""

import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from schemas.v1.models import (
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

__all__ = [
    "Entity",
    "Delta",
    "DeltaType",
    "Contract",
    "SpecType",
    "ProposalStatus",
    "Edge",
    "EdgeDimension",
    "EdgeType",
    "Proof",
    "ProofFacet",
    "SolverEngine",
    "ProofStatus",
    "Activity",
    "ActivityType",
    "Status",
]

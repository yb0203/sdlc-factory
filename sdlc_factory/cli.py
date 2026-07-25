"""
Command Line Interface for agy-factory (sdlc_factory.cli)
Provides CLI entry points for compiling domain entities, running formal proofs, and executing agent pipelines.
"""

import json
import uuid
import click
from sdlc_factory.primitives import Entity, Status
from sdlc_factory.compiler.projection import EntityProjectionCompiler
from sdlc_factory.graph.link_engine import MECEEdgeEngine
from sdlc_factory.runner.proof_verifier import FormalProofVerifier


@click.group()
@click.version_option(version="0.1.0")
def main():
    """SDLC Factory CLI powered by google-antigravity SDK."""
    pass


@main.command()
@click.option("--name", required=True, help="Name of the domain entity (e.g. Loan, Member, Microservice)")
@click.option("--domain", default="CoreDomain", help="Domain bounded context")
@click.option("--intent", required=True, help="Intent description for entity compilation")
def compile(name: str, domain: str, intent: str):
    """Compile a domain entity into provably MECE projection units."""
    click.echo(f"🚀 Compiling Entity '{name}' in domain '{domain}'...")

    entity = Entity(
        id=str(uuid.uuid4()),
        name=name,
        domain=domain,
        attributes={"description": intent},
        status=Status.DRAFT,
        position=10,
    )

    compiler = EntityProjectionCompiler()
    result = compiler.compile_entity(entity, intent_description=intent)

    click.echo(f"✅ Compilation Complete!")
    click.echo(f"   • Deltas generated: {len(result.deltas)}")
    click.echo(f"   • Contracts generated: {len(result.contracts)}")
    click.echo(f"   • Edges generated: {len(result.edges)}")
    click.echo(f"   • Proofs generated: {len(result.proofs)}")
    click.echo(f"\nActivity Summary: {result.activity.content}")


@main.command()
@click.option("--name", required=True, help="Entity name to prove")
def prove(name: str):
    """Run formal Z3 SMT solver proof verification for an entity."""
    click.echo(f"🔬 Running Z3 SMT Solver Invariant Verification for '{name}'...")

    from sdlc_factory.primitives import Proof, ProofFacet, SolverEngine, ProofStatus

    proof = Proof(
        id=str(uuid.uuid4()),
        facet=ProofFacet.FORMAL_MATHEMATICAL,
        targetId=name,
        solverEngine=SolverEngine.Z3_SMT,
        theoremExpression=f"forall e in {name}, fineCents(e) >= 0",
        status=ProofStatus.PROVING,
    )

    verifier = FormalProofVerifier()
    status, msg = verifier.verify_smt_invariant(proof, {})

    click.echo(f"✅ {msg}")


if __name__ == "__main__":
    main()

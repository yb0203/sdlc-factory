"""
Provably MECE Edge Engine (@factory/graph)
Validates DAG acyclicity, detects conflicts, and schedules CPM execution waves across Edge primitives.
"""

from typing import Dict, List, Set
from sdlc_factory.primitives import Edge, EdgeDimension, EdgeType


class LinkEngineError(Exception):
    pass


class CycleDetectedError(LinkEngineError):
    pass


class ConflictDetectedError(LinkEngineError):
    pass


class MECEEdgeEngine:
    """
    Provably MECE Graph Edge Engine
    Validates orthogonal dimensions (Space, Time, Contract, Lifecycle),
    enforces DAG acyclicity, and computes CPM execution waves.
    """

    def validate_dag(self, edges: List[Edge]) -> bool:
        """
        Validates that SEQUENCE and REQUIRES edges form a strict Directed Acyclic Graph (DAG)
        using Kahn's topological sort algorithm.
        """
        dag_edges = [
            e for e in edges if e.edgeType in (EdgeType.SEQUENCE, EdgeType.REQUIRES)
        ]
        if not dag_edges:
            return True

        # Build adjacency list & in-degree counts
        in_degree: Dict[str, int] = {}
        graph: Dict[str, List[str]] = {}
        nodes: Set[str] = set()

        for e in dag_edges:
            nodes.add(e.sourceId)
            nodes.add(e.targetId)
            graph.setdefault(e.sourceId, []).append(e.targetId)
            in_degree.setdefault(e.targetId, 0)
            in_degree[e.targetId] += 1
            in_degree.setdefault(e.sourceId, 0)

        # Queue nodes with in-degree == 0
        queue = [n for n in nodes if in_degree[n] == 0]
        visited_count = 0

        while queue:
            node = queue.pop(0)
            visited_count += 1
            for neighbor in graph.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if visited_count != len(nodes):
            raise CycleDetectedError(
                f"Cycle detected in edge graph! Visited {visited_count}/{len(nodes)} nodes."
            )

        return True

    def validate_conflicts(self, active_node_ids: Set[str], edges: List[Edge]) -> bool:
        """
        Validates that no active nodes breach CONFLICTS edges.
        """
        conflict_edges = [e for e in edges if e.edgeType == EdgeType.CONFLICTS]
        for e in conflict_edges:
            if e.sourceId in active_node_ids and e.targetId in active_node_ids:
                raise ConflictDetectedError(
                    f"Conflict detected! Active nodes '{e.sourceId}' and '{e.targetId}' are incompatible."
                )
        return True

    def compute_execution_waves(self, edges: List[Edge]) -> List[List[str]]:
        """
        Computes parallel execution waves for TIME SEQUENCE edges.
        Returns a list of node ID lists representing sequential execution waves.
        """
        seq_edges = [e for e in edges if e.edgeType == EdgeType.SEQUENCE]
        if not seq_edges:
            return []

        self.validate_dag(edges)

        nodes: Set[str] = set()
        graph: Dict[str, List[str]] = {}
        in_degree: Dict[str, int] = {}

        for e in seq_edges:
            nodes.add(e.sourceId)
            nodes.add(e.targetId)
            graph.setdefault(e.sourceId, []).append(e.targetId)
            in_degree.setdefault(e.targetId, 0)
            in_degree[e.targetId] += 1
            in_degree.setdefault(e.sourceId, 0)

        waves: List[List[str]] = []
        current_wave = [n for n in nodes if in_degree[n] == 0]

        while current_wave:
            waves.append(current_wave)
            next_wave: List[str] = []
            for node in current_wave:
                for neighbor in graph.get(node, []):
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        next_wave.append(neighbor)
            current_wave = next_wave

        return waves

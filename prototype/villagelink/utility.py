"""Local, structural queries over observed Village Link publications.

Connectivity reports published assertions, never established equivalence.
The graph neither dereferences endpoints nor discovers publications.
"""

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterable
from urllib.parse import urlsplit
import re

from .codec import parse as parse_uri

_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
_BAD_ESCAPE = re.compile(r"%(?![0-9A-Fa-f]{2})")


def _endpoint(uri: str) -> None:
    if not _SCHEME.match(uri) or any(c.isspace() or ord(c) < 32 for c in uri):
        raise ValueError(f"invalid endpoint URI: {uri!r}")
    if _BAD_ESCAPE.search(uri):
        raise ValueError(f"malformed endpoint URI escape: {uri!r}")
    parts = urlsplit(uri)
    if parts.scheme.lower() in {"http", "https"} and not parts.netloc:
        raise ValueError(f"HTTP endpoint URI needs an authority: {uri!r}")


@dataclass(frozen=True)
class Link:
    uri: str
    left: str
    right: str


def inspect(uri: str) -> Link:
    """Parse a Village Link and check both endpoint URI syntaxes."""
    left, right = parse_uri(uri)
    _endpoint(left)
    _endpoint(right)
    return Link(uri, left, right)


def parse(uri: str) -> tuple[str, str]:
    """Return the encoded order of the two valid endpoint URIs."""
    link = inspect(uri)
    return link.left, link.right


def validate(uri: str) -> bool:
    """Check link and endpoint URI syntax; make no network request."""
    try:
        inspect(uri)
    except (ValueError, TypeError):
        return False
    return True


@dataclass(frozen=True)
class Publication:
    link: str
    source_uri: str
    observed_at: str | None = None
    evidence_uri: str | None = None

    def __post_init__(self) -> None:
        inspect(self.link)
        _endpoint(self.source_uri)
        if self.evidence_uri is not None:
            _endpoint(self.evidence_uri)


@dataclass(frozen=True)
class Step:
    """A traversal step and all supplied publications of its edge."""
    source: str
    target: str
    publications: tuple[Publication, ...]


class Graph:
    """An immutable snapshot of an explicitly supplied, local dataset."""

    def __init__(self, publications: Iterable[Publication]):
        grouped: dict[frozenset[str], list[Publication]] = defaultdict(list)
        for publication in publications:
            link = inspect(publication.link)
            grouped[frozenset((link.left, link.right))].append(publication)
        adjacency: dict[str, list[Step]] = defaultdict(list)
        for ends, occurrences in grouped.items():
            members = sorted(ends)
            records = tuple(occurrences)
            if len(members) == 1:
                adjacency[members[0]].append(Step(members[0], members[0], records))
            else:
                a, b = members
                adjacency[a].append(Step(a, b, records))
                adjacency[b].append(Step(b, a, records))
        self._adjacency = {uri: tuple(sorted(steps, key=lambda s: s.target))
                           for uri, steps in adjacency.items()}

    def adjacent(self, uri: str) -> tuple[Step, ...]:
        return self._adjacency.get(uri, ())

    @staticmethod
    def _depth(max_depth: int) -> None:
        if isinstance(max_depth, bool) or not isinstance(max_depth, int) or max_depth < 0:
            raise ValueError("max_depth must be a non-negative integer")

    def traverse(self, uri: str, max_depth: int) -> tuple[Step, ...]:
        """Breadth-first discovery edges, at most max_depth hops away."""
        self._depth(max_depth)
        seen = {uri}
        queue = deque([(uri, 0)])
        steps = []
        while queue:
            current, depth = queue.popleft()
            if depth == max_depth:
                continue
            for step in self.adjacent(current):
                if step.target not in seen:
                    seen.add(step.target)
                    steps.append(step)
                    queue.append((step.target, depth + 1))
        return tuple(steps)

    def component(self, uri: str, max_depth: int) -> frozenset[str]:
        """Traces reachable within the bound, including the starting URI."""
        return frozenset((uri, *(step.target for step in self.traverse(uri, max_depth))))

    def paths(self, left: str, right: str, max_depth: int) -> tuple[tuple[Step, ...], ...]:
        """All simple structural paths within the bound (may grow exponentially)."""
        self._depth(max_depth)
        if left == right:
            return ((),)
        found = []
        stack = [(left, frozenset((left,)), ())]
        while stack:
            current, seen, path = stack.pop()
            if len(path) == max_depth:
                continue
            for step in reversed(self.adjacent(current)):
                if step.target in seen:
                    continue
                candidate = (*path, step)
                if step.target == right:
                    found.append(candidate)
                else:
                    stack.append((step.target, seen | {step.target}, candidate))
        return tuple(found)

    def connected(self, left: str, right: str, max_depth: int) -> bool:
        """Whether the supplied publication graph contains a bounded path."""
        self._depth(max_depth)
        return right in self.component(left, max_depth)

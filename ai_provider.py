from __future__ import annotations

from typing import Any, Protocol


class AIProvider(Protocol):
    """Interface for answering questions using structured screen context."""

    def ask(self, context: dict[str, Any], question: str) -> str:
        """Return an answer to a question about the supplied screen context."""
        ...
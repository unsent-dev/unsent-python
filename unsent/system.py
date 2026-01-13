"""System resource client."""
from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, TYPE_CHECKING

from .legacy_types import APIError

if TYPE_CHECKING:
    from .unsent import unsent

class System:
    """Client for system endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def health(self) -> Tuple[Optional[Dict[str, Any]], Optional[APIError]]:
        """Check system health."""
        data, err = self.unsent.get("/health")
        return (data, err)  # type: ignore[return-value]

    def version(self) -> Tuple[Optional[Dict[str, Any]], Optional[APIError]]:
        """Get system version."""
        data, err = self.unsent.get("/version")
        return (data, err)  # type: ignore[return-value]

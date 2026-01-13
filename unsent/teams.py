"""Teams resource client."""
from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, TYPE_CHECKING

from .legacy_types import APIError

if TYPE_CHECKING:
    from .unsent import unsent

from .types import TeamsGetResponse

class Teams:
    """Client for `/teams` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def list(self) -> Tuple[Optional[TeamsGetResponse], Optional[APIError]]:
        """List teams."""
        data, err = self.unsent.get("/teams")
        return (data, err)  # type: ignore[return-value]

    def get(self) -> Tuple[Optional[Dict[str, Any]], Optional[APIError]]:
        """Retrieve current team information."""
        data, err = self.unsent.get("/team")
        return (data, err)  # type: ignore[return-value]

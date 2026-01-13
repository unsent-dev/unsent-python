"""Activity resource client."""
from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, TYPE_CHECKING

from .legacy_types import APIError

if TYPE_CHECKING:
    from .unsent import unsent

from .types import ActivityGetResponse

class Activity:
    """Client for `/activity` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def list(
        self,
        *,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Tuple[Optional[ActivityGetResponse], Optional[APIError]]:
        """List activity.

        Args:
            page: Page number
            limit: Page size
        """
        query_params = []
        if page is not None:
            query_params.append(f"page={page}")
        if limit is not None:
            query_params.append(f"limit={limit}")

        query_string = "&".join(query_params)
        path = f"/activity?{query_string}" if query_string else "/activity"
        
        data, err = self.unsent.get(path)
        return (data, err)  # type: ignore[return-value]

    get = list

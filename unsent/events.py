"""Events resource client."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional, Tuple, TYPE_CHECKING, Union

from .legacy_types import APIError

if TYPE_CHECKING:
    from .unsent import unsent

from .types import EventsGetResponse

class Events:
    """Client for `/events` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def list(
        self,
        *,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None,
        start_date: Optional[Union[str, datetime]] = None,
    ) -> Tuple[Optional[EventsGetResponse], Optional[APIError]]:
        """List email events.

        Args:
            page: Page number
            limit: Page size
            status: Event status
            start_date: Filter events after this date
        """
        query_params = []
        if page is not None:
            query_params.append(f"page={page}")
        if limit is not None:
            query_params.append(f"limit={limit}")
        if status is not None:
            query_params.append(f"status={status}")
        if start_date is not None:
            val = start_date
            if isinstance(val, datetime):
                val = val.isoformat()
            query_params.append(f"startDate={val}")

        query_string = "&".join(query_params)
        path = f"/events?{query_string}" if query_string else "/events"
        
        data, err = self.unsent.get(path)
        return (data, err)  # type: ignore[return-value]

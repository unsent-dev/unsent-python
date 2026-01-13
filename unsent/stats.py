"""Stats resource client."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional, Tuple, TYPE_CHECKING, Union

from .legacy_types import APIError

if TYPE_CHECKING:
    from .unsent import unsent

from .types import StatsGetResponse

class Stats:
    """Client for `/stats` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def get(
        self,
        *,
        start_date: Optional[Union[str, datetime]] = None,
        end_date: Optional[Union[str, datetime]] = None,
    ) -> Tuple[Optional[StatsGetResponse], Optional[APIError]]:
        """Get stats.

        Args:
            start_date: Start date for stats
            end_date: End date for stats
        """
        query_params = []
        if start_date is not None:
            val = start_date
            if isinstance(val, datetime):
                val = val.isoformat()
            query_params.append(f"startDate={val}")
        if end_date is not None:
            val = end_date
            if isinstance(val, datetime):
                val = val.isoformat()
            query_params.append(f"endDate={val}")

        query_string = "&".join(query_params)
        path = f"/stats?{query_string}" if query_string else "/stats"
        
        data, err = self.unsent.get(path)
        return (data, err)  # type: ignore[return-value]

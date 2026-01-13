"""Metrics resource client."""
from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, TYPE_CHECKING

from .legacy_types import APIError

if TYPE_CHECKING:
    from .unsent import unsent

from .types import MetricsGetResponse

class Metrics:
    """Client for `/metrics` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def get(
        self,
        *,
        period: Optional[str] = "month",
    ) -> Tuple[Optional[MetricsGetResponse], Optional[APIError]]:
        """Get metrics.

        Args:
            period: Time period ('day', 'week', 'month')
        """
        query_params = []
        if period is not None:
            query_params.append(f"period={period}")

        query_string = "&".join(query_params)
        path = f"/metrics?{query_string}" if query_string else "/metrics"
        
        data, err = self.unsent.get(path)
        return (data, err)  # type: ignore[return-value]

"""Domain resource client using TypedDict shapes (no Pydantic)."""

from __future__ import annotations

from datetime import datetime
from typing import Optional, Tuple, List, Dict, Any, Union

from .legacy_types import APIError
from .types import (
    DomainsGetResponse,
    DomainsPostRequest,
    DomainsPostResponse,
    DomainsIdDeleteResponse,
    DomainsIdVerifyPutResponse,
    DomainsIdGetResponse,
)


class Domains:
    """Client for `/domains` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def list(self) -> Tuple[Optional[DomainsGetResponse], Optional[APIError]]:
        data, err = self.unsent.get("/domains")
        return (data, err)  # type: ignore[return-value]

    def create(
        self, payload: Union[DomainsPostRequest, Dict[str, Any]]
    ) -> Tuple[Optional[DomainsPostResponse], Optional[APIError]]:
        body = payload
        if hasattr(payload, "model_dump"):
            body = payload.model_dump(by_alias=True, exclude_none=True) # type: ignore
        data, err = self.unsent.post("/domains", body)
        return (data, err)  # type: ignore[return-value]

    def verify(
        self, domain_id: str
    ) -> Tuple[Optional[DomainsIdVerifyPutResponse], Optional[APIError]]:
        data, err = self.unsent.put(f"/domains/{domain_id}/verify", {})
        return (data, err)  # type: ignore[return-value]

    def get(self, domain_id: str) -> Tuple[Optional[DomainsIdGetResponse], Optional[APIError]]:
        data, err = self.unsent.get(f"/domains/{domain_id}")
        return (data, err)  # type: ignore[return-value]

    def delete(
        self, domain_id: str
    ) -> Tuple[Optional[DomainsIdDeleteResponse], Optional[APIError]]:
        data, err = self.unsent.delete(f"/domains/{domain_id}")
        return (data, err)  # type: ignore[return-value]

    def get_analytics(
        self,
        domain_id: str,
        *,
        period: Optional[str] = "month",
    ) -> Tuple[Optional[Dict[str, Any]], Optional[APIError]]:
        """Get domain analytics.

        Args:
            domain_id: The domain ID
            period: Time period ('day', 'week', 'month')
        """
        query_params = []
        if period is not None:
            query_params.append(f"period={period}")

        query_string = "&".join(query_params)
        path = f"/domains/{domain_id}/analytics?{query_string}" if query_string else f"/domains/{domain_id}/analytics"
        data, err = self.unsent.get(path)
        return (data, err)  # type: ignore[return-value]

    def get_stats(
        self,
        domain_id: str,
        *,
        start_date: Optional[Union[str, datetime]] = None,
        end_date: Optional[Union[str, datetime]] = None,
    ) -> Tuple[Optional[Dict[str, Any]], Optional[APIError]]:
        """Get domain stats.

        Args:
            domain_id: The domain ID
            start_date: Start date
            end_date: End date
        """
        query_params = []
        if start_date is not None:
            val: str
            if hasattr(start_date, "isoformat"): # Check for datetime duck typing
                val = start_date.isoformat() # type: ignore
            else:
                val = str(start_date)
            query_params.append(f"startDate={val}")
        if end_date is not None:
            val_end: str
            if hasattr(end_date, "isoformat"):
                val_end = end_date.isoformat() # type: ignore
            else:
                val_end = str(end_date)
            query_params.append(f"endDate={val_end}")

        query_string = "&".join(query_params)
        path = f"/domains/{domain_id}/stats?{query_string}" if query_string else f"/domains/{domain_id}/stats"
        data, err = self.unsent.get(path)
        return (data, err)  # type: ignore[return-value]


from .unsent import unsent  # noqa: E402  pylint: disable=wrong-import-position

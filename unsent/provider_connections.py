"""ProviderConnections resource client."""

from __future__ import annotations

from typing import Optional, Tuple, Dict, Any, Union

from .legacy_types import APIError
from .types import (
    ProviderConnectionsGetResponse,
    ProviderConnectionsPostRequest,
    ProviderConnectionsPostResponse,
    ProviderConnectionsIdDeleteResponse,
)


class ProviderConnections:
    """Client for `/provider-connections` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def list(self) -> Tuple[Optional[ProviderConnectionsGetResponse], Optional[APIError]]:
        data, err = self.unsent.get("/provider-connections")
        return (data, err)  # type: ignore[return-value]

    def create(self, payload: Union[ProviderConnectionsPostRequest, Dict[str, Any]]) -> Tuple[Optional[ProviderConnectionsPostResponse], Optional[APIError]]:
        body = payload
        if hasattr(payload, "model_dump"):
            body = payload.model_dump(by_alias=True, exclude_none=True) # type: ignore
        data, err = self.unsent.post("/provider-connections", body)
        return (data, err)  # type: ignore[return-value]

    def delete(self, id: str) -> Tuple[Optional[ProviderConnectionsIdDeleteResponse], Optional[APIError]]:
        data, err = self.unsent.delete(f"/provider-connections/{id}")
        return (data, err)  # type: ignore[return-value]


from .unsent import unsent  # noqa: E402  pylint: disable=wrong-import-position

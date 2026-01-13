"""Webhook resource client.

Note: Webhooks functionality is currently under development in the API.
This module provides a placeholder implementation for when the feature becomes available.
"""
from __future__ import annotations

from typing import Optional, Tuple, Dict, Any, List, Union

from .legacy_types import APIError


from .types import (
    WebhooksGetResponse,
    WebhooksPostRequest,
    WebhooksPostResponse,
    WebhooksIdGetResponse,
    WebhooksIdPatchRequest,
    WebhooksIdPatchResponse,
    WebhooksIdDeleteResponse,
)

class Webhooks:
    """Client for `/webhooks` endpoints."""

    def __init__(self, unsent: "unsent") -> None:
        self.unsent = unsent

    def list(self) -> Tuple[Optional[WebhooksGetResponse], Optional[APIError]]:
        data, err = self.unsent.get("/webhooks")
        return (data, err)  # type: ignore[return-value]

    def create(
        self, payload: Union[WebhooksPostRequest, Dict[str, Any]]
    ) -> Tuple[Optional[WebhooksPostResponse], Optional[APIError]]:
        body = payload
        if hasattr(payload, "model_dump"):
            body = payload.model_dump(by_alias=True, exclude_none=True) # type: ignore
        data, err = self.unsent.post("/webhooks", body)
        return (data, err)  # type: ignore[return-value]

    def get(self, webhook_id: str) -> Tuple[Optional[WebhooksIdGetResponse], Optional[APIError]]:
        data, err = self.unsent.get(f"/webhooks/{webhook_id}")
        return (data, err)  # type: ignore[return-value]

    def update(
        self, webhook_id: str, payload: Union[WebhooksIdPatchRequest, Dict[str, Any]]
    ) -> Tuple[Optional[WebhooksIdPatchResponse], Optional[APIError]]:
        body = payload
        if hasattr(payload, "model_dump"):
            body = payload.model_dump(by_alias=True, exclude_none=True) # type: ignore
        data, err = self.unsent.patch(f"/webhooks/{webhook_id}", body)
        return (data, err)  # type: ignore[return-value]

    def delete(
        self, webhook_id: str
    ) -> Tuple[Optional[WebhooksIdDeleteResponse], Optional[APIError]]:
        data, err = self.unsent.delete(f"/webhooks/{webhook_id}")
        return (data, err)  # type: ignore[return-value]

    def test(
        self, webhook_id: str
    ) -> Tuple[Optional[Dict[str, Any]], Optional[APIError]]:
        """Trigger a test event for a webhook."""
        data, err = self.unsent.post(f"/webhooks/{webhook_id}/test", {})
        return (data, err)  # type: ignore[return-value]


from .unsent import unsent  # noqa: E402

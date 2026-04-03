"""Settings for the observability MCP server."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings


class ObsSettings(BaseSettings):
    victorialogs_url: str = Field(
        default="http://localhost:9428",
        alias="NANOBOT_VICTORIALOGS_URL",
    )
    victoriatraces_url: str = Field(
        default="http://localhost:10428",
        alias="NANOBOT_VICTORIATRACES_URL",
    )


def resolve_settings() -> ObsSettings:
    return ObsSettings.model_validate({})

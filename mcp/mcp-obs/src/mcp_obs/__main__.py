"""Entry point for running the observability MCP server as a module."""

import asyncio

from mcp_obs.server import main

asyncio.run(main())

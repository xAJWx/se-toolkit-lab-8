#!/usr/bin/env python3
"""Query the LMS backend for available labs."""
import httpx
import asyncio
import json
import os

async def main():
    base_url = os.environ.get("NANOBOT_LMS_BACKEND_URL", "http://127.0.0.1:42001")
    api_key = os.environ.get("NANOBOT_LMS_API_KEY", os.environ.get("LMS_API_KEY", "my-secret-api-key"))
    
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    
    async with httpx.AsyncClient(base_url=base_url, headers=headers, timeout=10.0) as client:
        resp = await client.get("/items/")
        resp.raise_for_status()
        items = resp.json()
        labs = [i for i in items if i.get("type") == "lab"]
        print(json.dumps(labs, indent=2))

asyncio.run(main())

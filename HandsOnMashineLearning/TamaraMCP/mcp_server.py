#!/usr/bin/env python3
"""
MCP Server für Facade API
Bietet drei Tools für die Endpoints: v1/tamara, v1/ask, v1/hybridSearch
"""

import asyncio
import json
from typing import Any
import httpx
from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from mcp.server.stdio import stdio_server

# Konfiguration - passe diese Werte an deine Facade an
FACADE_BASE_URL = "http://localhost:8080"  # Beispiel-URL, anpassen!
# Falls Authentication nötig ist:
API_KEY = None  # Setze hier deinen API Key ein, falls benötigt

# Server initialisieren
app = Server("facade-mcp-server")

# HTTP Client für API-Aufrufe
http_client = httpx.AsyncClient(timeout=30.0)


def get_headers() -> dict[str, str]:
    """Erstelle Headers für API-Requests"""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers


@app.list_tools()
async def list_tools() -> list[Tool]:
    """Liste alle verfügbaren Tools"""
    return [
        Tool(
            name="tamara",
            description="Ruft den v1/tamara Endpoint auf. Nutze dieses Tool für Tamara-spezifische Anfragen.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Die Anfrage an Tamara"
                    },
                    "parameters": {
                        "type": "object",
                        "description": "Zusätzliche Parameter (optional)",
                        "additionalProperties": True
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="ask",
            description="Ruft den v1/ask Endpoint auf. Nutze dieses Tool für allgemeine Fragen.",
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "Die Frage, die gestellt werden soll"
                    },
                    "context": {
                        "type": "string",
                        "description": "Zusätzlicher Kontext (optional)"
                    },
                    "parameters": {
                        "type": "object",
                        "description": "Zusätzliche Parameter (optional)",
                        "additionalProperties": True
                    }
                },
                "required": ["question"]
            }
        ),
        Tool(
            name="hybrid_search",
            description="Ruft den v1/hybridSearch Endpoint auf. Nutze dieses Tool für hybride Suchvorgänge.",
            inputSchema={
                "type": "object",
                "properties": {
                    "search_query": {
                        "type": "string",
                        "description": "Die Suchanfrage"
                    },
                    "filters": {
                        "type": "object",
                        "description": "Suchfilter (optional)",
                        "additionalProperties": True
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximale Anzahl der Ergebnisse",
                        "default": 10
                    }
                },
                "required": ["search_query"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Führe ein Tool aus"""
    
    try:
        if name == "tamara":
            # v1/tamara Endpoint
            payload = {
                "query": arguments.get("query"),
                **(arguments.get("parameters", {}))
            }
            
            response = await http_client.post(
                f"{FACADE_BASE_URL}/v1/tamara",
                json=payload,
                headers=get_headers()
            )
            response.raise_for_status()
            result = response.json()
            
            return [TextContent(
                type="text",
                text=f"Tamara Response:\n{json.dumps(result, indent=2, ensure_ascii=False)}"
            )]
        
        elif name == "ask":
            # v1/ask Endpoint
            payload = {
                "question": arguments.get("question"),
                **({"context": arguments["context"]} if arguments.get("context") else {}),
                **(arguments.get("parameters", {}))
            }
            
            response = await http_client.post(
                f"{FACADE_BASE_URL}/v1/ask",
                json=payload,
                headers=get_headers()
            )
            response.raise_for_status()
            result = response.json()
            
            return [TextContent(
                type="text",
                text=f"Ask Response:\n{json.dumps(result, indent=2, ensure_ascii=False)}"
            )]
        
        elif name == "hybrid_search":
            # v1/hybridSearch Endpoint
            payload = {
                "query": arguments.get("search_query"),
                "limit": arguments.get("limit", 10),
                **({"filters": arguments["filters"]} if arguments.get("filters") else {})
            }
            
            response = await http_client.post(
                f"{FACADE_BASE_URL}/v1/hybridSearch",
                json=payload,
                headers=get_headers()
            )
            response.raise_for_status()
            result = response.json()
            
            return [TextContent(
                type="text",
                text=f"Hybrid Search Results:\n{json.dumps(result, indent=2, ensure_ascii=False)}"
            )]
        
        else:
            return [TextContent(
                type="text",
                text=f"Unbekanntes Tool: {name}"
            )]
    
    except httpx.HTTPStatusError as e:
        return [TextContent(
            type="text",
            text=f"HTTP Error {e.response.status_code}: {e.response.text}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Starte den MCP Server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

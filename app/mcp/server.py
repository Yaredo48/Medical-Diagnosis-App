# app/mcp/server.py
# This is a conceptual bridge for MCP

def get_tool_definitions():
    """Returns the JSON schema for our tools so an MCP host can read them."""
    return [
        {
            "name": "extract_symptoms",
            "description": "Extracts medical entities from raw text.",
            "input_schema": { "type": "object", "properties": { "text": {"type": "string"} } }
        },
        {
            "name": "pubmed_search",
            "description": "Searches for real medical papers.",
            "input_schema": { "type": "object", "properties": { "query": {"type": "string"} } }
        }
    ]
"""Lab 7.4: Tools as Capability Boundaries"""

def search_tool(query: str) -> dict:
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query required")
    if len(query) > 200:
        raise ValueError("query too long")
    return {"results": [f"hit for {query!r}"]}
for q in ["budget policy", "", 123]:
    try:
        print(search_tool(q) if isinstance(q, str) else search_tool(str(q)))
    except ValueError as e:
        print({"error": str(e)})

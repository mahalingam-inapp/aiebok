"""Lab 7.5: MCP and Integration Protocols"""

CHAPTER = "7.5"
print("chapter hook:", CHAPTER)
CLIENT_SCOPES = {"analyst": ["search_policy"]}
REQUEST = {"client": "analyst", "tool": "admin_delete"}
def authorize(client, tool):
    return tool in CLIENT_SCOPES.get(client, [])
print({"allowed": authorize(REQUEST["client"], REQUEST["tool"])})
print("---")
print("change one input above, predict output, re-run")

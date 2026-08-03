# Model Context Protocol Specification

## Citation

Anthropic. *Model Context Protocol Specification.* 2024. [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)

## One-sentence contribution

Standard for tools, resources, and prompts between clients and servers.

## Problem

Every LLM application implemented tool integration differently—custom JSON schemas, ad hoc auth, proprietary protocols. Tool providers had to build N integrations for N host applications, and developers could not swap tool backends without rewriting.

## Prior art

OpenAI function calling defined a schema format but not a transport or discovery protocol. LangChain tools were Python-specific with no standard wire format. LSP (Language Server Protocol) inspired the idea of a standard protocol but was code-editor-specific.

## Core idea

Anthropic's Model Context Protocol (MCP) defines a JSON-RPC 2.0 wire protocol between a host (LLM application) and servers (tool/data providers). Servers expose capabilities via three primitives: Tools (callable functions with JSON Schema inputs), Resources (readable data sources), and Prompts (templated prompt sequences). Discovery is dynamic—hosts query servers for available capabilities at connection time. Transport supports stdio (local) and SSE (remote). Auth and permissions are server-managed.

## Evidence

- Adopted by Claude Desktop, Cursor, Zed, and growing server ecosystem (100+ MCP servers).
- Server implementations exist for GitHub, Slack, Postgres, filesystem, and web search.
- Dynamic discovery enables hosts to expose only relevant tools per context.
- Separation of concerns: tool providers build one MCP server; hosts integrate once.

## Limitations

- Early specification—breaking changes possible as protocol matures.
- Security model still evolving (server sandboxing, permission scopes, audit logging).
- Transport fragmentation (stdio vs. SSE vs. future options) complicates deployment.
- No standard for streaming tool results or long-running operations.

## Lasting impact

MCP is becoming the USB-C of LLM tool integration—one protocol connecting hosts to tools, resources, and prompts. It reduces integration friction and enables an ecosystem of reusable tool servers.

## Reproduction exercise

Build a minimal MCP server exposing one tool (e.g., `get_weather(city)`) using the Python MCP SDK. Connect it to Claude Desktop or Cursor. Verify dynamic discovery, tool invocation, and error handling. Compare integration code against a bespoke function-calling implementation.

## Related chapters

- [05 Mcp And Integration Protocols](../../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md)
- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)
- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)

## Related concepts

- [Mcp](../../concepts/cards/mcp.md)
- [Tool Schemas](../../concepts/cards/tool-schemas.md)
- [Portable Interfaces](../../concepts/cards/portable-interfaces.md)

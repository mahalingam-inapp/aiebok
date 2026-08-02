"""Keep logical capabilities separate from provider mappings."""
CAPABILITIES = {
    "model_access": {"aws": "Bedrock", "azure": "Azure AI Foundry", "gcp": "Vertex AI"},
    "retrieval": {"aws": "OpenSearch", "azure": "Azure AI Search", "gcp": "Vertex AI Search"},
    "identity": {"aws": "IAM", "azure": "Entra ID", "gcp": "Cloud IAM"},
}


def architecture(provider):
    return {capability: services[provider] for capability, services in CAPABILITIES.items()}


for provider in ("aws", "azure", "gcp"):
    print(provider, architecture(provider))

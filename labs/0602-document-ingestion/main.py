"""Lab 6.2: Document Ingestion"""

manifest = {
    "doc_id": "POL-441",
    "pages": 12,
    "acl": "HR-ONLY",
    "chunks": [{"id": 1, "page": 3, "text_hash": "abc123"}],
}
def allowed(chunk, user_groups):
    required = manifest["acl"]
    return required in user_groups
user = {"groups": ["ALL-STAFF"]}
print({"access": allowed(manifest["chunks"][0], user["groups"])})

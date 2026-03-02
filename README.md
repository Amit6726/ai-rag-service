
# AI RAG Service

Small RAG (Retrieval-Augmented Generation) service. Project layout:

- `app/` - application entry and API routes
- `core/` - core logic (embeddings, helpers)
- `services/` - retriever and vector store implementations
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.10+ (3.11 used in the dev venv)
- `virtualenv` or `venv`

## Quick setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) run the app with Uvicorn:

```bash
uvicorn app.main:app --reload
```

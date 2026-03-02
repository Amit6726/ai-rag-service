
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

Adjust the command above if your entrypoint differs.

## Git / push to GitHub (SSH recommended)

The repo was initialized locally and a remote was added, but pushing over HTTPS failed due to permissions. I recommend using SSH to push. Example steps:

1. Generate an SSH key (if you don't already have one):

```bash
ssh-keygen -t ed25519 -C "amitrajput6726@gmail.com"
```

2. Copy the public key and add it to your GitHub account (https://github.com/settings/keys).

3. Switch the remote to SSH and push:

```bash
git remote set-url origin git@github.com:Amit6726/ai-rag-service.git
git push -u origin main
```

If you prefer HTTPS, authenticate using `gh auth login` or a Personal Access Token (PAT), then run:

```bash
git push -u origin main
```

## Notes

- A `.gitignore` was added to avoid committing the `venv` directory; make sure your local venv is not tracked.
- If the app entrypoint is different from `app.main:app`, update the run command accordingly.

If you want, I can attempt the SSH push now (I will change the remote to SSH and run `git push -u origin main`).

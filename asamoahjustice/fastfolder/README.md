uv venv

pip install "fastapi[standard]"

uv add "fastapi[standard]" uvicorn
uv init

uv main:app --reload

source .venv/Scripts/activate
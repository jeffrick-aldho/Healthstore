# Healthcare API

FastAPI + MongoDB backend scaffolded to match the required structure in `Healthcare.pdf`.

## Run

1. Create and activate virtual environment:
   - Windows PowerShell: `python -m venv .venv` then `.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Start API:
   - `uvicorn app.main:app --reload`

## Base URL

- `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`

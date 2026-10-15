# Assignment Bot

A simple chat bot built with [Streamlit](https://streamlit.io) and Google's Gemini API.

## Prerequisites

- Python 3.12 or newer
- A Gemini API key. You can get one free from [Google AI Studio](https://aistudio.google.com/apikey).

## Configure your API key

You can give the app your key in either of two ways:

1. **Sidebar:** start the app and paste the key into the "Gemini API key" field in the sidebar.
2. **`.env` file:** create a file named `.env` in the project root:

   ```env
   GEMINI_API_KEY=your-key-here
   ```

   `.env` is already listed in `.gitignore`, so it won't be committed.

If you enter a key in the sidebar, it takes priority over the one in `.env`.

## Run locally with Python (pip + venv)

1. Clone the repository and move into it:

   ```bash
   git clone <repo-url>
   cd bot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (cmd): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`

3. Install the project and its dependencies:

   ```bash
   pip install -e .
   ```

4. Start the app:

   ```bash
   streamlit run src/bot/app.py
   ```

   Streamlit opens the app in your browser at <http://localhost:8501>.

## Run locally with uv

[uv](https://docs.astral.sh/uv/) installs the exact dependency versions pinned in `uv.lock` and manages the virtual environment for you.

1. Install uv if you don't have it:

   - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

2. Install the dependencies. uv creates `.venv` and, if needed, downloads Python 3.12 (the version in `.python-version`):

   ```bash
   uv sync
   ```

3. Start the app:

   ```bash
   uv run streamlit run src/bot/app.py
   ```

   You don't need to activate the virtual environment, because `uv run` uses it automatically.

### Adding dependencies

Add new packages with `uv add` so that both `pyproject.toml` and `uv.lock` are updated:

```bash
uv add <package-name>
```

Don't install packages with `pip install` alone. Streamlit Cloud installs from `uv.lock`, so a package that isn't in the lockfile will be missing when the app is deployed.

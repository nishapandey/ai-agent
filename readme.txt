AI Research Agent (LangChain + Anthropic)

This project is a simple research assistant built with LangChain tool-calling, backed by Anthropic Claude. It can search the web (DuckDuckGo), read Wikipedia, and optionally save results to `research_output.txt` via a save tool.

Setup
1. Create a `.env` file in the project root with:
   ANTHROPIC_API_KEY=your_api_key_here
   # Optional (defaults to the value used in code)
   ANTHROPIC_MODEL=claude-opus-4-1-20250805

2. Create and activate a virtual environment, then install dependencies:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. Run the app:
   python3 main.py
   # Alternatively: bash startup.sh (expects deps already installed)

Usage
- When prompted with "Enter a query:", type your research question.
- The agent may call tools:
  - search: DuckDuckGo web search
  - wikipedia: Wikipedia lookup
  - save_text_to_file: appends structured text to `research_output.txt`
- The program prints the parsed topic. Additional fields may be printed/saved depending on tool usage and prompt behavior.

Notes
- If you see "Missing ANTHROPIC_API_KEY", ensure `.env` exists and contains ANTHROPIC_API_KEY.
- Ensure your network permits requests to DuckDuckGo and Wikipedia.
- Dependencies are listed in `requirements.txt`. If you change models, adjust `ANTHROPIC_MODEL` in `.env` accordingly.
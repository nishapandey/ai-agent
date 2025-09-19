Developed an AI agent using LangChain that integrates with external tools and generates responses powered by OpenAI GPT models

Setup
1. Create a .env file in the project root with:
   OPENAI_API_KEY=your_api_key_here
   # Optional, defaults to gpt-4o-mini
   OPENAI_MODEL=gpt-4o-mini

2. Run the startup script (creates venv, installs deps, runs the app):
   bash startup.sh

Notes
- The agent uses OpenAI via LangChain. Ensure the API key is valid.
- If you see an authentication error, double-check that `.env` exists and contains OPENAI_API_KEY.
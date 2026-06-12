# config.py

from pathlib import Path

# Root directory to search
# Change this to any folder you want the agent to scan

SEARCH_ROOT = str(Path.home())

# SQLite database path
DATABASE_PATH = "data/memory.db"

# Ollama model
OLLAMA_MODEL = "llama3.2"

# Max characters sent to LLM for summarization
MAX_SUMMARY_CHARS = 12000

# Console title
APP_NAME = "FileMind AI Agent"
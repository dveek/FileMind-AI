# tools.py

from config import SEARCH_ROOT, MAX_SUMMARY_CHARS
from utils.file_search import search_files
from utils.pdf_reader import extract_text
from utils.duplicate_finder import find_duplicates
from ollama_client import chat


def file_search_tool(keyword):

    results = search_files(SEARCH_ROOT, keyword)

    if not results:
        return "No matching files found."

    output = "\n".join(results[:50])

    if len(results) > 50:
        output += f"\n\n... and {len(results)-50} more files"

    return output


def pdf_summary_tool(pdf_path):

    try:

        text = extract_text(pdf_path)

        if not text.strip():
            return "PDF contains no readable text."

        text = text[:MAX_SUMMARY_CHARS]

        prompt = f"""
You are an expert document summarizer.

Summarize the following PDF content.

CONTENT:
{text}
"""

        return chat(prompt)

    except Exception as e:

        return f"Failed to read PDF: {e}"


def duplicate_finder_tool():

    duplicates = find_duplicates(SEARCH_ROOT)

    if not duplicates:
        return "No duplicate files found."

    output = []

    for original, duplicate in duplicates[:50]:

        output.append(
            f"\nORIGINAL:\n{original}\n\nDUPLICATE:\n{duplicate}\n"
        )

    return "\n".join(output)
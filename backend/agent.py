# agent.py

import os

from tools import (
    file_search_tool,
    pdf_summary_tool,
    duplicate_finder_tool
)

from ollama_client import chat


SYSTEM_PROMPT = """
You are FileMind AI Agent.

Available tools:

1. SEARCH_FILE
   Purpose:
   Search files by filename keyword.

2. SUMMARIZE_PDF
   Purpose:
   Summarize a PDF document.

3. FIND_DUPLICATES
   Purpose:
   Find duplicate files.

RULES:

Return ONLY one of these formats:

TOOL: SEARCH_FILE
ARG: keyword

OR

TOOL: SUMMARIZE_PDF
ARG: full_file_path

OR

TOOL: FIND_DUPLICATES
ARG: none

Do not explain.
"""


class Agent:

    def decide(self, user_query):

        prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}
"""

        response = chat(prompt)

        return response

    def execute(self, user_query):

        decision = self.decide(user_query)
        print("\n=== RAW LLM RESPONSE ===")
        print(decision)
        print("========================\n")

        try:

            lines = decision.splitlines()

            tool = ""
            arg = ""

            for line in lines:

                if line.startswith("TOOL:"):
                    tool = line.replace("TOOL:", "").strip()

                elif line.startswith("ARG:"):
                    arg = line.replace("ARG:", "").strip()

            if tool == "SEARCH_FILE":

                return file_search_tool(arg)

            elif tool == "SUMMARIZE_PDF":

                if not os.path.exists(arg):
                    return (
                        "File not found.\n"
                        "Provide the full PDF path."
                    )

                return pdf_summary_tool(arg)

            elif tool == "FIND_DUPLICATES":

                return duplicate_finder_tool()

            else:

                return (
                    "Agent could not determine "
                    "which tool to use."
                )

        except Exception as e:

            return f"Agent Error: {e}"
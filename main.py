# main.py

from rich.console import Console
from rich.panel import Panel

from agent import Agent
from memory import Memory
from config import APP_NAME


console = Console()

agent = Agent()

memory = Memory()

print("MAIN.PY IS RUNNING")
def banner():

    console.print(
        Panel.fit(
            f"{APP_NAME}\n"
            "Local AI File System Agent\n"
            "Powered by Ollama Llama 3.2"
        )
    )


def show_help():

    console.print("""
Commands:

help
history
exit

Examples:

find dbms pdf files

find weather app project

find duplicate files

summarize C:\\notes\\dbms.pdf
""")


def show_history():

    rows = memory.recent()

    if not rows:
        console.print("No history.")
        return

    for command, result in rows:

        console.print("\n[cyan]Command:[/cyan]")
        console.print(command)

        console.print("[green]Result:[/green]")
        console.print(result[:300])

        console.print("-" * 50)


def main():

    banner()

    while True:

        query = input("\nFileMind > ")

        query = query.strip()

        if not query:
            continue

        if query.lower() == "exit":
            break

        if query.lower() == "help":
            show_help()
            continue

        if query.lower() == "history":
            show_history()
            continue

        console.print(
            "\n[yellow]Thinking...[/yellow]"
        )

        result = agent.execute(query)

        console.print(
            Panel(
                result,
                title="Result"
            )
        )

        memory.save(query, result)


if __name__ == "__main__":
    main()
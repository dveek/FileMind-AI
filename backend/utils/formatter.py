# utils/formatter.py

from rich.console import Console

console = Console()


def success(message):
    console.print(f"[green]{message}[/green]")


def error(message):
    console.print(f"[red]{message}[/red]")


def info(message):
    console.print(f"[cyan]{message}[/cyan]")
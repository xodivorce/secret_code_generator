from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich.rule import Rule
from rich import box
import time

console = Console()

def encode_message(message, shift):
    encoded = ""
    for char in message:
        if char.isupper():
            encoded += chr(((ord(char) - 65 + shift) % 26) + 65)
        elif char.islower():
            encoded += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            encoded += char
    return encoded

def decode_message(message, shift):
    decoded = ""
    for char in message:
        if char.isupper():
            decoded += chr(((ord(char) - 65 - shift) % 26) + 65)
        elif char.islower():
            decoded += chr(((ord(char) - 97 - shift) % 26) + 97)
        else:
            decoded += char
    return decoded

def create_header():
    title = Text("\u2003\u2003🔐 SECRET CODE GENERATOR 🔐\u2003", style="bold bright_cyan")
    subtitle = Text("◆ Encode And Decode Messages ◆", style="dim bright_magenta")
    return Panel(
        Align.center(title + "\n" + subtitle),
        style="bold bright_blue",
        box=box.DOUBLE,
        padding=(1, 2)
    )

def create_menu():
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(style="bold bright_green", width=3)
    table.add_column(style="bright_white")
    table.add_column(style="dim")
    
    table.add_row("1", "📝 Encode Message", "Transform your text into secret code")
    table.add_row("2", "🔍 Decode Message", "Reveal hidden messages")
    table.add_row("3", "🚪 Exit Program", "Close the application")
    
    return Panel(
        table,
        title="[bold bright_yellow]⚡ MAIN MENU ⚡[/bold bright_yellow]",
        title_align="center",
        border_style="bright_yellow",
        padding=(1, 2)
    )

def show_result(result_text, is_encoded=True):
    operation = "ENCODED" if is_encoded else "DECODED"
    emoji = "🔒" if is_encoded else "🔓"
    color = "bright_green" if is_encoded else "bright_cyan"
    
    result_panel = Panel(
        f"[bold {color}]{result_text}[/bold {color}]",
        title=f"[bold bright_white]{emoji} {operation} MESSAGE {emoji}[/bold bright_white]",
        title_align="center",
        border_style=color,
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(result_panel)
    console.print("\n")

def display_menu():
    while True:
        console.clear()
        
        console.print(create_header())
        console.print()
        console.print(create_menu())
        console.print()
        
        choice = Prompt.ask(
            "[bold bright_white]❯ Select your choice",
            choices=["1", "2", "3"],
            default="1"
        )
        
        console.print()
        
        if choice == "1":
            console.print(Rule("[bold bright_green]🔒 ENCODING MODE[/bold bright_green]", style="bright_green"))
            console.print()
            
            message = Prompt.ask("📝 [bold bright_white]Enter message to encode")
            shift = IntPrompt.ask("🔢 [bold bright_white]Enter shift value", default=3)
            
            console.print("\n[dim bright_blue]⚡ Processing...[/dim bright_blue]")
            time.sleep(0.5)
            
            encoded = encode_message(message, shift)
            show_result(encoded, is_encoded=True)
            
        elif choice == "2":
            console.print(Rule("[bold bright_cyan]🔓 DECODING MODE[/bold bright_cyan]", style="bright_cyan"))
            console.print()
            
            message = Prompt.ask("🔍 [bold bright_white]Enter message to decode")
            shift = IntPrompt.ask("🔢 [bold bright_white]Enter shift value", default=3)
            
            console.print("\n[dim bright_blue]⚡ Processing...[/dim bright_blue]")
            time.sleep(0.5)
            
            decoded = decode_message(message, shift)
            show_result(decoded, is_encoded=False)
            
        elif choice == "3":
            console.print()
            farewell = Panel(
                Align.center(
                    "[bold bright_red] 🚪 Thank you for using SECRET CODE GENERATOR! 🚪\n"
                    "[dim]◆ We hope you really enjoyed this tool. Goodbye! ◆[/dim]"
                ),
                style="bold bright_red",
                box=box.DOUBLE
            )
            console.print(farewell)
            console.print()
            break
        
        if choice in ["1", "2"]:
            Prompt.ask("\n[bold bright_yellow]Press [bright_white]Enter[/bright_white] to return to main menu[/bold bright_yellow]")

if __name__ == "__main__":
    display_menu()
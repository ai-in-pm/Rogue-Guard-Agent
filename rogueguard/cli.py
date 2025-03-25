import click
from rich.console import Console
from .models.guard import RogueGuard
from .config.settings import settings
import os
import sys

console = Console()

@click.group()
def cli():
    """RogueGuard - Advanced AI Behavior Analysis System"""
    pass

@cli.command()
@click.option('--api-key', help='OpenAI API key')
def configure(api_key):
    """Configure RogueGuard settings"""
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        console.print("[green]API key configured successfully[/green]")
    else:
        console.print("[yellow]Please provide an API key using --api-key[/yellow]")

@cli.command()
def monitor():
    """Start interactive monitoring session"""
    try:
        if not os.getenv('OPENAI_API_KEY'):
            console.print("[red]Error: OpenAI API key not found. Use 'rogueguard configure --api-key YOUR_KEY' to set it.[/red]")
            sys.exit(1)
            
        console.print("[bold red]RogueWatch - AI Behavior Analysis System[/bold red]")
        console.print("[italic]Type 'exit' to quit[/italic]\n")
        
        guard = RogueGuard()
        
        while True:
            try:
                user_input = input("🔍 > ")
                if user_input.lower() == 'exit':
                    break
                
                analysis = guard.analyze_interaction(user_input)
                guard.display_analysis(analysis)
                print()
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[red]Error: {str(e)}[/red]")
        
        console.print("\n[bold red]Shutting down RogueWatch. Stay vigilant![/bold red]")
        
    except Exception as e:
        console.print(f"[red]Fatal error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('file', type=click.Path(exists=True))
def analyze_file(file):
    """Analyze AI responses from a file"""
    try:
        guard = RogueGuard()
        
        with open(file, 'r') as f:
            content = f.read()
            
        analysis = guard.analyze_interaction(content)
        guard.display_analysis(analysis)
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

def main():
    """Main entry point for the CLI"""
    cli()

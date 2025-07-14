import typer
from core.pipeline import Pipeline
from core.utils import setup_logging

app = typer.Typer()

@app.command()
def main():
    setup_logging()
    typer.echo("Welcome to metaGPT CLI!")
    user_input = typer.prompt("Enter your project idea")
    pipeline = Pipeline()
    results = pipeline.run(user_input)
    typer.echo("\n--- Product Requirements ---\n")
    typer.echo(results["requirements"])
    typer.echo("\n--- Project Plan ---\n")
    typer.echo(results["project_plan"])
    typer.echo("\n--- Architecture ---\n")
    typer.echo(results["architecture"])
    typer.echo("\n--- Code / Pseudocode ---\n")
    typer.echo(results["code"])
    typer.echo("\n--- QA Report ---\n")
    typer.echo(results["qa_report"])

if __name__ == "__main__":
    app()

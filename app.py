import click
from utils.data_handler import save_transaction, load_data
from utils.visualizer import plot_expense_distribution

@click.group()
def cli():
    """Budget Tracker CLI"""
    pass

@cli.command()
@click.option("--date", prompt="Date (YYYY-MM-DD)", help="Transaction date")
@click.option("--category", prompt="Category", help="Transaction category")
@click.option("--amount", type=float, prompt="Amount", help="Transaction amount")
def add(date, category, amount):
    """Add a new transaction."""
    save_transaction(date, category, amount)
    click.echo("Transaction added successfully!")

@cli.command()
def summary():
    """Show monthly summary."""
    df = load_data()
    income = df[df["Amount"] > 0]["Amount"].sum()
    expenses = df[df["Amount"] < 0]["Amount"].sum()
    balance = income + expenses

    click.echo(f"Total Income: {income}")
    click.echo(f"Total Expenses: {expenses}")
    click.echo(f"Balance: {balance}")

@cli.command()
def visualize():
    """Visualize expense distribution."""
    plot_expense_distribution()

if __name__ == "__main__":
    cli()

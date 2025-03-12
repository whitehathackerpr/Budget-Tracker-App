import matplotlib.pyplot as plt
from utils.data_handler import load_data

def plot_expense_distribution():
    df = load_data()  # Use our safe data-loading function
    if df.empty:
        print("No transactions available.")
        return
    category_totals = df.groupby("Category")["Amount"].sum()
    category_totals.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.show()

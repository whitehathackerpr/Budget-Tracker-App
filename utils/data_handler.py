import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/transactions.csv")

def load_data():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(exist_ok=True)
        df = pd.DataFrame(columns=["Date", "Category", "Amount"])
        df.to_csv(DATA_FILE, index=False)
    else:
        try:
            df = pd.read_csv(DATA_FILE)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=["Date", "Category", "Amount"])
            df.to_csv(DATA_FILE, index=False)
    return df

def save_transaction(date, category, amount):
    df = load_data()
    new_transaction = pd.DataFrame([{"Date": date, "Category": category, "Amount": amount}])
    df = pd.concat([df, new_transaction], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

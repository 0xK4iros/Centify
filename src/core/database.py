import pathlib
import pandas as pd
import uuid

#  Get the path of the database file
path = pathlib.Path(__file__).parent.parent.parent

#  Initialize the database
def init_db():
    if not (path / "data"/ "transactions.csv").exists():
        (path / "data").mkdir(parents=True, exist_ok=True)
        pd.DataFrame(columns=["transaction_id", "date", "description", "category", "type",
                              "amount"]).to_csv(path / "data" / "transactions.csv", index=False)


#  Load transactions from the database
def load_transactions():
    try:
        return pd.read_csv(path / "data" / "transactions.csv", index_col=None, parse_dates=['date'])
    except (FileNotFoundError, IOError, pd.errors.EmptyDataError):
            init_db()
            return load_transactions()
    
#  Save transactions to the database
def save_transactions(date, description, category, type, amount):
    transaction_id = str(uuid.uuid4())
    new_transaction = pd.DataFrame({
        "transaction_id": [transaction_id],
        "date": [date],
        "description": [description],
        "category": [category],
        "type": [type],
        "amount": [amount]
    })
    new_transaction.to_csv(path / "data" / "transactions.csv", header=False, mode="a", index=False)




init_db()
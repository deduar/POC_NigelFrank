import pandas as pd
from .config import REQUIRED_COLUMNS


def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"transaction_id": str, "customer_id": str})
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df
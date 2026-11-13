import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
n = 100_000
df = pd.DataFrame({
    "transaction_id": [f"T{i:06d}" for i in range(n)],
    "customer_id": [f"C{rng.integers(1, 5000):04d}" for _ in range(n)],
    "product": rng.choice(["A", "B", "C"], n),
    "quantity": rng.integers(1, 10, n),
    "unit_price": np.round(rng.uniform(5, 200, n), 2),
    "timestamp": pd.date_range("2024-01-01", periods=n, freq="min"),
    "region": rng.choice([" EU ", "us", "LATAM"], n),
    "status": rng.choice(["ok", "ok", "ok", "pending"], n),
})
Path("data/generated").mkdir(parents=True, exist_ok=True)
df.to_csv("data/generated/transactions_large.csv", index=False)
print("generated", len(df))
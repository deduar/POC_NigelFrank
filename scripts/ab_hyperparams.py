# Helper (Jupyter-exported): A/B exploration of transform thresholds.
# Run: python scripts/ab_hyperparams.py
import pandas as pd
from src.pipeline.ingest import load_csv
from src.pipeline.transform import transform

df = load_csv("data/sample/transactions.csv")
t = transform(df)
print(t.groupby("discount_tier")["total_amount"].agg(["count", "mean"]))
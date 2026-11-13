import numpy as np
import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    # vectorized with numpy
    out["total_amount"] = np.round(out["quantity"].to_numpy() * out["unit_price"].to_numpy(), 2)
    out["discount_tier"] = np.where(out["total_amount"] >= 100, "high", "low")
    out["month"] = out["timestamp"].dt.to_period("M").astype(str)
    out["region"] = out["region"].str.strip().str.lower()
    # customer lifetime aggregates
    agg = out.groupby("customer_id")["total_amount"].transform("sum")
    out["customer_lifetime_value"] = np.round(agg.to_numpy(), 2)
    return out
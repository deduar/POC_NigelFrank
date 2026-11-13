import pandas as pd
from src.pipeline.transform import transform


def test_transform_adds_total():
    df = pd.DataFrame({
        "transaction_id": ["1"],
        "customer_id": ["c1"],
        "product": ["A"],
        "quantity": [2],
        "unit_price": [10.0],
        "timestamp": pd.to_datetime(["2024-01-01"]),
        "region": [" EU "],
        "status": ["ok"],
    })
    out = transform(df)
    assert "total_amount" in out.columns
    assert out["total_amount"].iloc[0] == 20.0
    assert out["region"].iloc[0] == "eu"
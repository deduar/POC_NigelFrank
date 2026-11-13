import pandas as pd
import pytest
from src.pipeline.validate import validate, ValidationError


def test_validate_ok():
    df = pd.DataFrame({
        "transaction_id": ["1", "2"],
        "customer_id": ["c1", "c2"],
        "product": ["A", "B"],
        "quantity": [1, 2],
        "unit_price": [10.0, 5.0],
        "timestamp": pd.to_datetime(["2024-01-01", "2024-01-02"]),
        "region": ["eu", "us"],
        "status": ["ok", "ok"],
    })
    rep = validate(df)
    assert rep["rows"] == 2


def test_validate_duplicate_raises():
    df = pd.DataFrame({
        "transaction_id": ["1", "1"],
        "customer_id": ["c1", "c2"],
        "product": ["A", "B"],
        "quantity": [1, 2],
        "unit_price": [10.0, 5.0],
        "timestamp": pd.to_datetime(["2024-01-01", "2024-01-02"]),
        "region": ["eu", "us"],
        "status": ["ok", "ok"],
    })
    with pytest.raises(ValidationError):
        validate(df)
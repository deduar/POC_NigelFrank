import pandas as pd
from .config import NULLABLE_OK, MAX_NULL_RATIO


class ValidationError(Exception):
    pass


def validate(df: pd.DataFrame) -> dict:
    report = {"rows": len(df), "nulls": {}, "duplicates": 0, "failed": 0}
    # null ratio check
    for col in df.columns:
        if col in NULLABLE_OK:
            continue
        ratio = df[col].isna().mean()
        report["nulls"][col] = int(df[col].isna().sum())
        if ratio > MAX_NULL_RATIO:
            raise ValidationError(f"Column {col} null ratio {ratio:.3f} > {MAX_NULL_RATIO}")
    # duplicate transaction ids
    dups = df["transaction_id"].duplicated().sum()
    report["duplicates"] = int(dups)
    if dups > 0:
        raise ValidationError(f"Duplicate transaction_id: {dups}")
    # business rule: quantity > 0, unit_price >= 0
    bad = (df["quantity"] <= 0) | (df["unit_price"] < 0)
    report["failed"] = int(bad.sum())
    if bad.any():
        raise ValidationError(f"Invalid rows: {int(bad.sum())}")
    return report
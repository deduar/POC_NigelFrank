import pandas as pd
from sqlalchemy import create_engine


def load(df: pd.DataFrame, db_url: str, table: str = "transactions") -> int:
    engine = create_engine(db_url)
    df.to_sql(table, engine, if_exists="replace", index=False)
    return len(df)
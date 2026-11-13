import tempfile, os
import pandas as pd
from src.pipeline.ingest import load_csv
from src.pipeline.runner import run


def test_e2e_sample():
    r = run("data/sample/transactions.csv")
    assert r["loaded"] > 0
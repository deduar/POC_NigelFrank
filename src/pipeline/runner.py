import json
from pathlib import Path

from .config import SAMPLE_CSV, DB_URL
from .ingest import load_csv
from .transform import transform
from .validate import validate
from .load import load


def run(csv_path: str = str(SAMPLE_CSV)) -> dict:
    raw = load_csv(csv_path)
    clean_validated = validate(raw)
    transformed = transform(raw)
    validate(transformed)
    n = load(transformed, DB_URL)
    report = {"ingested": len(raw), "quality": clean_validated, "loaded": n}
    Path("data").mkdir(exist_ok=True)
    Path("data/quality_report.json").write_text(json.dumps(report, indent=2, default=str))
    return report


if __name__ == "__main__":
    print(run())
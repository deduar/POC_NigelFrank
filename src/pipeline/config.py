from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
SAMPLE_CSV = DATA_DIR / "sample" / "transactions.csv"
DB_URL = "sqlite:///data/output.db"

REQUIRED_COLUMNS = ["transaction_id", "customer_id", "product", "quantity", "unit_price", "timestamp", "region", "status"]
NULLABLE_OK = ["product"]
MAX_NULL_RATIO = 0.01
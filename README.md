# POC — Lead Python Data Engineer

KISS proof-of-concept: a sales transactions ETL pipeline in Python/Pandas/NumPy with data quality validation, tests, and CI/CD. Demonstrates the core required skills of the Lead Python Data Engineer role.

## Run
```bash
pip install -r requirements.txt
python -m src.pipeline.runner
pytest
```

## Docker
```bash
docker compose up --build
```

## Architecture
Ingest (CSV) -> Validate (schema + business rules) -> Transform (Pandas/NumPy vectorized) -> Validate -> Load (SQLite/SQLAlchemy) -> Quality report.

## Performance
Vectorized transforms vs. row-wise loops; see scripts/baseline_report.py.

## Production next steps
Spark/Databricks, Azure (ADF, ADLS, Delta Lake), dbt, Airflow, monitoring, auth, K8s. Jupyter helpers live in scripts/ and notebooks/ (helper only; main dev is containerized).# POC_NigelFrank

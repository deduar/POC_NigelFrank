#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
echo "=== POC demo run ==="
docker compose up --build --abort-on-container-exit 2>&1 | tee run_evidence.log
echo "=== Tests ==="
docker run --rm -v "$(pwd)":/app -w /app poc-app:latest sh -c "pip install -q pytest ruff black && pytest -q" 2>&1 | tee -a run_evidence.log
echo "DONE"
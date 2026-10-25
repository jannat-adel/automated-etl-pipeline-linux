#!/bin/bash

PROJECT_DIR="/home/jannat/data-pipeline-project"

echo "=========================================="
echo "Pipeline Started at: $(date)"
echo "=========================================="


echo "[1/3] Fetching raw data..."
python3 "$PROJECT_DIR/scripts/fetch_data.py"


echo "[2/3] Transforming data..."
python3 "$PROJECT_DIR/scripts/transform_data.py"


echo "[3/3] Running backup..."
bash "$PROJECT_DIR/scripts/backup.sh"

echo "=========================================="
echo "Pipeline Finished Successfully at: $(date)"
echo "=========================================="

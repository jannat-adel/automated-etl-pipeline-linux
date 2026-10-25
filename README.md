🔄 Automated End-to-End Data Pipeline (ETL) with Bash & Python

An automated, lightweight ETL (Extract, Transform, Load) pipeline built on Linux using Python for data processing and Bash for process orchestration and backup automation via system `crontab`.

---

📌 Architecture & Features

- **Ingestion (`fetch_data.py`):** Generates/fetches raw transactional data and stores it in timestamped `.csv` files.
- **Transformation (`transform_data.py`):** Cleans raw data, applies basic transformations, and saves structured outputs.
- **Backup Automation (`backup.sh`):** Compresses and archives processed and raw data into compressed `.tar.gz` backups.
- **Automation & Logging (`Crontab` + `run_pipeline.sh`):** Runs tasks automatically on schedule and logs all operations and execution status to `pipeline.log`.

---

 🛠 Project Structure

```text
data-pipeline-project/
│
├── raw_data/          # Ingested raw datasets
├── processed_data/    # Cleaned & transformed datasets
├── backups/           # Compressed archives (.tar.gz)
├── logs/              # Pipeline execution logs (pipeline.log)
└── scripts/           # Core scripts
    ├── fetch_data.py
    ├── transform_data.py
    ├── backup.sh
    └── run_pipeline.sh

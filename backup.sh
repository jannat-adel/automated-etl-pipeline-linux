#!/bin/bash
BACKUP_DIR="/home/jannat/data-pipeline-project/backups"
PROJECT_DIR="/home/jannat/data-pipeline-project"

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz" -C "$PROJECT_DIR" raw_data processed_data
echo "Backup completed successfully!"

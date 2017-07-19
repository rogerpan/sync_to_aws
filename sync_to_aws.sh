#!/bin/bash
date
time /root/.local/bin/aws s3 sync --quiet /data/mssql s3://datg-databases-backup/mssql --sse=AES256

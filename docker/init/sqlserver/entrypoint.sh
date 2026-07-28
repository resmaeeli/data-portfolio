#!/bin/bash

echo "SQL Server entrypoint started..."

# Start SQL Server in background
/opt/mssql/bin/sqlservr &

echo "SQL Server process started."

# Run database initialization
bash /init/setup.sh

# Keep SQL Server process alive
wait
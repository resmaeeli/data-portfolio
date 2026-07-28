#!/bin/bash

echo "Waiting for SQL Server..."

# Wait for SQL Server service
until /opt/mssql-tools18/bin/sqlcmd \
-S localhost \
-U sa \
-P "YourStrong@Pass123" \
-C \
-Q "SELECT 1" > /dev/null 2>&1
do
    sleep 5
done

echo "SQL Server is ready."


# Restore AdventureWorks database
echo "Restoring AdventureWorks database..."

/opt/mssql-tools18/bin/sqlcmd \
-S localhost \
-U sa \
-P "YourStrong@Pass123" \
-C \
-i /init/restore.sql

echo "Restore completed."
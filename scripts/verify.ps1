$ErrorActionPreference = "Stop"

Write-Host "Running installation verification..."


# Check containers

docker ps --filter "name=sqlserver" --format "SQL Server: {{.Status}}"
docker ps --filter "name=postgres" --format "PostgreSQL: {{.Status}}"


# Check SQL Server

Write-Host ""
Write-Host "Checking SQL Server connection..."

docker exec sqlserver /opt/mssql-tools18/bin/sqlcmd `
-S localhost `
-U sa `
-P "YourStrong@Pass123" `
-C `
-Q "SELECT 1" `
> $null

Write-Host "SQL Server: OK"


# Check PostgreSQL

Write-Host ""
Write-Host "Checking PostgreSQL connection..."

docker exec postgres bash -c "pg_isready -U postgres > /dev/null 2>&1"

Write-Host "PostgreSQL: OK"


Write-Host ""
Write-Host "Verification completed."
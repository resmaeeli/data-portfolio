Write-Host "Data Portfolio setup started..."


# Project paths
$ProjectRoot = Split-Path -Parent $PSScriptRoot

$BackupPath = Join-Path $ProjectRoot "docker\init\sqlserver\backup"


# Ensure backup folder exists
if (!(Test-Path $BackupPath)) {
    New-Item -ItemType Directory -Path $BackupPath | Out-Null
}

Write-Host "Backup folder ready:"
Write-Host $BackupPath


# AdventureWorks backup settings
$DownloadPath = Join-Path $BackupPath "AdventureWorks2022.bak"

$DownloadUrl = "https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorks2022.bak"


# Check existing backup
Write-Host "Download target:"
Write-Host $DownloadPath

if (Test-Path $DownloadPath) {
    Write-Host "AdventureWorks backup already exists."
}
else {
    Write-Host "Downloading AdventureWorks backup..."

    Invoke-WebRequest `
        -Uri $DownloadUrl `
        -OutFile $DownloadPath

    if (Test-Path $DownloadPath) {

        $FileSizeMB = [math]::Round(
            (Get-Item $DownloadPath).Length / 1MB,
            2
        )

        Write-Host "AdventureWorks backup downloaded successfully."
        Write-Host "Size: $FileSizeMB MB"

    }    
}



Write-Host "Setup step completed."
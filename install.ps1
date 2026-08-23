Write-Host "Data Portfolio installation started..."

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Project root:"
Write-Host $ProjectRoot


# Prepare external files (database backups)
Write-Host "Running setup script..."

& "$ProjectRoot\scripts\setup.ps1"


# Start Docker environment
Write-Host "Starting Docker services..."

Set-Location $ProjectRoot

docker compose up -d



Write-Host "Docker services started."

# Setup Python environment

Write-Host "Setting up Python environment..."

$VenvPath = Join-Path $ProjectRoot ".venv"

if (!(Test-Path $VenvPath)) {
    python -m venv $VenvPath
    Write-Host "Virtual environment created."
}
else {
    Write-Host "Virtual environment already exists."
}


& "$VenvPath\Scripts\python.exe" -m pip install -r "$ProjectRoot\requirements.txt"

Write-Host "Python environment ready."


# Verify installation
Write-Host "Running verification..."

& "$ProjectRoot\scripts\verify.ps1"


Write-Host "Installation completed successfully."
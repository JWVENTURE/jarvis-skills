# JARVIS Reflect Toggle Script

$ReflectModeFile = "$env:USERPROFILE\.claude\.reflect-mode"
$ReflectLog = "$env:USERPROFILE\.claude\.reflect.log"

function Show-ReflectStatus {
    if (Test-Path $ReflectModeFile) {
        $mode = Get-Content $ReflectModeFile
        Write-Host "JARVIS Reflect: AUTO mode enabled" -ForegroundColor Green
    } else {
        Write-Host "JARVIS Reflect: MANUAL mode (use /reflect command)" -ForegroundColor Gray
    }

    if (Test-Path $ReflectLog) {
        Write-Host "`nRecent Activity:"
        Get-Content $ReflectLog -Tail 3
    }
}

# Main
$action = $args[0]

switch ($action) {
    "on" {
        Set-Content -Path $ReflectModeFile -Value "auto"
        $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path $ReflectLog -Value "[$ts] Reflect: AUTO enabled"
        Write-Host "Reflect AUTO enabled - JARVIS will learn from every session" -ForegroundColor Green
    }
    "off" {
        if (Test-Path $ReflectModeFile) {
            Remove-Item $ReflectModeFile -Force
            $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            Add-Content -Path $ReflectLog -Value "[$ts] Reflect: Disabled"
            Write-Host "Reflect disabled" -ForegroundColor Yellow
        } else {
            Write-Host "Reflect is already disabled" -ForegroundColor Gray
        }
    }
    "status" {
        Show-ReflectStatus
    }
    default {
        Show-ReflectStatus
    }
}

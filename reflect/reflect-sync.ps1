# JARVIS Reflect Sync - Learn from session and push to GitHub

$SkillsDir = "$env:USERPROFILE\.claude\skills"
$ReflectModeFile = "$env:USERPROFILE\.claude\.reflect-mode"
$LogFile = "$env:USERPROFILE\.claude\.reflect.log"

# Check if reflect is enabled
if (-not (Test-Path $ReflectModeFile)) {
    Write-Host "Reflect is disabled. Use 'reflect-on' to enable." -ForegroundColor Gray
    exit 0
}

# Check if skills is a git repo
if (-not (Test-Path "$SkillsDir\.git")) {
    Write-Host "Skills not initialized as git repo. Run:" -ForegroundColor Yellow
    Write-Host "  cd ~/.claude/skills && git init" -ForegroundColor Gray
    exit 0
}

# Check for changes
$changes = git -C $SkillsDir status --porcelain 2>$null

if ([string]::IsNullOrEmpty($changes)) {
    Write-Host "No new learnings to sync." -ForegroundColor Gray
    exit 0
}

# Show what changed
Write-Host "`nNew learnings detected:" -ForegroundColor Cyan
git -C $SkillsDir status --short

# Commit changes
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMsg = "learn: $timestamp"

git -C $SkillsDir add .
git -C $SkillsDir commit -m $commitMsg

# Try to push
Write-Host "`nPushing to GitHub..." -ForegroundColor Cyan
$pushResult = git -C $SkillsDir push 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Learnings synced to GitHub" -ForegroundColor Green
} else {
    Write-Host "⚠️ Push failed. Repo may not be connected to GitHub." -ForegroundColor Yellow
    Write-Host "  Run: cd ~/.claude/skills" -ForegroundColor Gray
    Write-Host "  Run: gh repo create jarvis-skills --private --source=." -ForegroundColor Gray
}

# Log it
Add-Content -Path $LogFile -Value "[$timestamp] Sync: $commitMsg"

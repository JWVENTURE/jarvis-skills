---
name: system-admin
description: Windows system maintenance, disk space monitoring, cleanup tasks
---

# System Administration - Windows

## Disk Space Monitoring

### Critical Thresholds
- **< 100 GB free:** WARNING - take action
- **< 50 GB free:** CRITICAL - immediate cleanup needed
- **< 20 GB free:** DANGER - system corruption risk

### Common Space Hogs (User's System)
| Location | Size | Action |
|----------|------|--------|
| `C:\Users\ROG\AppData\Local\warp\Warp\data\logs\mcp` | 346+ GB | Delete when > 500 MB |
| `C:\Users\ROG\AppData\Local\Docker\wsl` | 27+ GB | Periodic cleanup |
| `C:\Users\ROG\.claude\worktrees` | 1.1+ GB | Delete old worktrees |
| Playwright test artifacts | 50-200 MB | Auto-delete after run |

### Quick Disk Check
```powershell
$freeGB = (Get-PSDrive C).Free / 1GB
Write-Host "Free disk space: $([math]::Round($freeGB, 2)) GB"
```

---

## Cleanup Scripts Created

### Warp MCP Log Cleanup
**Location:** `C:\uniplay-development\scripts\daily-warp-cleanup.ps1`
**Usage:** Run manually when remembered
**Threshold:** Deletes when > 500 MB

### Docker WSL2 Cleanup
```powershell
wsl --shutdown
# Then delete Docker data if needed
```

### Git Worktree Cleanup
```powershell
Remove-Item "$env:USERPROFILE\.claude\worktrees\*" -Recurse -Force
```

---

## Tools Installed
- **WizTree** - Fast disk space analyzer
- **Docker Desktop** - WSL2 backend
- **Postman** - API testing

---

## System Information
- **OS:** Windows 11 Home Single Language 10.0.26200
- **Disk:** ~1 TB total
- **Username:** ROG

---

## Pending Review

- [ ] Consider Storage Sense for automatic temp file cleanup
- [ ] Monitor Warp response to bug report

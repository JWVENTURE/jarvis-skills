---
name: warp-terminal
description: Warp terminal bugs, issues, and workarounds
---

# Warp Terminal - Known Issues

## 🐛 CRITICAL BUG: MCP Logging Disk Hog

**Status:** Unconfirmed by Warp, reported 2026-03-31

### Problem
Warp's MCP (Model Context Protocol) logging creates massive log files:
- **Size:** 346.57 GB in 1-2 days
- **Location:** `C:\Users\ROG\AppData\Local\warp\Warp\data\logs\mcp`
- **Impact:** File corruption, system shutdown, data loss

### Root Cause
- No log rotation
- No size limits
- No auto-cleanup
- No user notifications

### User Impact (Actual)
- System file corruption when disk filled
- Forced laptop shutdown
- Lost unsaved work
- Had to uninstall games to recover space

### Solution
Monitor and clean up manually until Warp fixes:

```powershell
# Check Warp log size
$size = (Get-ChildItem "$env:LOCALAPPDATA\warp\Warp\data\logs\mcp" -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB
Write-Host "Warp logs: $size MB"

# Delete if over 500 MB
if ($size -gt 500) {
    Remove-Item "$env:LOCALAPPDATA\warp\Warp\data\logs\mcp\*" -Recurse -Force
    Write-Host "Deleted!"
}
```

### Cleanup Script
Located at: `C:\uniplay-development\scripts\daily-warp-cleanup.ps1`

### Email Report Sent
- **To:** Olivia (Warp team)
- **Date:** March 31, 2026
- **File:** `Warp Product Feedback - Critical Bug Report.md`
- **Contact:** h.jabbar@jwventures.group

---

## Other Notes
- User likes Warp but MCP feature is dangerous on Windows
- Consider using MCP in Cursor/Claude Desktop instead
- Keep Warp MCP disabled until fix is released

---

## Pending Review

- [ ] 2026-03-31: Check if Warp acknowledged bug report

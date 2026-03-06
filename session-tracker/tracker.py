"""
JARVIS Session Tracker
Auto-saves session state for crash recovery
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
SESSION_DIR = Path.home() / ".claude" / ".session-log"
SESSION_FILE = SESSION_DIR / "sessions.json"
LATEST_FILE = SESSION_DIR / "latest-session.json"
CURRENT_FILE = SESSION_DIR / "current-context.json"
ARCHIVE_DIR = SESSION_DIR / "archive"

# Ensure directories exist
SESSION_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_DIR.mkdir(exist_ok=True)


def get_session_id():
    """Generate session ID from date/time"""
    now = datetime.now()
    return f"{now.strftime('%Y-%m-%d')}-session-{now.strftime('%H%M')}"


def load_sessions():
    """Load all sessions"""
    if SESSION_FILE.exists():
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return {"sessions": []}


def save_sessions(sessions):
    """Save all sessions"""
    with open(SESSION_FILE, 'w') as f:
        json.dump(sessions, f, indent=2)


def start_session(project="unknown", branch="unknown"):
    """Start a new session"""
    sessions = load_sessions()

    session_id = get_session_id()
    now = datetime.now().isoformat()

    session = {
        "id": session_id,
        "start_time": now,
        "last_update": now,
        "status": "active",
        "project": project,
        "branch": branch,
        "tasks": [],
        "snapshots": [{"time": now, "action": "Session started"}]
    }

    sessions["sessions"].append(session)
    save_sessions(sessions)

    # Save as latest
    save_latest(session)

    return session_id


def update_session(session_id, updates):
    """Update session with new data"""
    sessions = load_sessions()

    for session in sessions["sessions"]:
        if session["id"] == session_id:
            session["last_update"] = datetime.now().isoformat()

            # Update fields
            for key, value in updates.items():
                if key == "snapshot":
                    session["snapshots"].append({
                        "time": datetime.now().isoformat(),
                        "action": value
                    })
                else:
                    session[key] = value

            save_sessions(sessions)
            save_latest(session)
            return True

    return False


def save_latest(session):
    """Save current session as latest"""
    with open(LATEST_FILE, 'w') as f:
        json.dump(session, f, indent=2)


def load_latest():
    """Load latest session"""
    if LATEST_FILE.exists():
        with open(LATEST_FILE, 'r') as f:
            return json.load(f)
    return None


def end_session(session_id, summary=""):
    """End a session"""
    sessions = load_sessions()

    for session in sessions["sessions"]:
        if session["id"] == session_id:
            session["status"] = "ended"
            session["end_time"] = datetime.now().isoformat()
            session["summary"] = summary

            # Add final snapshot
            session["snapshots"].append({
                "time": session["end_time"],
                "action": "Session ended" + (f": {summary}" if summary else "")
            })

            save_sessions(sessions)
            return True

    return False


def list_sessions(limit=10):
    """List recent sessions"""
    sessions = load_sessions()

    # Sort by start time (newest first)
    sorted_sessions = sorted(
        sessions["sessions"],
        key=lambda x: x["start_time"],
        reverse=True
    )[:limit]

    return sorted_sessions


def get_active_session():
    """Get currently active session (if any)"""
    latest = load_latest()
    if latest and latest.get("status") == "active":
        return latest
    return None


def format_session_list(sessions):
    """Format sessions for display"""
    if not sessions:
        return "No sessions found."

    output = ["Recent Sessions:"]
    output.append("")

    # Header
    output.append(f"{'ID':<20} {'Time':<8} {'Status':<10} {'Project':<15} {'Branch'}")
    output.append("-" * 80)

    for s in sessions:
        start_time = datetime.fromisoformat(s["start_time"]).strftime("%H:%M")
        output.append(
            f"{s['id']:<20} {start_time:<8} {s['status']:<10} {s.get('project', 'unknown'):<15} {s.get('branch', '-')}"
        )

    return "\n".join(output)


def format_session_detail(session):
    """Format session details for display"""
    if not session:
        return "No session details found."

    output = []
    output.append(f"Session: {session['id']}")
    output.append(f"Status: {session['status'].upper()}")
    output.append(f"Project: {session.get('project', 'unknown')}")
    output.append(f"Branch: {session.get('branch', 'unknown')}")
    output.append(f"Started: {session['start_time']}")

    if session.get('tasks'):
        output.append("")
        output.append("Tasks:")
        for i, task in enumerate(session['tasks'], 1):
            status = task.get('status', 'pending')
            desc = task.get('desc', 'No description')
            output.append(f"  {i}. [{status.upper()}] {desc}")

    if session.get('snapshots'):
        output.append("")
        output.append("Recent Actions:")
        for snap in session['snapshots'][-5:]:  # Last 5
            time = datetime.fromisoformat(snap['time']).strftime("%H:%M")
            output.append(f"  {time} - {snap['action']}")

    if session.get('context'):
        output.append("")
        output.append("Context:")
        for key, value in session['context'].items():
            output.append(f"  {key}: {value}")

    return "\n".join(output)


# CLI interface
if __name__ == "__main__":
    import sys

    command = sys.argv[1] if len(sys.argv) > 1 else "list"

    if command == "list":
        sessions = list_sessions()
        print(format_session_list(sessions))

    elif command == "current":
        session = load_latest()
        print(format_session_detail(session))

    elif command == "start":
        project = sys.argv[2] if len(sys.argv) > 2 else "unknown"
        branch = sys.argv[3] if len(sys.argv) > 3 else "unknown"
        session_id = start_session(project, branch)
        print(f"Started session: {session_id}")

    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: tracker.py update <key> <value>")
            sys.exit(1)

        session = get_active_session()
        if not session:
            print("No active session. Start one first.")
            sys.exit(1)

        key = sys.argv[2]
        value = sys.argv[3] if len(sys.argv) > 3 else ""

        update_session(session['id'], {key: value})
        print(f"Updated {key}")

    elif command == "snapshot":
        if len(sys.argv) < 3:
            print("Usage: tracker.py snapshot <action_description>")
            sys.exit(1)

        session = get_active_session()
        if not session:
            print("No active session. Start one first.")
            sys.exit(1)

        action = " ".join(sys.argv[2:])
        update_session(session['id'], {"snapshot": action})
        print(f"Snapshot: {action}")

    elif command == "end":
        session = get_active_session()
        if not session:
            print("No active session.")
            sys.exit(1)

        summary = sys.argv[2] if len(sys.argv) > 2 else ""
        end_session(session['id'], summary)
        print(f"Ended session: {session['id']}")

    elif command == "recover":
        session = load_latest()
        if session:
            print(format_session_detail(session))
        else:
            print("No previous session found.")

    else:
        print("Usage:")
        print("  tracker.py list              - List recent sessions")
        print("  tracker.py current           - Show current session")
        print("  tracker.py start <project>   - Start new session")
        print("  tracker.py update <key> <val>- Update session data")
        print("  tracker.py snapshot <action> - Add action snapshot")
        print("  tracker.py end [summary]     - End current session")
        print("  tracker.py recover           - Show latest for recovery")

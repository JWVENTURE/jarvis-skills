#!/usr/bin/env python3
"""
JARVIS Multi-Agent Supervisor

Manages multi-agent execution without blowing up context:
- Classifies tasks as independent (parallel) or dependent (sequential)
- Writes agent outputs to external storage (not session)
- Returns only summaries to main session
- Manages context budget
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Paths
SUPERVISOR_DIR = Path(__file__).parent
OUTPUT_DIR = SUPERVISOR_DIR / "output"
TASKS_FILE = SUPERVISOR_DIR / "tasks.json"
SUMMARY_FILE = SUPERVISOR_DIR / "summary.json"


def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from tasks.json"""
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to tasks.json"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


def classify_tasks(tasks: List[Dict[str, Any]]) -> Dict[str, List[Dict]]:
    """
    Classify tasks into parallel (independent) and sequential (dependent)

    Parallel: Can run simultaneously (no shared state, different files)
    Sequential: Must run in order (output of one feeds into next)
    """
    parallel = []
    sequential = []

    for task in tasks:
        execution = task.get("execution", "sequential")

        if execution == "parallel":
            # Check for dependencies
            if task.get("depends_on"):
                # Has dependencies, must be sequential
                sequential.append(task)
            else:
                # No dependencies, can run in parallel
                parallel.append(task)
        else:
            sequential.append(task)

    # Sort sequential tasks by dependencies (simple topological sort)
    ordered = []
    seen = set()

    def add_task(task):
        if task["id"] in seen:
            return
        for dep_id in task.get("depends_on", []):
            dep_task = next((t for t in sequential if t["id"] == dep_id), None)
            if dep_task:
                add_task(dep_task)
        ordered.append(task)
        seen.add(task["id"])

    for task in sequential:
        add_task(task)

    return {"parallel": parallel, "sequential": ordered}


def write_agent_output(task_id: str, agent_type: str, prompt: str, findings: str) -> str:
    """Write agent output to external storage (lightweight summary only)"""
    timestamp = datetime.now().isoformat()
    output_file = OUTPUT_DIR / f"{task_id}.json"

    output = {
        "task_id": task_id,
        "agent_type": agent_type,
        "timestamp": timestamp,
        "prompt_brief": prompt[:200] + "..." if len(prompt) > 200 else prompt,
        "findings": findings,
        "status": "completed"
    }

    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    return str(output_file)


def generate_summary(tasks: List[Dict]) -> None:
    """Generate final summary from all agent outputs"""
    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_tasks": len(tasks),
        "completed": 0,
        "findings": []
    }

    for task in tasks:
        output_file = OUTPUT_DIR / f"{task['id']}.json"
        if output_file.exists():
            with open(output_file, 'r') as f:
                agent_output = json.load(f)
                summary["findings"].append({
                    "task_id": task["id"],
                    "name": task.get("name", task["id"]),
                    "findings": agent_output.get("findings", ""),
                    "status": agent_output.get("status", "unknown")
                })
                summary["completed"] += 1

    with open(SUMMARY_FILE, 'w') as f:
        json.dump(summary, f, indent=2)

    return summary


def print_plan(classification: Dict) -> None:
    """Print execution plan for user approval"""
    print("\n" + "="*60)
    print("MULTI-AGENT EXECUTION PLAN")
    print("="*60)

    parallel = classification["parallel"]
    sequential = classification["sequential"]

    if parallel:
        print(f"\n[PARALLEL] ({len(parallel)} tasks - can run simultaneously):")
        for task in parallel:
            print(f"  - [{task['id']}] {task.get('name', task['id'])}")

    if sequential:
        print(f"\n[SEQUENTIAL] ({len(sequential)} tasks - must run in order):")
        for i, task in enumerate(sequential, 1):
            deps = f" (after: {task.get('depends_on', [])})" if task.get('depends_on') else ""
            print(f"  {i}. [{task['id']}] {task.get('name', task['id'])}{deps}")

    print("\n" + "="*60)
    print(f"Total: {len(parallel) + len(sequential)} tasks")
    print(f"Output directory: {OUTPUT_DIR}")
    print("="*60 + "\n")


def create_template_tasks() -> List[Dict]:
    """Create example tasks.json template"""
    return [
        {
            "id": "task-1",
            "name": "Review Profile Screen",
            "execution": "parallel",
            "agent_type": "Explore",
            "prompt": "Analyze profile screen components. Return: file paths, 3 findings, 1 fix priority.",
            "depends_on": []
        },
        {
            "id": "task-2",
            "name": "Review Wallet System",
            "execution": "parallel",
            "agent_type": "Explore",
            "prompt": "Analyze wallet/credits display. Return: file paths, 3 findings, 1 fix priority.",
            "depends_on": []
        },
        {
            "id": "task-3",
            "name": "Implement Fixes",
            "execution": "sequential",
            "agent_type": "general-purpose",
            "prompt": "Using findings from task-1 and task-2, implement the priority fixes.",
            "depends_on": ["task-1", "task-2"]
        }
    ]


# CLI Commands
def cmd_plan(args):
    """Show execution plan without running"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Run 'supervisor.py init' to create template.")
        return

    classification = classify_tasks(tasks)
    print_plan(classification)


def cmd_init(args):
    """Create template tasks.json"""
    if TASKS_FILE.exists():
        print("tasks.json already exists. Delete it first to reinitialize.")
        return

    template = create_template_tasks()
    save_tasks(template)
    print(f"Created template tasks.json at {TASKS_FILE}")
    print("Edit it with your tasks, then run 'supervisor.py plan' to see the execution plan.")


def cmd_status(args):
    """Show current status"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks defined.")
        return

    summary_file = SUMMARY_FILE
    if summary_file.exists():
        with open(summary_file, 'r') as f:
            summary = json.load(f)
        print(f"\nStatus: {summary['completed']}/{summary['total_tasks']} tasks completed")
    else:
        print(f"\nStatus: {len(tasks)} tasks defined, 0 completed")

    print(f"\nAgent outputs in: {OUTPUT_DIR}")
    output_files = list(OUTPUT_DIR.glob("*.json"))
    for f in output_files:
        with open(f, 'r') as file:
            data = json.load(file)
        print(f"  ✓ {data['task_id']}: {data.get('status', 'unknown')}")


def cmd_summary(args):
    """Print current summary"""
    summary_file = SUMMARY_FILE
    if not summary_file.exists():
        print("No summary available. Run agents first.")
        return

    with open(summary_file, 'r') as f:
        summary = json.load(f)

    print("\n" + "="*60)
    print("EXECUTION SUMMARY")
    print("="*60)
    print(f"Completed: {summary['completed']}/{summary['total_tasks']} tasks\n")

    for finding in summary['findings']:
        print(f"\n[{finding['task_id']}] {finding['name']}")
        print(f"Status: {finding['status']}")
        print(f"Findings:\n{finding['findings']}")

    print("\n" + "="*60)


def cmd_reset(args):
    """Reset all outputs"""
    import shutil
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
        OUTPUT_DIR.mkdir()

    if SUMMARY_FILE.exists():
        SUMMARY_FILE.unlink()

    print("Reset: All agent outputs cleared")


def main():
    if len(sys.argv) < 2:
        print("JARVIS Multi-Agent Supervisor")
        print("\nCommands:")
        print("  init     - Create template tasks.json")
        print("  plan     - Show execution plan")
        print("  status   - Show current status")
        print("  summary  - Show execution summary")
        print("  reset    - Reset all outputs")
        print("\nFor Claude Code:")
        print("  1. Create/edit tasks.json")
        print("  2. Use 'plan' to review")
        print("  3. Run agents using Claude Code Agent tool")
        print("  4. Each agent writes output to output/")
        print("  5. Use 'summary' to see aggregated results")
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "init": cmd_init,
        "plan": cmd_plan,
        "status": cmd_status,
        "summary": cmd_summary,
        "reset": cmd_reset,
    }

    if cmd in commands:
        commands[cmd](args)
    else:
        print(f"Unknown command: {cmd}")
        main()


if __name__ == "__main__":
    main()

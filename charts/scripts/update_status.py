#!/usr/bin/env python3
"""
Update chart status files and generate status reports.

Usage:
    python3 update_status.py --show              # Show current status
    python3 update_status.py --chart <path> --status <status>  # Update chart status
"""

import argparse
import yaml
from pathlib import Path
from datetime import datetime

def load_status_file(status_path):
    """Load a status file."""
    if not status_path.exists():
        return {}
    
    with open(status_path, 'r') as f:
        return yaml.safe_load(f) or {}

def save_status_file(status_path, data):
    """Save a status file."""
    status_path.parent.mkdir(parents=True, exist_ok=True)
    with open(status_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def show_status():
    """Show current status of all charts."""
    print("=" * 70)
    print("Chart Status Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()
    
    chart_dirs = [
        "charts/sankey",
        "charts/bar_charts",
        "charts/time_series",
        "charts/network"
    ]
    
    for chart_dir in chart_dirs:
        status_file = Path(chart_dir) / ".status"
        
        if not status_file.exists():
            print(f"⚠️  {chart_dir}: No status file")
            continue
        
        status = load_status_file(status_file)
        
        chart_type = status.get("chart_type", "Unknown")
        status_val = status.get("status", "unknown")
        
        # Status symbol
        if status_val == "production":
            symbol = "🟢"
        elif status_val == "review":
            symbol = "🟡"
        elif status_val == "development":
            symbol = "🔵"
        else:
            symbol = "⚪"
        
        print(f"{symbol} {chart_type.upper()}: {status_val}")
        
        # List charts
        for chart in status.get("charts", []):
            chart_status = chart.get("status", "unknown")
            chart_name = chart.get("name", "Unknown")
            print(f"   - {chart_name} ({chart_status})")
        
        print()

def update_chart_status(chart_path, new_status):
    """Update status for a specific chart."""
    status_file = Path(chart_path).parent / ".status"
    
    if not status_file.exists():
        print(f"❌ Status file not found: {status_file}")
        return False
    
    status = load_status_file(status_file)
    
    # Find and update chart
    found = False
    for chart in status.get("charts", []):
        if chart.get("file") == Path(chart_path).name:
            chart["status"] = new_status
            chart["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            found = True
            break
    
    if not found:
        print(f"❌ Chart not found in status file: {chart_path}")
        return False
    
    # Update overall status
    statuses = [c.get("status") for c in status.get("charts", [])]
    if all(s == "production" for s in statuses):
        status["status"] = "production"
    elif any(s == "production" for s in statuses):
        status["status"] = "review"
    else:
        status["status"] = "development"
    
    status["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    save_status_file(status_file, status)
    print(f"✅ Updated {chart_path} to {new_status}")
    return True

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Update chart status")
    parser.add_argument("--show", action="store_true", help="Show current status")
    parser.add_argument("--chart", help="Chart file path")
    parser.add_argument("--status", help="New status (production, review, development, planned)")
    
    args = parser.parse_args()
    
    if args.show:
        show_status()
    elif args.chart and args.status:
        update_chart_status(args.chart, args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
Generate all political visualization charts.

This script runs all chart generation scripts and reports status.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Chart generation scripts
CHART_SCRIPTS = [
    ("Sankey - Unified Flow", "analysis/unified_flow_sankey.py"),
    ("Sankey - Outflows Detailed", "analysis/outflows_sankey_detailed.py"),
    # Add more scripts as they're implemented
    # ("Bar - Top Committees", "charts/scripts/generate_bar_top_committees.py"),
    # ("Bar - Party Comparison", "charts/scripts/generate_bar_party_comparison.py"),
    # ("Time Series - Monthly Trends", "charts/scripts/generate_timeseries_monthly.py"),
]

def run_script(script_path):
    """Run a chart generation script and return success status."""
    try:
        result = subprocess.run(
            ["python3", str(script_path)],
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Script timed out after 300 seconds"
    except Exception as e:
        return False, "", str(e)

def main():
    """Generate all charts and report status."""
    print("=" * 70)
    print("Political Visualization Charts - Generation Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()
    
    results = []
    
    for chart_name, script_path in CHART_SCRIPTS:
        script_file = Path(script_path)
        
        if not script_file.exists():
            print(f"⚠️  SKIPPED: {chart_name}")
            print(f"   Script not found: {script_path}")
            results.append((chart_name, "SKIPPED", "Script not found"))
            print()
            continue
        
        print(f"🔄 GENERATING: {chart_name}")
        print(f"   Script: {script_path}")
        
        success, stdout, stderr = run_script(script_file)
        
        if success:
            print(f"✅ SUCCESS: {chart_name}")
            if stdout:
                for line in stdout.strip().split('\n')[-3:]:
                    print(f"   {line}")
            results.append((chart_name, "SUCCESS", ""))
        else:
            print(f"❌ FAILED: {chart_name}")
            if stderr:
                for line in stderr.strip().split('\n')[-3:]:
                    print(f"   {line}")
            results.append((chart_name, "FAILED", stderr))
        
        print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    success_count = sum(1 for _, status, _ in results if status == "SUCCESS")
    failed_count = sum(1 for _, status, _ in results if status == "FAILED")
    skipped_count = sum(1 for _, status, _ in results if status == "SKIPPED")
    
    for chart_name, status, _ in results:
        if status == "SUCCESS":
            symbol = "✅"
        elif status == "FAILED":
            symbol = "❌"
        else:
            symbol = "⚠️ "
        print(f"{symbol} {chart_name}: {status}")
    
    print()
    print(f"Total: {len(results)} | Success: {success_count} | Failed: {failed_count} | Skipped: {skipped_count}")
    print()
    
    # Exit code
    if failed_count > 0:
        print("❌ Some charts failed to generate")
        return 1
    else:
        print("✅ All charts generated successfully")
        return 0

if __name__ == "__main__":
    sys.exit(main())


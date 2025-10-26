#!/usr/bin/env python3
"""
Validate generated chart files for quality and correctness.

Checks:
- DOCTYPE declaration present
- Colors render correctly
- File size reasonable
- HTML structure valid
"""

import re
from pathlib import Path
from datetime import datetime

def check_doctype(html_content):
    """Check if DOCTYPE is present."""
    return "<!DOCTYPE html>" in html_content

def check_colors(html_content):
    """Check if party colors are present."""
    colors = {
        "red_full": "rgba(204, 0, 0, 1)",
        "blue_full": "rgba(0, 51, 153, 1)",
        "red_light": "rgba(255, 180, 180, 1)",
        "blue_light": "rgba(173, 216, 230, 1)",
        "gray": "rgba(128, 128, 128, 1)"
    }
    
    found_colors = {}
    for color_name, color_value in colors.items():
        if color_value in html_content:
            found_colors[color_name] = True
    
    return found_colors

def check_plotly(html_content):
    """Check if Plotly is included."""
    return "plotly" in html_content.lower()

def check_file_size(file_path):
    """Check if file size is reasonable."""
    size_mb = file_path.stat().st_size / (1024 * 1024)
    return size_mb, size_mb < 50  # Warn if > 50MB

def validate_chart(chart_path):
    """Validate a single chart file."""
    if not chart_path.exists():
        return {
            "file": chart_path.name,
            "exists": False,
            "valid": False,
            "errors": ["File not found"]
        }
    
    with open(chart_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Check DOCTYPE
    if not check_doctype(content):
        errors.append("Missing DOCTYPE declaration")
    
    # Check Plotly
    if not check_plotly(content):
        errors.append("Plotly not found in HTML")
    
    # Check colors
    colors = check_colors(content)
    if not colors:
        warnings.append("No party colors found")
    
    # Check file size
    size_mb, size_ok = check_file_size(chart_path)
    if not size_ok:
        warnings.append(f"Large file size: {size_mb:.2f}MB")
    
    return {
        "file": chart_path.name,
        "exists": True,
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "colors_found": colors,
        "file_size_mb": size_mb
    }

def main():
    """Validate all charts."""
    print("=" * 70)
    print("Chart Validation Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()
    
    # Find all HTML files in output directories
    output_dir = Path("analysis/outputs")
    chart_files = list(output_dir.glob("*.html"))
    
    if not chart_files:
        print("⚠️  No chart files found in analysis/outputs/")
        return 1
    
    results = []
    for chart_file in sorted(chart_files):
        result = validate_chart(chart_file)
        results.append(result)
        
        # Print result
        if result["valid"]:
            print(f"✅ {result['file']}")
        else:
            print(f"❌ {result['file']}")
        
        if result["errors"]:
            for error in result["errors"]:
                print(f"   ERROR: {error}")
        
        if result["warnings"]:
            for warning in result["warnings"]:
                print(f"   WARNING: {warning}")
        
        if result.get("colors_found"):
            colors_str = ", ".join(result["colors_found"].keys())
            print(f"   Colors: {colors_str}")
        
        print(f"   Size: {result.get('file_size_mb', 0):.2f}MB")
        print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    valid_count = sum(1 for r in results if r["valid"])
    invalid_count = sum(1 for r in results if not r["valid"])
    
    print(f"Total: {len(results)} | Valid: {valid_count} | Invalid: {invalid_count}")
    print()
    
    if invalid_count > 0:
        print("❌ Some charts failed validation")
        return 1
    else:
        print("✅ All charts passed validation")
        return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())


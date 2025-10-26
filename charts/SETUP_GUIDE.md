# Setup and Getting Started Guide

Complete guide to setting up and using the political-charts repository.

## 🚀 Quick Start (5 minutes)

### 1. Verify Installation
```bash
cd /Users/ak/Political-Media-Spending-
python3 --version  # Should be 3.8+
pip3 list | grep plotly  # Should show plotly 6.1.2+
```

### 2. Generate Charts
```bash
python3 charts/scripts/generate_all_charts.py
```

### 3. Validate Charts
```bash
python3 charts/scripts/validate_charts.py
```

### 4. View Status
```bash
python3 charts/scripts/update_status.py --show
```

## 📋 Prerequisites

### System Requirements
- Python 3.8 or higher
- 2GB+ RAM
- Modern web browser (Chrome, Firefox, Safari, Edge)
- ~500MB disk space for charts and data

### Python Packages
```bash
pip3 install plotly>=6.1.2
pip3 install pandas>=1.3.0
pip3 install numpy>=1.21.0
pip3 install pyyaml>=5.4.0
```

### Install All Dependencies
```bash
pip3 install -r requirements.txt
```

## 📁 Directory Setup

The repository structure is already created:

```
charts/
├── README.md                    # Main documentation
├── CONFIG.yaml                  # Global configuration
├── CHART_STATUS.md             # Status tracker
├── NAMING_CONVENTIONS.md       # Naming standards
├── INDEX.md                    # Quick reference
├── DIRECTORY_STRUCTURE.md      # This structure
├── SETUP_GUIDE.md              # This file
│
├── sankey/                     # Production charts
├── bar_charts/                 # Planned charts
├── time_series/                # Planned charts
├── network/                    # Planned charts
├── templates/                  # Chart templates
├── scripts/                    # Utility scripts
└── data/                       # Data files
```

## 🔧 Configuration

### Global Settings
Edit `charts/CONFIG.yaml` to customize:

```yaml
# Output directory
charts:
  output_dir: "analysis/outputs"

# Color scheme
colors:
  republican:
    full: "#CC0000"
    light: "#FFB4B4"
  democratic:
    full: "#003399"
    light: "#ADD8E6"

# Plotly settings
plotly:
  version: "6.1.2"
  layout:
    height: 1200
    width: 1600
```

### Chart-Specific Settings
Each chart type has its own README.md with customization options.

## 📊 Data Files

### Required Data
The system expects these files in `analysis/outputs/`:

1. **fec_committees_combined.parquet**
   - FEC committee data
   - Contains: CMTE_ID, CMTE_NM, party_affiliation, type_family, designation_name, TTL_RECEIPTS

2. **outflows_schedule_b_recipients_2024.csv**
   - FEC Schedule B outflows
   - Contains: committee_id, committee_name, recipient_id, committee_name_recipient, total

### Data Format
- Parquet files: Binary columnar format (efficient)
- CSV files: Text format (human-readable)
- All data filtered for 2024 cycle

## 🎨 Color Scheme

All charts use consistent party affiliation colors:

| Party | Full Color | Light Color | Use Case |
|-------|-----------|-------------|----------|
| Republican | #CC0000 | #FFB4B4 | Main committees (full), Categories (light) |
| Democratic | #003399 | #ADD8E6 | Main committees (full), Categories (light) |
| Unknown | #808080 | #D3D3D3 | Non-partisan or unknown affiliation |

## 🚀 Common Tasks

### Generate All Charts
```bash
python3 charts/scripts/generate_all_charts.py
```

Output: All charts regenerated in `analysis/outputs/`

### Generate Specific Chart
```bash
python3 analysis/unified_flow_sankey.py
```

Output: `analysis/outputs/sankey_unified_flow_2024.html`

### Validate Charts
```bash
python3 charts/scripts/validate_charts.py
```

Checks:
- DOCTYPE declaration
- Color rendering
- File size
- HTML structure

### View Chart Status
```bash
python3 charts/scripts/update_status.py --show
```

Shows status of all charts by type.

### Update Chart Status
```bash
python3 charts/scripts/update_status.py \
  --chart sankey/sankey_unified_flow_2024.html \
  --status production
```

Updates status and last_updated timestamp.

## 📝 Creating a New Chart

### Step 1: Plan
- Decide chart type (sankey, bar, timeseries, network)
- Define data requirements
- Sketch visualization

### Step 2: Create Directory
```bash
mkdir -p charts/{chart_type}
```

### Step 3: Add Documentation
Copy template and customize:
```bash
cp charts/bar_charts/README.md charts/{chart_type}/README.md
```

### Step 4: Create Status File
```bash
cp charts/bar_charts/.status charts/{chart_type}/.status
```

Edit `.status` file with chart details.

### Step 5: Implement Script
```bash
cp charts/templates/chart_template.py \
   charts/scripts/generate_{chart_type}.py
```

Edit script to implement your chart.

### Step 6: Test
```bash
python3 charts/scripts/generate_{chart_type}.py
python3 charts/scripts/validate_charts.py
```

### Step 7: Update Status
```bash
python3 charts/scripts/update_status.py \
  --chart {chart_type}/{chart_name}.html \
  --status production
```

### Step 8: Update Documentation
- Update `CHART_STATUS.md`
- Update `README.md` in chart type directory
- Update `INDEX.md` if needed

## 🐛 Troubleshooting

### Charts Not Generating
**Problem:** Script fails with error
**Solution:**
1. Check data files exist: `ls analysis/outputs/*.parquet`
2. Verify Python packages: `pip3 list | grep plotly`
3. Check file permissions: `ls -la charts/scripts/`
4. Run with verbose output: `python3 -u script.py`

### Colors Not Displaying
**Problem:** Charts show gray instead of colors
**Solution:**
1. Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
2. Clear browser cache
3. Check DOCTYPE in HTML: `head -1 output.html`
4. Validate colors: `python3 charts/scripts/validate_charts.py`

### File Size Too Large
**Problem:** HTML file > 50MB
**Solution:**
1. Reduce data: Limit top N items
2. Compress data: Use aggregation
3. Check for duplicate data in HTML
4. Consider splitting into multiple charts

### Status File Not Updating
**Problem:** `.status` file not changing
**Solution:**
1. Check file permissions: `ls -la charts/{type}/.status`
2. Verify YAML syntax: `python3 -c "import yaml; yaml.safe_load(open('file'))"`
3. Run update script with full path
4. Check for write permissions

## 📚 Documentation Reference

| Document | Purpose |
|----------|---------|
| `README.md` | Main overview and getting started |
| `CHART_STATUS.md` | Development status of all charts |
| `NAMING_CONVENTIONS.md` | File naming standards |
| `CONFIG.yaml` | Global configuration |
| `INDEX.md` | Quick reference guide |
| `DIRECTORY_STRUCTURE.md` | Directory organization |
| `SETUP_GUIDE.md` | This file - setup instructions |

## 🔗 Related Resources

### FEC Data
- [FEC Data Documentation](https://www.fec.gov/data/)
- [Committee Data](https://www.fec.gov/data/committees/)
- [Schedule B Data](https://www.fec.gov/data/disbursements/)

### Plotly
- [Plotly Python Documentation](https://plotly.com/python/)
- [Sankey Diagrams](https://plotly.com/python/sankey-diagram/)
- [Bar Charts](https://plotly.com/python/bar-charts/)

### Python
- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [NumPy Documentation](https://numpy.org/)

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Python 3.8+ installed
- [ ] All packages installed: `pip3 list`
- [ ] Data files exist: `ls analysis/outputs/*.parquet`
- [ ] Charts directory created: `ls -la charts/`
- [ ] Scripts executable: `ls -la charts/scripts/`
- [ ] Generate charts: `python3 charts/scripts/generate_all_charts.py`
- [ ] Validate charts: `python3 charts/scripts/validate_charts.py`
- [ ] View status: `python3 charts/scripts/update_status.py --show`
- [ ] Open chart in browser: `open analysis/outputs/sankey_unified_flow_2024.html`

## 🎯 Next Steps

1. **Review Documentation**
   - Read `README.md` for overview
   - Check `CHART_STATUS.md` for current progress
   - Review `NAMING_CONVENTIONS.md` for standards

2. **Generate Charts**
   - Run `python3 charts/scripts/generate_all_charts.py`
   - Validate with `python3 charts/scripts/validate_charts.py`

3. **Explore Charts**
   - Open HTML files in browser
   - Interact with visualizations
   - Test zoom, pan, hover features

4. **Plan New Charts**
   - Review `CHART_STATUS.md` for planned charts
   - Check `bar_charts/README.md` for next priorities
   - Follow setup guide to implement

5. **Maintain Repository**
   - Keep documentation updated
   - Update status files regularly
   - Monitor data file freshness

---

**Last Updated:** 2024-10-26  
**Version:** 1.0.0


# Political Charts Repository Index

Quick reference guide for the political visualization charts repository structure and management.

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Main repository documentation and overview |
| `CHART_STATUS.md` | Development status tracker for all charts |
| `NAMING_CONVENTIONS.md` | File naming standards and conventions |
| `CONFIG.yaml` | Global configuration for all charts |
| `INDEX.md` | This file - quick reference guide |

## 📁 Directory Structure

```
charts/
├── README.md                    # Main documentation
├── CHART_STATUS.md             # Status tracker
├── NAMING_CONVENTIONS.md       # Naming standards
├── CONFIG.yaml                 # Global config
├── INDEX.md                    # This file
│
├── sankey/                     # Sankey diagrams (PRODUCTION)
│   ├── README.md
│   ├── .status
│   ├── sankey_unified_flow_2024.html
│   └── sankey_outflows_detailed_2024.html
│
├── bar_charts/                 # Bar charts (PLANNED)
│   ├── README.md
│   └── .status
│
├── time_series/                # Time series (PLANNED)
│   ├── README.md
│   └── .status
│
├── network/                    # Network diagrams (PLANNED)
│   ├── README.md
│   └── .status
│
├── templates/                  # Chart generation templates
│   ├── chart_template.py       # Generic chart template
│   └── sankey_template.py      # Sankey-specific template
│
├── scripts/                    # Utility scripts
│   ├── generate_all_charts.py  # Generate all charts
│   ├── validate_charts.py      # Validate chart files
│   └── update_status.py        # Update status files
│
└── data/                       # Data files (symlinked from analysis/outputs)
    ├── fec_committees_combined.parquet
    └── outflows_schedule_b_recipients_2024.csv
```

## 🚀 Quick Start Commands

### Generate All Charts
```bash
python3 charts/scripts/generate_all_charts.py
```

### Validate Charts
```bash
python3 charts/scripts/validate_charts.py
```

### View Chart Status
```bash
python3 charts/scripts/update_status.py --show
```

### Update Chart Status
```bash
python3 charts/scripts/update_status.py --chart sankey/sankey_unified_flow_2024.html --status production
```

## 📊 Chart Status Overview

| Chart Type | Status | Count | Location |
|-----------|--------|-------|----------|
| Sankey | 🟢 Production | 2 | `sankey/` |
| Bar Charts | ⚪ Planned | 3 | `bar_charts/` |
| Time Series | ⚪ Planned | 3 | `time_series/` |
| Network | ⚪ Planned | 2 | `network/` |

## 🎨 Color Scheme Reference

All charts use consistent party affiliation colors:

```
Republican:  #CC0000 (full) / #FFB4B4 (light)
Democratic:  #003399 (full) / #ADD8E6 (light)
Unknown:     #808080 (full) / #D3D3D3 (light)
```

## 📝 File Naming Patterns

### Chart Output Files
```
{chart_type}_{description}_{year}.html
```
Example: `sankey_unified_flow_2024.html`

### Data Files
```
{data_source}_{description}_{year}.{ext}
```
Example: `fec_committees_combined.parquet`

### Scripts
```
{action}_{chart_type}.py
```
Example: `generate_sankey.py`

## 🔄 Development Workflow

### Adding a New Chart

1. **Create Directory**
   ```bash
   mkdir -p charts/{chart_type}
   ```

2. **Add Documentation**
   - Copy `README.md` template
   - Document chart purpose and features

3. **Create Status File**
   - Copy `.status` template
   - Set initial status to "planned"

4. **Implement Generation Script**
   - Use `charts/templates/chart_template.py` as base
   - Follow naming conventions
   - Place in `charts/scripts/`

5. **Update CHART_STATUS.md**
   - Add chart entry
   - Set priority and estimated completion

6. **Generate and Validate**
   ```bash
   python3 charts/scripts/generate_all_charts.py
   python3 charts/scripts/validate_charts.py
   ```

7. **Update Status**
   ```bash
   python3 charts/scripts/update_status.py --chart {path} --status production
   ```

## 📋 Status Levels

| Status | Symbol | Meaning |
|--------|--------|---------|
| Production-Ready | 🟢 | Tested, documented, ready for use |
| Ready for Review | 🟡 | Complete but needs validation |
| In Development | 🔵 | Active work in progress |
| Planned | ⚪ | Scheduled for future development |

## 🔗 Related Files

### Generation Scripts
- `analysis/unified_flow_sankey.py` - Generates unified flow Sankey
- `analysis/outflows_sankey_detailed.py` - Generates outflows Sankey

### Data Files
- `analysis/outputs/fec_committees_combined.parquet` - Committee data
- `analysis/outputs/outflows_schedule_b_recipients_2024.csv` - Outflows data

### Configuration
- `charts/CONFIG.yaml` - Global configuration
- `charts/NAMING_CONVENTIONS.md` - Naming standards

## 📞 Support

For questions or issues:
1. Check relevant README.md in chart type directory
2. Review CHART_STATUS.md for known issues
3. Check NAMING_CONVENTIONS.md for naming questions
4. Review CONFIG.yaml for configuration options

## 🔍 Key Concepts

### Sankey Diagrams
Flow diagrams showing money movement between entities. Currently have 2 production-ready charts.

### Party Affiliation
All charts use consistent color coding:
- Red for Republican
- Blue for Democratic
- Gray for Unknown/Non-partisan

### Data Pipeline
1. Load FEC data (parquet/CSV)
2. Process and aggregate
3. Map party affiliation
4. Generate visualization
5. Output HTML with embedded Plotly

### Quality Assurance
- DOCTYPE declaration required
- Colors validated
- File sizes checked
- HTML structure verified

## 📈 Development Roadmap

### Q4 2024
- ✅ Sankey diagrams (COMPLETE)
- 🔵 Bar charts (IN PROGRESS)

### Q1 2025
- ⚪ Time series charts
- ⚪ Network diagrams

### Q2 2025
- ⚪ Dashboard integration
- ⚪ Advanced filtering

---

**Last Updated:** 2024-10-26  
**Repository:** political-charts  
**Maintainer:** Political Charts Team


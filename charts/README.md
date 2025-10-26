# Political Visualization Charts

A comprehensive collection of interactive political visualization charts showing money flows, campaign spending, and political contributions using FEC (Federal Election Commission) data.

## 📊 Chart Types

### 1. **Sankey Diagrams** (`sankey/`)
Flow diagrams showing the movement of money between political entities.

**Current Charts:**
- `unified_flow_2024.html` - Complete money flow: Type → Designation → Committee → Recipient
- `outflows_detailed_2024.html` - Detailed outflows: Committee Type → Committee → Recipient

**Purpose:** Visualize the complete journey of political money from source through intermediaries to final recipients.

**Color Coding:**
- 🔴 **Red** - Republican-affiliated entities
- 🔵 **Blue** - Democratic-affiliated entities
- ⚫ **Gray** - Unknown/Non-partisan entities
- Light shades indicate category nodes (Type, Designation, Recipient)

**Dependencies:**
- Plotly 6.1.2+
- Python 3.8+
- pandas
- FEC data files (parquet format)

**Generation:**
```bash
python3 analysis/unified_flow_sankey.py
python3 analysis/outflows_sankey_detailed.py
```

**Output Location:** `analysis/outputs/sankey_*.html`

---

### 2. **Bar Charts** (`bar_charts/`)
Comparative visualizations of spending by category, party, or time period.

**Status:** In Development

**Planned Charts:**
- Top committees by spending
- Party spending comparison
- Committee type breakdown

---

### 3. **Time Series** (`time_series/`)
Temporal analysis of political spending trends.

**Status:** In Development

**Planned Charts:**
- Monthly spending trends
- Cumulative spending over time
- Seasonal patterns

---

### 4. **Network Diagrams** (`network/`)
Graph-based visualizations showing relationships between political entities.

**Status:** Planned

---

## 📁 Directory Structure

```
charts/
├── README.md                          # This file
├── CHART_STATUS.md                    # Chart development status tracker
├── NAMING_CONVENTIONS.md              # File naming standards
├── CONFIG.yaml                        # Global configuration
├── sankey/
│   ├── README.md                      # Sankey-specific documentation
│   ├── unified_flow_2024.html         # Production-ready
│   ├── outflows_detailed_2024.html    # Production-ready
│   └── .status                        # Status file
├── bar_charts/
│   ├── README.md
│   └── .status
├── time_series/
│   ├── README.md
│   └── .status
├── network/
│   ├── README.md
│   └── .status
├── templates/                         # Chart generation templates
│   ├── sankey_template.py
│   └── chart_template.py
├── data/                              # Data files and mappings
│   ├── fec_committees_combined.parquet
│   └── outflows_schedule_b_recipients_2024.csv
└── scripts/                           # Utility scripts
    ├── generate_all_charts.py
    ├── validate_charts.py
    └── update_status.py
```

## 🎨 Color Scheme

All charts use consistent party affiliation colors:

| Party | Full Color | Light Color | Hex (Full) | Hex (Light) |
|-------|-----------|-------------|-----------|------------|
| Republican | 🔴 Red | Light Red | #CC0000 | #FFB4B4 |
| Democratic | 🔵 Blue | Light Blue | #003399 | #ADD8E6 |
| Unknown | ⚫ Gray | Light Gray | #808080 | #D3D3D3 |

## 📋 Chart Status Levels

- **🟢 Production-Ready** - Tested, documented, ready for deployment
- **🟡 Ready for Review** - Complete but needs validation
- **🔵 In Development** - Active work in progress
- **⚪ Planned** - Scheduled for development

## 🔧 Dependencies

### Python Packages
```
plotly>=6.1.2
pandas>=1.3.0
numpy>=1.21.0
pyyaml>=5.4.0
```

### Data Sources
- FEC Committee data (parquet format)
- FEC Schedule B data (CSV format)
- Party affiliation mappings

### System Requirements
- Python 3.8+
- 2GB+ RAM for large datasets
- Modern web browser for viewing HTML charts

## 📝 Naming Conventions

See `NAMING_CONVENTIONS.md` for detailed naming standards.

**Quick Reference:**
- Chart files: `{chart_type}_{description}_{year}.html`
- Data files: `{data_source}_{description}_{year}.{ext}`
- Scripts: `{action}_{chart_type}.py`

## 🚀 Quick Start

### Generate All Charts
```bash
python3 scripts/generate_all_charts.py
```

### Generate Specific Chart Type
```bash
python3 analysis/unified_flow_sankey.py
```

### View Chart Status
```bash
python3 scripts/update_status.py --show
```

## 📊 Data Pipeline

1. **Data Ingestion** - FEC data loaded from parquet/CSV
2. **Processing** - Data aggregation and party mapping
3. **Visualization** - Plotly chart generation
4. **Output** - HTML files with embedded data and styling
5. **Validation** - Chart verification and status update

## 🔍 Quality Assurance

- All charts include DOCTYPE declaration for Standards Mode rendering
- Colors verified to render correctly in modern browsers
- Node heights calculated based on flow values
- Party affiliation inferred from connected entities when needed

## 📚 Additional Resources

- [Plotly Documentation](https://plotly.com/python/)
- [FEC Data Documentation](https://www.fec.gov/data/)
- [Chart Status Tracker](CHART_STATUS.md)
- [Naming Conventions](NAMING_CONVENTIONS.md)

## 🤝 Contributing

When adding new charts:
1. Create appropriate subdirectory in `charts/`
2. Add README.md with chart documentation
3. Follow naming conventions
4. Update CHART_STATUS.md
5. Add generation script to `scripts/`
6. Test chart rendering in multiple browsers

## 📄 License

[Add your license information here]

---

**Last Updated:** 2024-10-26
**Maintainer:** [Your Name]


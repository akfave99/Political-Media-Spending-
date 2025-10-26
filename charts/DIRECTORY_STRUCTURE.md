# Directory Structure

Complete visual guide to the political-charts repository organization.

## 📁 Full Directory Tree

```
charts/
│
├── 📄 README.md                          # Main repository documentation
├── 📄 CHART_STATUS.md                    # Chart development status tracker
├── 📄 NAMING_CONVENTIONS.md              # File naming standards
├── 📄 CONFIG.yaml                        # Global configuration
├── 📄 INDEX.md                           # Quick reference guide
├── 📄 DIRECTORY_STRUCTURE.md             # This file
│
├── 📁 sankey/                            # Sankey diagrams (🟢 PRODUCTION)
│   ├── 📄 README.md                      # Sankey documentation
│   ├── 📄 .status                        # Status file (YAML)
│   ├── 📊 sankey_unified_flow_2024.html  # Unified flow visualization
│   └── 📊 sankey_outflows_detailed_2024.html  # Outflows visualization
│
├── 📁 bar_charts/                        # Bar charts (⚪ PLANNED)
│   ├── 📄 README.md                      # Bar chart documentation
│   └── 📄 .status                        # Status file (YAML)
│
├── 📁 time_series/                       # Time series (⚪ PLANNED)
│   ├── 📄 README.md                      # Time series documentation
│   └── 📄 .status                        # Status file (YAML)
│
├── 📁 network/                           # Network diagrams (⚪ PLANNED)
│   ├── 📄 README.md                      # Network documentation
│   └── 📄 .status                        # Status file (YAML)
│
├── 📁 templates/                         # Chart generation templates
│   ├── 📄 chart_template.py              # Generic chart template
│   └── 📄 sankey_template.py             # Sankey-specific template
│
├── 📁 scripts/                           # Utility and management scripts
│   ├── 📄 generate_all_charts.py         # Generate all charts
│   ├── 📄 validate_charts.py             # Validate chart files
│   └── 📄 update_status.py               # Update status files
│
└── 📁 data/                              # Data files (symlinked)
    ├── 📊 fec_committees_combined.parquet
    └── 📊 outflows_schedule_b_recipients_2024.csv
```

## 📊 File Types Legend

| Symbol | Type | Description |
|--------|------|-------------|
| 📄 | Markdown | Documentation files |
| 📋 | YAML | Configuration and status files |
| 🐍 | Python | Python scripts |
| 📊 | HTML/Data | Generated charts or data files |

## 📂 Directory Descriptions

### Root Level (`charts/`)
Main documentation and configuration files for the entire repository.

**Key Files:**
- `README.md` - Start here for overview
- `CONFIG.yaml` - Global settings for all charts
- `CHART_STATUS.md` - Track development progress
- `INDEX.md` - Quick reference guide

### Chart Type Directories

#### `sankey/` - Sankey Diagrams
**Status:** 🟢 Production-Ready

Contains flow diagrams showing political money movement.

**Files:**
- `README.md` - Sankey-specific documentation
- `.status` - Development status (YAML)
- `sankey_unified_flow_2024.html` - 4-level flow visualization
- `sankey_outflows_detailed_2024.html` - 3-level outflows visualization

#### `bar_charts/` - Bar Charts
**Status:** ⚪ Planned

For comparative spending analysis.

**Planned Charts:**
- Top committees by spending
- Party spending comparison
- Committee type breakdown

#### `time_series/` - Time Series
**Status:** ⚪ Planned

For temporal trend analysis.

**Planned Charts:**
- Monthly spending trends
- Cumulative spending over time
- Seasonal patterns

#### `network/` - Network Diagrams
**Status:** ⚪ Planned

For relationship visualization.

**Planned Charts:**
- Committee relationships
- Money flow network

### `templates/` - Chart Templates
Reusable templates for creating new charts.

**Files:**
- `chart_template.py` - Generic chart template
- `sankey_template.py` - Sankey-specific template

Use these as starting points when implementing new chart types.

### `scripts/` - Utility Scripts
Management and automation scripts.

**Files:**
- `generate_all_charts.py` - Run all chart generation scripts
- `validate_charts.py` - Validate generated charts
- `update_status.py` - Update chart status files

### `data/` - Data Files
Data sources for chart generation.

**Files:**
- `fec_committees_combined.parquet` - FEC committee data
- `outflows_schedule_b_recipients_2024.csv` - FEC outflows data

## 📋 File Organization Principles

### 1. Chart Type Separation
Each chart type has its own directory:
- Keeps related files together
- Easier to manage and scale
- Clear organization for developers

### 2. Documentation at Every Level
- Root level: Overall repository docs
- Chart type level: Type-specific docs
- File level: Inline code comments

### 3. Status Tracking
Each chart type directory has `.status` file:
- YAML format for easy parsing
- Tracks development progress
- Updated by `update_status.py` script

### 4. Consistent Naming
All files follow naming conventions:
- Chart files: `{type}_{description}_{year}.html`
- Scripts: `{action}_{type}.py`
- Data files: `{source}_{description}_{year}.{ext}`

## 🔄 File Relationships

```
CONFIG.yaml
    ↓
    ├─→ scripts/generate_all_charts.py
    │       ↓
    │       ├─→ analysis/unified_flow_sankey.py
    │       └─→ analysis/outflows_sankey_detailed.py
    │               ↓
    │               └─→ sankey/*.html
    │
    ├─→ scripts/validate_charts.py
    │       ↓
    │       └─→ Validates all *.html files
    │
    └─→ scripts/update_status.py
            ↓
            └─→ Updates .status files
```

## 📝 Adding New Files

### New Chart Type
1. Create directory: `charts/{chart_type}/`
2. Add `README.md` with documentation
3. Add `.status` file with initial status
4. Create generation script in `scripts/`
5. Update `CHART_STATUS.md`

### New Chart in Existing Type
1. Create generation script in `scripts/`
2. Update chart type's `README.md`
3. Update chart type's `.status` file
4. Update `CHART_STATUS.md`

### New Utility Script
1. Create in `scripts/` directory
2. Follow naming convention: `{action}_{type}.py`
3. Add docstring with usage instructions
4. Update `README.md` with usage

## 🔍 Finding Files

### By Purpose
- **Documentation:** Look in `README.md` files
- **Configuration:** Check `CONFIG.yaml`
- **Status:** Check `.status` files
- **Scripts:** Look in `scripts/` directory
- **Charts:** Look in chart type directories

### By Chart Type
- **Sankey:** `charts/sankey/`
- **Bar Charts:** `charts/bar_charts/`
- **Time Series:** `charts/time_series/`
- **Network:** `charts/network/`

### By Status
- **Production:** Check `CHART_STATUS.md` for 🟢 entries
- **In Development:** Check for 🔵 entries
- **Planned:** Check for ⚪ entries

## 📊 Statistics

| Category | Count |
|----------|-------|
| Documentation Files | 6 |
| Configuration Files | 1 |
| Status Files | 4 |
| Python Scripts | 4 |
| Chart Directories | 4 |
| Production Charts | 2 |
| Planned Charts | 8 |

## 🚀 Quick Navigation

### I want to...

**View chart status**
→ Open `CHART_STATUS.md`

**Understand naming conventions**
→ Open `NAMING_CONVENTIONS.md`

**Generate all charts**
→ Run `python3 scripts/generate_all_charts.py`

**Validate charts**
→ Run `python3 scripts/validate_charts.py`

**Create a new chart**
→ Copy `templates/chart_template.py` and follow `NAMING_CONVENTIONS.md`

**Update chart status**
→ Run `python3 scripts/update_status.py --chart {path} --status {status}`

**View configuration**
→ Open `CONFIG.yaml`

**Get quick reference**
→ Open `INDEX.md`

---

**Last Updated:** 2024-10-26


# Naming Conventions

Consistent naming standards for all chart files, data files, and scripts in the political-charts repository.

## 📊 Chart Output Files

### Format
```
{chart_type}_{description}_{year}.html
```

### Components

| Component | Description | Examples |
|-----------|-------------|----------|
| `chart_type` | Type of visualization | `sankey`, `bar`, `timeseries`, `network` |
| `description` | Brief chart description | `unified_flow`, `outflows_detailed`, `top_committees` |
| `year` | Data year (4 digits) | `2024`, `2023` |

### Examples

✅ **Good:**
- `sankey_unified_flow_2024.html`
- `sankey_outflows_detailed_2024.html`
- `bar_top_committees_2024.html`
- `timeseries_monthly_trends_2024.html`
- `network_committee_relationships_2024.html`

❌ **Bad:**
- `sankey.html` (missing description and year)
- `unified_flow_sankey_2024.html` (wrong order)
- `sankey_unified_flow_24.html` (year not 4 digits)
- `Sankey_Unified_Flow_2024.html` (inconsistent capitalization)

---

## 📁 Directory Names

### Format
```
{chart_type}/
```

### Standards
- All lowercase
- Use underscores for multi-word names
- No spaces or special characters
- Plural for collections, singular for specific items

### Examples

✅ **Good:**
- `sankey/`
- `bar_charts/`
- `time_series/`
- `network/`
- `templates/`
- `scripts/`

❌ **Bad:**
- `Sankey/` (capitalized)
- `bar-charts/` (hyphens instead of underscores)
- `time series/` (spaces)
- `sankey_diagrams/` (too verbose)

---

## 🐍 Python Script Names

### Format
```
{action}_{chart_type}.py
```

### Components

| Component | Description | Examples |
|-----------|-------------|----------|
| `action` | What the script does | `generate`, `validate`, `update`, `analyze` |
| `chart_type` | Type of chart (optional) | `sankey`, `bar`, `all` |

### Examples

✅ **Good:**
- `generate_sankey.py`
- `generate_all_charts.py`
- `validate_charts.py`
- `update_status.py`
- `analyze_data.py`

❌ **Bad:**
- `sankey.py` (no action verb)
- `generate_sankey_diagrams.py` (too verbose)
- `GenerateSankey.py` (wrong capitalization)
- `gen_sankey.py` (abbreviated action)

---

## 📊 Data File Names

### Format
```
{data_source}_{description}_{year}.{extension}
```

### Components

| Component | Description | Examples |
|-----------|-------------|----------|
| `data_source` | Origin of data | `fec`, `census`, `external` |
| `description` | What the data contains | `committees`, `outflows`, `recipients` |
| `year` | Data year (4 digits) | `2024`, `2023` |
| `extension` | File format | `csv`, `parquet`, `json` |

### Examples

✅ **Good:**
- `fec_committees_combined_2024.parquet`
- `fec_outflows_schedule_b_2024.csv`
- `fec_recipients_2024.json`
- `party_affiliation_mapping_2024.csv`

❌ **Bad:**
- `committees.parquet` (missing source and year)
- `fec_2024_committees.parquet` (wrong order)
- `FEC_Committees_2024.parquet` (inconsistent capitalization)
- `fec_committees_24.parquet` (year not 4 digits)

---

## 🏷️ Status File Names

### Format
```
.status
```

### Location
Each chart type directory contains a `.status` file tracking development status.

### Content Format
```yaml
chart_type: sankey
status: production  # production, review, development, planned
last_updated: 2024-10-26
version: 1.0
files:
  - unified_flow_2024.html
  - outflows_detailed_2024.html
```

### Examples

✅ **Good:**
- `sankey/.status`
- `bar_charts/.status`
- `time_series/.status`

---

## 📝 Configuration File Names

### Format
```
{purpose}.yaml
```

### Examples

✅ **Good:**
- `CONFIG.yaml` (global configuration)
- `colors.yaml` (color scheme configuration)
- `data_sources.yaml` (data source configuration)

---

## 🔤 Capitalization Rules

### File Names
- **All lowercase** for chart and data files
- **UPPERCASE** for configuration files (CONFIG.yaml, README.md)
- **Underscores** for word separation (never hyphens or spaces)

### Directory Names
- **All lowercase**
- **Underscores** for multi-word names

### Python Variables/Functions
- **snake_case** for variables and functions
- **PascalCase** for classes
- **UPPERCASE** for constants

---

## 🎨 Chart Type Abbreviations

Use these standardized abbreviations in file names:

| Chart Type | Abbreviation | Directory |
|-----------|--------------|-----------|
| Sankey Diagram | `sankey` | `sankey/` |
| Bar Chart | `bar` | `bar_charts/` |
| Time Series | `timeseries` | `time_series/` |
| Network Diagram | `network` | `network/` |
| Pie Chart | `pie` | `pie_charts/` |
| Heatmap | `heatmap` | `heatmaps/` |
| Scatter Plot | `scatter` | `scatter_plots/` |

---

## 📋 Description Keywords

Use these keywords in descriptions for consistency:

| Keyword | Meaning | Example |
|---------|---------|---------|
| `unified` | Complete/comprehensive view | `unified_flow` |
| `detailed` | Detailed/granular view | `outflows_detailed` |
| `top` | Top N items | `top_committees` |
| `comparison` | Comparative analysis | `party_comparison` |
| `trends` | Temporal trends | `monthly_trends` |
| `breakdown` | Category breakdown | `type_breakdown` |
| `relationships` | Entity relationships | `committee_relationships` |

---

## ✅ Validation Checklist

Before committing new files, verify:

- [ ] File name follows `{type}_{description}_{year}.{ext}` format
- [ ] All lowercase (except CONFIG files)
- [ ] Year is 4 digits
- [ ] No spaces or special characters (except underscores)
- [ ] Directory name is lowercase with underscores
- [ ] Script name follows `{action}_{type}.py` format
- [ ] Data file name includes source, description, and year
- [ ] Status file is named `.status` and in correct directory

---

## 🔄 Migration Guide

If renaming existing files:

1. Update file name to follow conventions
2. Update all references in scripts and documentation
3. Update CHART_STATUS.md
4. Update .status files
5. Commit with message: `refactor: rename {old_name} to {new_name}`

---

**Last Updated:** 2024-10-26


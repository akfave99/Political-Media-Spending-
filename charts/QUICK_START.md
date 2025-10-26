# Quick Start Checklist

Get up and running with the political-charts repository in minutes.

## ⚡ 5-Minute Quick Start

### Step 1: Verify Setup (1 min)
```bash
cd /Users/ak/Political-Media-Spending-
python3 --version          # Should be 3.8+
pip3 list | grep plotly    # Should show plotly 6.1.2+
ls analysis/outputs/*.parquet  # Should show data files
```

### Step 2: Generate Charts (2 min)
```bash
python3 charts/scripts/generate_all_charts.py
```

Expected output:
```
✅ SUCCESS: Sankey - Unified Flow
✅ SUCCESS: Sankey - Outflows Detailed
```

### Step 3: Validate Charts (1 min)
```bash
python3 charts/scripts/validate_charts.py
```

Expected output:
```
✅ sankey_unified_flow_2024.html
✅ sankey_outflows_detailed_2024.html
```

### Step 4: View Charts (1 min)
```bash
open analysis/outputs/sankey_unified_flow_2024.html
```

## 📋 Essential Commands

### View Status
```bash
python3 charts/scripts/update_status.py --show
```

### Generate All Charts
```bash
python3 charts/scripts/generate_all_charts.py
```

### Validate Charts
```bash
python3 charts/scripts/validate_charts.py
```

### Update Chart Status
```bash
python3 charts/scripts/update_status.py \
  --chart sankey/sankey_unified_flow_2024.html \
  --status production
```

## 📚 Essential Documentation

| Document | Purpose | Read Time |
|----------|---------|-----------|
| README.md | Overview | 5 min |
| CHART_STATUS.md | Current progress | 3 min |
| NAMING_CONVENTIONS.md | File naming | 5 min |
| INDEX.md | Quick reference | 2 min |
| SETUP_GUIDE.md | Detailed setup | 10 min |

## 🎯 Common Tasks

### I want to...

**View all charts**
```bash
ls analysis/outputs/*.html
```

**Check chart status**
```bash
python3 charts/scripts/update_status.py --show
```

**Generate specific chart**
```bash
python3 analysis/unified_flow_sankey.py
```

**Validate all charts**
```bash
python3 charts/scripts/validate_charts.py
```

**Create new chart**
1. Copy `charts/templates/chart_template.py`
2. Follow `NAMING_CONVENTIONS.md`
3. Place in `charts/scripts/`
4. Run `python3 charts/scripts/generate_all_charts.py`

**Update chart status**
```bash
python3 charts/scripts/update_status.py \
  --chart {path} --status production
```

## 🔍 File Locations

| Item | Location |
|------|----------|
| Charts | `analysis/outputs/*.html` |
| Configuration | `charts/CONFIG.yaml` |
| Status | `charts/CHART_STATUS.md` |
| Scripts | `charts/scripts/` |
| Templates | `charts/templates/` |
| Data | `analysis/outputs/*.parquet` |

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Plotly 6.1.2+ installed
- [ ] Data files exist in `analysis/outputs/`
- [ ] Charts directory created
- [ ] Scripts are executable
- [ ] Charts generate successfully
- [ ] Charts validate successfully
- [ ] Status shows correctly

## 🎨 Color Reference

Quick color reference for all charts:

```
Republican:  🔴 #CC0000 (full) / #FFB4B4 (light)
Democratic:  🔵 #003399 (full) / #ADD8E6 (light)
Unknown:     ⚫ #808080 (full) / #D3D3D3 (light)
```

## 📊 Chart Status

Current status of all charts:

```
🟢 PRODUCTION (2 charts)
  ├─ sankey_unified_flow_2024.html
  └─ sankey_outflows_detailed_2024.html

⚪ PLANNED (8 charts)
  ├─ bar_top_committees_2024.html
  ├─ bar_party_comparison_2024.html
  ├─ bar_committee_type_breakdown_2024.html
  ├─ timeseries_monthly_trends_2024.html
  ├─ timeseries_cumulative_spending_2024.html
  ├─ timeseries_seasonal_patterns_2024.html
  ├─ network_committee_relationships_2024.html
  └─ network_money_flow_network_2024.html
```

## 🚀 Next Steps

### Immediate (Today)
1. ✅ Run `python3 charts/scripts/generate_all_charts.py`
2. ✅ Run `python3 charts/scripts/validate_charts.py`
3. ✅ Open charts in browser
4. ✅ Review `README.md`

### Short Term (This Week)
1. Review `CHART_STATUS.md`
2. Understand naming conventions
3. Explore chart customization
4. Plan new charts

### Medium Term (This Month)
1. Implement bar charts
2. Implement time series
3. Add filtering capabilities
4. Create dashboard

## 🐛 Troubleshooting

### Charts not generating?
```bash
# Check data files
ls -la analysis/outputs/*.parquet

# Check Python packages
pip3 list | grep -E "plotly|pandas|numpy"

# Run with verbose output
python3 -u charts/scripts/generate_all_charts.py
```

### Colors not showing?
```bash
# Hard refresh browser
# Mac: Cmd+Shift+R
# Windows: Ctrl+Shift+R

# Validate charts
python3 charts/scripts/validate_charts.py
```

### Status not updating?
```bash
# Check file permissions
ls -la charts/sankey/.status

# Verify YAML syntax
python3 -c "import yaml; yaml.safe_load(open('charts/sankey/.status'))"
```

## 📞 Help Resources

| Issue | Resource |
|-------|----------|
| Setup problems | SETUP_GUIDE.md |
| File naming | NAMING_CONVENTIONS.md |
| Chart status | CHART_STATUS.md |
| Directory structure | DIRECTORY_STRUCTURE.md |
| Configuration | CONFIG.yaml |
| Quick reference | INDEX.md |

## 🎯 Success Criteria

You're ready when:
- ✅ Charts generate without errors
- ✅ Charts validate successfully
- ✅ Colors display correctly
- ✅ Status shows production-ready
- ✅ Documentation is clear

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
**Status:** Ready to Use  
**Charts:** 2 Production, 8 Planned


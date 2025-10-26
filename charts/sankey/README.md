# Sankey Diagrams

Interactive flow diagrams showing the movement of political money between entities.

## 📊 Available Charts

### 1. Unified Flow 2024
**File:** `sankey_unified_flow_2024.html`  
**Status:** 🟢 Production-Ready  
**Last Updated:** 2024-10-26

#### Description
Complete money flow visualization showing the journey of political contributions through four levels:
1. **Type** - Committee type (PAC, Party Committee, Candidate Committee)
2. **Designation** - Committee designation (Authorized, Unauthorized, Leadership PAC, etc.)
3. **Committee** - Actual committees (top 50 by receipts)
4. **Recipient** - Final recipients of outflows

#### Features
- 4-level hierarchical flow
- Top 50 committees by total receipts
- Party affiliation color coding
- Interactive Plotly visualization
- 1200x1600px canvas for optimal rendering
- Light colors for category nodes, vibrant colors for committees

#### Data Source
- FEC Committee data (2024 cycle)
- FEC Schedule B outflows
- Party affiliation mappings

#### Color Coding
- 🔴 **Red** - Republican committees (full) / Republican categories (light)
- 🔵 **Blue** - Democratic committees (full) / Democratic categories (light)
- ⚫ **Gray** - Unknown/Non-partisan entities

#### Generation
```bash
python3 analysis/unified_flow_sankey.py
```

#### Output
- HTML file with embedded Plotly visualization
- Fully interactive (hover, zoom, pan)
- Responsive design
- Standards Mode rendering (DOCTYPE included)

---

### 2. Outflows Detailed 2024
**File:** `sankey_outflows_detailed_2024.html`  
**Status:** 🟢 Production-Ready  
**Last Updated:** 2024-10-26

#### Description
Detailed outflows visualization showing the flow of money from committee types through specific committees to recipients.

#### Features
- 3-level hierarchical flow
- Committee type categorization
- Party affiliation color coding
- Interactive Plotly visualization
- Detailed recipient information

#### Data Source
- FEC Committee data (2024 cycle)
- FEC Schedule B outflows
- Party affiliation mappings

#### Generation
```bash
python3 analysis/outflows_sankey_detailed.py
```

#### Output
- HTML file with embedded Plotly visualization
- Fully interactive
- Standards Mode rendering

---

## 🎨 Color Scheme

| Party | Committee Color | Category Color | Hex (Committee) | Hex (Category) |
|-------|-----------------|----------------|-----------------|----------------|
| Republican | 🔴 Red | Light Red | #CC0000 | #FFB4B4 |
| Democratic | 🔵 Blue | Light Blue | #003399 | #ADD8E6 |
| Unknown | ⚫ Gray | Light Gray | #808080 | #D3D3D3 |

---

## 🔧 Technical Details

### Plotly Configuration
- **Version:** 6.1.2+
- **Rendering:** SVG-based
- **Interactivity:** Full hover, zoom, pan support
- **Responsiveness:** Adapts to viewport size

### Node Sizing
- Node height proportional to flow value
- Minimum node height: 1.0 pixel
- Padding between nodes: 15 pixels
- Node thickness: 20 pixels

### Link Styling
- Link opacity: 0.4 (40% transparent)
- Link color: Inherited from source node
- Link width: Proportional to flow value

### HTML Output
- DOCTYPE: HTML5 (`<!DOCTYPE html>`)
- Charset: UTF-8
- Viewport: Responsive
- Plotly CDN: Included

---

## 📈 Data Processing Pipeline

1. **Load FEC Data**
   - Committee data from parquet file
   - Outflows data from CSV file
   - Filter by cycle (2024)

2. **Build Party Map**
   - Map committee names to party affiliation
   - Infer party for category nodes from connected committees
   - Handle unknown/mixed affiliations

3. **Create Flows**
   - Level 1: Type → Designation
   - Level 2: Designation → Committee (top 50)
   - Level 3: Committee → Recipient

4. **Assign Colors**
   - Full colors for committee nodes
   - Light colors for category nodes
   - Gray for unknown affiliations

5. **Generate Visualization**
   - Create Plotly Sankey diagram
   - Apply styling and configuration
   - Output HTML file

---

## 🐛 Troubleshooting

### Colors Not Displaying
- **Issue:** Nodes appear gray instead of colored
- **Solution:** Hard refresh browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
- **Cause:** Browser cache or Quirks Mode rendering

### Nodes Too Small
- **Issue:** Nodes appear as thin lines
- **Solution:** Increase plot dimensions in configuration
- **Cause:** Insufficient canvas height for node calculation

### Missing Data
- **Issue:** Some committees not appearing
- **Solution:** Check data file exists and is not corrupted
- **Cause:** Data file missing or incomplete

---

## 📝 Customization

### Modify Colors
Edit `charts/CONFIG.yaml`:
```yaml
colors:
  republican:
    full: "#CC0000"
    light: "#FFB4B4"
```

### Change Top N Committees
Edit `analysis/unified_flow_sankey.py`:
```python
desig_cmte_flows = desig_cmte_flows.sort_values(ascending=False).head(50)  # Change 50
```

### Adjust Canvas Size
Edit `analysis/unified_flow_sankey.py`:
```python
fig.update_layout(height=1200, width=1600)  # Modify dimensions
```

---

## 🚀 Performance

- **File Size:** ~2-5 MB (depending on data)
- **Load Time:** 1-3 seconds (typical)
- **Interactivity:** Smooth on modern browsers
- **Memory Usage:** ~100-200 MB in browser

---

## 🔍 Quality Assurance

- ✅ DOCTYPE declaration present
- ✅ Colors render correctly in all modern browsers
- ✅ Node heights calculated properly
- ✅ Party affiliation inferred correctly
- ✅ Interactive features working
- ✅ Responsive design verified

---

## 📚 Related Files

- Generation scripts: `analysis/unified_flow_sankey.py`, `analysis/outflows_sankey_detailed.py`
- Configuration: `charts/CONFIG.yaml`
- Status tracker: `charts/CHART_STATUS.md`
- Naming conventions: `charts/NAMING_CONVENTIONS.md`

---

**Last Updated:** 2024-10-26


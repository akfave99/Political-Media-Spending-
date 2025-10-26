# Bar Charts

Comparative visualizations of political spending by category, party, and committee.

## 📊 Planned Charts

### 1. Top Committees by Spending
**File:** `bar_top_committees_2024.html`  
**Status:** ⚪ Planned  
**Priority:** High

#### Description
Horizontal bar chart showing the top 20 committees by total spending in 2024.

#### Features
- Top 20 committees ranked by spending
- Party affiliation color coding
- Interactive hover information
- Sortable/filterable (planned)

#### Data Source
- FEC Committee data (2024 cycle)
- FEC Schedule B outflows

#### Generation
```bash
python3 charts/scripts/generate_bar_top_committees.py
```

---

### 2. Party Spending Comparison
**File:** `bar_party_comparison_2024.html`  
**Status:** ⚪ Planned  
**Priority:** High

#### Description
Grouped bar chart comparing Republican vs Democratic spending across categories.

#### Features
- Side-by-side party comparison
- Category breakdown
- Percentage and absolute values
- Interactive legend

#### Data Source
- FEC Committee data with party affiliation
- FEC Schedule B outflows

#### Generation
```bash
python3 charts/scripts/generate_bar_party_comparison.py
```

---

### 3. Committee Type Breakdown
**File:** `bar_committee_type_breakdown_2024.html`  
**Status:** ⚪ Planned  
**Priority:** Medium

#### Description
Stacked bar chart showing spending distribution by committee type.

#### Features
- Stacked bars by committee type
- Party affiliation within each type
- Percentage breakdown
- Hover details

#### Data Source
- FEC Committee data (2024 cycle)

#### Generation
```bash
python3 charts/scripts/generate_bar_committee_type.py
```

---

## 🎨 Color Scheme

Same as other charts:
- 🔴 **Red** - Republican
- 🔵 **Blue** - Democratic
- ⚫ **Gray** - Unknown/Non-partisan

---

## 🔧 Technical Details

### Plotly Configuration
- **Chart Type:** Bar (horizontal and vertical)
- **Interactivity:** Hover, zoom, pan
- **Responsiveness:** Adaptive to viewport

### Styling
- Font: Arial, sans-serif
- Font size: 10-12px
- Margins: 50px (top, bottom, left, right)

---

## 📈 Development Roadmap

### Phase 1 (Q4 2024)
- [ ] Implement top committees chart
- [ ] Implement party comparison chart
- [ ] Add basic filtering

### Phase 2 (Q1 2025)
- [ ] Add committee type breakdown
- [ ] Implement advanced filtering
- [ ] Add export functionality

### Phase 3 (Q2 2025)
- [ ] Add time-based comparisons
- [ ] Implement drill-down capability
- [ ] Create dashboard integration

---

## 📝 Template

Use this template when creating new bar charts:

```python
import plotly.graph_objects as go
import pandas as pd

def generate_bar_chart(data, title, output_path):
    """Generate a bar chart from data."""
    
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Bar(
        x=data['category'],
        y=data['value'],
        marker_color=data['color'],
        name='Category'
    ))
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Category",
        yaxis_title="Amount ($)",
        height=600,
        width=1000,
        hovermode='x unified'
    )
    
    # Save
    fig.write_html(str(output_path))
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    # Load data
    data = pd.read_csv("data.csv")
    
    # Generate chart
    generate_bar_chart(data, "Chart Title", "output.html")
```

---

## 🚀 Getting Started

To implement a new bar chart:

1. Create script in `charts/scripts/generate_bar_*.py`
2. Follow naming conventions
3. Use template above
4. Update CHART_STATUS.md
5. Update this README
6. Test in multiple browsers
7. Commit with descriptive message

---

**Last Updated:** 2024-10-26


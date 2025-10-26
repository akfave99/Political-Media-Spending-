# Network Diagrams

Graph-based visualizations showing relationships between political entities.

## 📊 Planned Charts

### 1. Committee Relationships
**File:** `network_committee_relationships_2024.html`  
**Status:** ⚪ Planned  
**Priority:** Medium

#### Description
Interactive network graph showing connections between committees based on shared recipients or funding patterns.

#### Features
- Node-link diagram
- Committee nodes with party colors
- Edge thickness represents connection strength
- Interactive zoom and pan
- Hover information

#### Data Source
- FEC Committee data
- FEC Schedule B outflows
- Party affiliation mappings

---

### 2. Money Flow Network
**File:** `network_money_flow_network_2024.html`  
**Status:** ⚪ Planned  
**Priority:** Low

#### Description
Comprehensive network showing all money flows between entities.

#### Features
- Complete flow network
- Directional edges
- Node size represents total flow
- Color represents party affiliation
- Interactive filtering

#### Data Source
- FEC Committee data
- FEC Schedule B outflows

---

## 🎨 Color Scheme

- 🔴 **Red** - Republican
- 🔵 **Blue** - Democratic
- ⚫ **Gray** - Unknown/Non-partisan

---

## 📈 Development Roadmap

### Phase 1 (Q1 2025)
- [ ] Implement committee relationships network
- [ ] Add basic filtering

### Phase 2 (Q2 2025)
- [ ] Implement money flow network
- [ ] Add advanced filtering
- [ ] Add community detection

### Phase 3 (Q3 2025)
- [ ] Add temporal network analysis
- [ ] Implement network statistics
- [ ] Create dashboard integration

---

## 🔧 Technical Considerations

Network diagrams require:
- Graph layout algorithm (force-directed, hierarchical, etc.)
- Edge bundling for clarity
- Performance optimization for large networks
- Interactive filtering and search

---

**Last Updated:** 2024-10-26


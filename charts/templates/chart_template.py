#!/usr/bin/env python3
"""
Template for creating new political visualization charts.

Copy this file and modify for your specific chart type.
"""

import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
import yaml

# Configuration
CONFIG_FILE = Path(__file__).parent.parent / "CONFIG.yaml"

def load_config():
    """Load global configuration."""
    with open(CONFIG_FILE, 'r') as f:
        return yaml.safe_load(f)

def load_data(config):
    """Load data for the chart."""
    # Example: Load FEC committee data
    data_dir = Path(config['charts']['data_dir'])
    
    # Load your data here
    # df = pd.read_parquet(data_dir / "fec_committees_combined.parquet")
    
    return None  # Replace with actual data

def process_data(df, config):
    """Process data for visualization."""
    # Transform and aggregate data as needed
    return df

def create_chart(data, config):
    """Create the visualization."""
    fig = go.Figure()
    
    # Add traces
    # Example for bar chart:
    # fig.add_trace(go.Bar(
    #     x=data['category'],
    #     y=data['value'],
    #     marker_color=data['color'],
    #     name='Category'
    # ))
    
    # Update layout
    fig.update_layout(
        title="Chart Title",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        height=config['plotly']['layout']['height'],
        width=config['plotly']['layout']['width'],
        font=dict(
            family=config['defaults']['font']['family'],
            size=config['defaults']['font']['size']
        ),
        hovermode='closest'
    )
    
    return fig

def save_chart(fig, output_path):
    """Save chart to HTML file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    fig.write_html(
        str(output_path),
        include_plotlyjs=True,
        config={'responsive': True}
    )
    
    print(f"✅ Saved: {output_path}")

def main():
    """Main entry point."""
    # Load configuration
    config = load_config()
    
    # Load data
    df = load_data(config)
    if df is None:
        print("❌ Failed to load data")
        return 1
    
    # Process data
    df = process_data(df, config)
    
    # Create chart
    fig = create_chart(df, config)
    
    # Save chart
    output_dir = Path(config['charts']['output_dir'])
    output_path = output_dir / "chart_name_2024.html"
    save_chart(fig, output_path)
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())


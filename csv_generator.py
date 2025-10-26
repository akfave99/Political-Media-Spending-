#!/usr/bin/env python3
"""
CSV Generator for FEC Reports
Automatically generates CSV files from Excel reports
"""

import pandas as pd
import os
from datetime import datetime

def create_csv_files_from_excel(excel_filename, data=None):
    """
    Create CSV files from Excel report
    
    Args:
        excel_filename: Path to the Excel file
        data: Optional data dictionary (for compatibility)
    
    Returns:
        List of created CSV filenames
    """
    print(f"📊 Creating CSV files from {excel_filename}")
    
    if not os.path.exists(excel_filename):
        print(f"❌ Excel file not found: {excel_filename}")
        return []
    
    # Extract timestamp from Excel filename for CSV files
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    csv_files_created = []
    
    # Define sheets to convert to CSV
    sheets_to_convert = {
        'Top Republicans': f'FEC_Republicans_{timestamp}.csv',
        'Top Democrats': f'FEC_Democrats_{timestamp}.csv', 
        'Committee Analysis': f'FEC_Committees_{timestamp}.csv',
        'Geographic Analysis': f'FEC_Geographic_{timestamp}.csv',
        'PVI Analysis': f'FEC_PVI_Analysis_{timestamp}.csv',
        'Political Metrics': f'FEC_Political_Metrics_{timestamp}.csv'
    }
    
    try:
        # Read Excel file and get available sheets
        excel_file = pd.ExcelFile(excel_filename)
        available_sheets = excel_file.sheet_names
        
        print(f"📋 Available sheets: {available_sheets}")
        
        for sheet_name, csv_filename in sheets_to_convert.items():
            if sheet_name in available_sheets:
                try:
                    # Read sheet data
                    df = pd.read_excel(excel_filename, sheet_name=sheet_name)
                    
                    # Skip empty sheets
                    if df.empty:
                        print(f"⚠️ Skipping empty sheet: {sheet_name}")
                        continue
                    
                    # Save as CSV
                    df.to_csv(csv_filename, index=False)
                    file_size = os.path.getsize(csv_filename)
                    csv_files_created.append(csv_filename)
                    
                    print(f"✅ {sheet_name} → {csv_filename} ({file_size:,} bytes, {len(df)} rows)")
                    
                except Exception as e:
                    print(f"⚠️ Error converting {sheet_name}: {e}")
            else:
                print(f"⚠️ Sheet not found: {sheet_name}")
        
        excel_file.close()
        
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        return []
    
    print(f"📊 CSV generation complete: {len(csv_files_created)} files created")
    return csv_files_created

def add_csv_generation_to_fec_system():
    """
    Add CSV generation method to the FEC system class
    This method can be called to patch the existing system
    """
    
    csv_method_code = '''
    def _create_csv_files(self, excel_filename, data):
        """Create CSV files from the Excel report data"""
        print("📊 Generating CSV files from Excel report...")
        
        # Import the CSV generator
        from csv_generator import create_csv_files_from_excel
        
        # Generate CSV files
        csv_files = create_csv_files_from_excel(excel_filename, data)
        
        return csv_files
    '''
    
    return csv_method_code

if __name__ == "__main__":
    # Test the CSV generation with the latest Excel file
    import glob
    
    # Find the most recent Excel file
    excel_files = glob.glob("FEC_Final_Enhanced_*.xlsx")
    if excel_files:
        latest_file = max(excel_files, key=os.path.getctime)
        print(f"🧪 Testing CSV generation with: {latest_file}")
        
        csv_files = create_csv_files_from_excel(latest_file)
        
        print(f"\n📊 TEST RESULTS:")
        print(f"✅ CSV files created: {len(csv_files)}")
        for csv_file in csv_files:
            size = os.path.getsize(csv_file)
            print(f"   📄 {csv_file}: {size:,} bytes")
    else:
        print("❌ No Excel files found for testing")

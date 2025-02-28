#!/usr/bin/env python3
"""
Convert USA Enhanced Travel Queries Forecast CSV to Excel

This script converts the USA Enhanced Travel Queries Forecast CSV file to Excel format,
preserving the structure and formatting of the original file.
"""

import pandas as pd
import os

def convert_csv_to_excel(csv_path, excel_path):
    """
    Convert a CSV file to Excel format.
    
    Parameters:
    - csv_path: Path to the CSV file
    - excel_path: Path to save the Excel file
    """
    # Read the CSV file
    with open(csv_path, 'r') as file:
        content = file.read()
    
    # Split the content by section markers
    sections = content.split('====================')
    
    # Create a new Excel writer
    writer = pd.ExcelWriter(excel_path, engine='openpyxl')
    
    # Process each section
    for i, section in enumerate(sections):
        if not section.strip():
            continue
        
        # Extract the section name
        lines = section.strip().split('\n')
        section_name = lines[0].strip().replace(',', '')
        
        if i == 0:
            # This is the header section
            section_name = 'Overview'
        
        # Ensure section name is not empty
        if not section_name:
            section_name = f'Section_{i}'
        
        # Limit section name length to 31 characters (Excel sheet name limit)
        if len(section_name) > 31:
            section_name = section_name[:31]
        
        # Parse the section data
        section_data = []
        for line in lines[1:]:
            if line.strip():
                section_data.append(line.split(','))
        
        # Create a DataFrame
        if section_data:
            df = pd.DataFrame(section_data)
            
            # Write to Excel
            df.to_excel(writer, sheet_name=section_name, index=False, header=False)
            
            # Auto-adjust column widths
            worksheet = writer.sheets[section_name]
            for idx, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(str(col)))
                worksheet.column_dimensions[chr(65 + idx)].width = max_len + 2
    
    # Save the Excel file
    writer.close()
    
    print(f"Converted {csv_path} to {excel_path}")

if __name__ == "__main__":
    # Define paths
    csv_path = "Travel_Queries_Forecast_USA.csv"
    excel_path = "Travel_Queries_Forecast_USA_Enhanced.xlsx"
    
    # Convert CSV to Excel
    convert_csv_to_excel(csv_path, excel_path)

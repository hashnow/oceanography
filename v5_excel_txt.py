import pandas as pd

# Input files
input_xls = "RA_Data_2011_2024_kenya.xls"  # Replace with your actual file
output_csv = "stacked_values.csv"          # Output file

# Function to extract and stack values column-first
def extract_and_stack(df, source_name):
    # Select columns 2 to 12 (i.e., 3rd to 13th columns) and first 30 rows
    selected_data = df.iloc[:31, 2:14]

    # Stack column-wise: one full column, then next
    stacked_values = []
    column_labels = []
    for col in selected_data.columns:
        stacked_values.extend(selected_data[col].tolist())
        column_labels.extend([col] * len(selected_data))

    # Create DataFrame with source indicator and original column name
    result = pd.DataFrame({
        'Value': stacked_values,
        'Source': source_name,
        'Original_Column': column_labels
    })
    return result

# Read Excel (first sheet)
sheets_dict = pd.read_excel(input_xls, sheet_name=None)
first_sheet_name = list(sheets_dict.keys())[0]
df_xls = pd.read_excel(input_xls, sheet_name=first_sheet_name)

# Process and save
stacked_xls = extract_and_stack(df_xls, "Excel")
stacked_xls.to_csv(output_csv, index=False)

print(stacked_xls.head())
print(f"\nAll values stacked column-wise and saved to: {output_csv}")
print(f"Total values: {len(stacked_xls)}")


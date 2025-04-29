import pandas as pd

# Input and output files
input_xls = "RA_Data_2011_2024_kenya.xls"
output_csv = "combined_stacked_values.csv"

# Function to extract and stack values column-wise from a row chunk
def extract_and_stack(df_chunk, source_name, chunk_index, start_year):
    stacked_values = []
    column_labels = []
    row_labels = []
    year_labels = []

    current_year = start_year + chunk_index

    for col in df_chunk.columns:
        column_data = df_chunk[col].tolist()
        stacked_values.extend(column_data)
        column_labels.extend([col] * len(column_data))
        row_labels.extend(range(chunk_index * len(df_chunk), chunk_index * len(df_chunk) + len(column_data)))
        year_labels.extend([current_year] * len(column_data))

    result = pd.DataFrame({
        'Value': stacked_values,
        'Source': source_name,
        'Original_Column': column_labels,
        'Row_Index': row_labels,
        'Year': year_labels
    })
    return result

# Read the Excel file and get first sheet
sheets_dict = pd.read_excel(input_xls, sheet_name=None)
first_sheet_name = list(sheets_dict.keys())[0]
df_xls = pd.read_excel(input_xls, sheet_name=first_sheet_name)

# Select columns 3–13 (i.e., index 2:13)
data = df_xls.iloc[:, 2:13]
total_rows = data.shape[0]
chunk_size = 31
start_year = 2011

# Process in row chunks and accumulate
all_chunks = []
for i in range(0, total_rows, chunk_size):
    df_chunk = data.iloc[i:i+chunk_size]
    if not df_chunk.empty:
        chunk_index = i // chunk_size
        stacked_chunk = extract_and_stack(df_chunk, "Excel", chunk_index, start_year)
        all_chunks.append(stacked_chunk)

# Combine and save
final_df = pd.concat(all_chunks, ignore_index=True)
final_df.to_csv(output_csv, index=False)

print(final_df.head())
print(f"\nProcessed in chunks and saved to: {output_csv}")
print(f"Total stacked values: {len(final_df)}")


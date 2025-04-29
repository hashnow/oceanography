import pandas as pd

# Input and output filenames
input_file = "RA_Data_2011_2024_kenya.xls"  # Replace with your actual file
output_file = "reshaped_data.txt"

# Read all sheets to get the first sheet name
sheets_dict = pd.read_excel(input_file, sheet_name=None)
first_sheet_name = list(sheets_dict.keys())[0]

print(first_sheet_name)

# Read only the first sheet
df = pd.read_excel(input_file, sheet_name=first_sheet_name)

# Get the first column
first_column_name = df.columns[2]
first_column_data = df[first_column_name].head(30)

# Print the first 30 values from the fcirst column
print(f"First column name: {first_column_name}")
print("First 30 values:")
print(first_column_data)

# Get all column names and their first 30 values
columns_data = [(col, df[col].head(30).tolist()) for col in df.columns]

# Print results
for col, values in columns_data:
    print(f"\nColumn: {col}")
    print("First 30 values:", values)

# Assume columns are named 'Jan', 'Feb', ..., 'Dec' (modify if different)
monthly_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Collapse all monthly data into a single list
all_months_data = [value for col in monthly_columns 
                   for value in df[col].dropna().tolist()]

# Print the first 30 values of the combined list
print("First 30 values of collapsed monthly data:")
print(all_months_data[:30])

# (Optional) Save to a file
with open("collapsed_data.txt", "w") as f:
    f.write(str(all_months_data))

# --- Save as CSV (single column) ---
output_csv = "collapsed_data.csv"
pd.DataFrame(all_months_data, columns=["Value"]).to_csv(output_csv, index=False)
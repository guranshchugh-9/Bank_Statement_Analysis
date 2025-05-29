import pandas as pd
import os
import re

OUTPUT_FOLDER = "processed_files/"
excel_files = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".xlsx")]

if not excel_files:
    print("No Excel file found in processed folder!")
    exit()

excel_file = os.path.join(OUTPUT_FOLDER, excel_files[0])

def clean_table(df):
    cleaned_rows = []
    current_row = None

    if 'Date' not in df.columns:
        print("Skipping sheet due to missing 'Date' column.")
        return pd.DataFrame()

    for index, row in df.iterrows():
        if pd.notna(row['Date']):
            if current_row is not None:
                cleaned_rows.append(current_row)
            current_row = row
        else:
            if current_row is None:
                continue
            current_row['Narration'] = f"{str(current_row['Narration']).strip()} {str(row['Narration']).strip()}"

    if current_row is not None:
        cleaned_rows.append(current_row)

    return pd.DataFrame(cleaned_rows)

all_tables = pd.read_excel(excel_file, sheet_name=None, engine="openpyxl")
combined_df = pd.concat([clean_table(df) for df in all_tables.values()], ignore_index=True)

csv_output = os.path.join(OUTPUT_FOLDER, "cleaned_bank_statement.csv")
combined_df.to_csv(csv_output, index=False)
print(f"Cleaned data saved to: {csv_output}")
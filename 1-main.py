import os
import subprocess

UPLOAD_FOLDER = "uploads/"
OUTPUT_FOLDER = "processed_files/"

# Ensure required folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Use 'python3' instead of 'python' in macOS
PYTHON_CMD = "python3"  

# 1. Convert PDF to Excel
print("Step 1: Converting PDF to Excel...")
subprocess.run([PYTHON_CMD, "2-convert_pdf_to_excel.py"], check=True)

# 2. Clean the extracted data
print("Step 2: Cleaning bank statement...")
subprocess.run([PYTHON_CMD, "3-clean_data.py"], check=True)

# 3. Categorize transactions
print("Step 3: Categorizing transactions...")
subprocess.run([PYTHON_CMD, "4-categorize_transactions.py"], check=True)

# 4. Generate Financial Summary
print("Step 4: Calculating Income/Expenditure...")
subprocess.run([PYTHON_CMD, "5-financial_summary.py"], check=True)

# 5. Generate Graphs
print("Step 5: Generating Graphs...")
subprocess.run([PYTHON_CMD, "6-generate_graphs.py"], check=True)

# 6. Send Data to Frontend
print("Step 6: Sending Graphs to Frontend...")
subprocess.run([PYTHON_CMD, "7-backend.py"], check=True)

print("All steps completed successfully!")

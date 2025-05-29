import convertapi
import os
import sys


UPLOAD_FOLDER = "uploads/"
OUTPUT_FOLDER = "processed_files/"

pdf_path = sys.argv[1]
password = sys.argv[2]

# Ensure API Key
convertapi.api_credentials = "secret_J5o8W6vzZVtDYVms"

# Get the uploaded file
pdf_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".pdf")]
if not pdf_files:
    print("No PDF found in uploads folder!")
    exit()

pdf_path = os.path.join(UPLOAD_FOLDER, pdf_files[0])

# Convert PDF to Excel
print(f"Processing PDF: {pdf_path}")
convertapi.convert('xlsx', {
    'File': pdf_path,
    'password': password,
    'OcrLanguage': 'en',
}, from_format='pdf').save_files(OUTPUT_FOLDER)

print("PDF conversion complete!")